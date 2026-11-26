"""
Web server for the QA module 4 labs site.

Serves the single-page site (index.html) and these JSON endpoints:

    GET /api/weather?place=London       current weather (Optional Task 2)
    GET /api/postcode?code=SW1A 1AA     postcode coordinates (Optional Task 3)
    GET /api/football?league=sco.1&team=Celtic&date=20261121
                                        football matches (Day 4 workshop);
                                        team and date are optional
    GET /api/modules                    list of the Module 1-8 lab files
    GET /api/solutions                  list of the module solution files
    GET /api/module-file?path=...       text of one listed lab or solution file

Uses only the Python standard library. Run it with:

    python3 server.py

then open http://127.0.0.1:8000 in a browser. To use another port:

    PORT=8001 python3 server.py

The server listens on 127.0.0.1 (this computer only) unless HOST is set. In a
container, set HOST=0.0.0.0 so the site can be reached from outside.
"""

import json
import os
import sys
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

WEB_DIR = Path(__file__).resolve().parent
REPO_DIR = WEB_DIR.parent

# Import the task code from its own folders.
sys.path.insert(0, str(REPO_DIR / "Optional" / "Optional-Task-2"))
sys.path.insert(0, str(REPO_DIR / "Optional" / "Optional-Task-3"))
sys.path.insert(0, str(REPO_DIR / "DAY4-Workshop" / "football-monitor" / "part8-documentation"))
sys.path.insert(0, str(WEB_DIR))

from football_monitor import ApiError as FootballApiError  # noqa: E402
from football_monitor import fetch_scoreboard, filter_by_team, league_name, parse_matches  # noqa: E402
from modules import MODULES, SOLUTIONS, allowed_paths  # noqa: E402
from postcode_lookup import PostcodeError, PostcodeNotFound, load_postcodes, lookup_postcode  # noqa: E402
from weather import WeatherError, get_weather_for_place  # noqa: E402

HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "8000"))
PAGE_PATH = WEB_DIR / "index.html"


class SiteRequestHandler(BaseHTTPRequestHandler):
    """Routes requests to the page, the APIs and the lab files."""

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)

        if parsed.path in ("/", "/index.html"):
            self.send_page()
        elif parsed.path == "/api/weather":
            self.send_weather(query.get("place", [""])[0])
        elif parsed.path == "/api/postcode":
            self.send_postcode(query.get("code", [""])[0])
        elif parsed.path == "/api/football":
            self.send_football(
                query.get("league", [""])[0].strip(),
                query.get("team", [""])[0].strip(),
                query.get("date", [""])[0].strip(),
            )
        elif parsed.path == "/api/modules":
            self.send_json(200, MODULES)
        elif parsed.path == "/api/solutions":
            self.send_json(200, SOLUTIONS)
        elif parsed.path == "/api/module-file":
            self.send_module_file(query.get("path", [""])[0])
        else:
            self.send_json(404, {"error": "Page not found."})

    def send_page(self):
        self.send_bytes(200, "text/html; charset=utf-8", PAGE_PATH.read_bytes())

    def send_weather(self, place):
        place = place.strip()
        if not place:
            self.send_json(400, {"error": "Enter a place name."})
            return

        try:
            weather = get_weather_for_place(place)
        except WeatherError as error:
            self.send_json(404, {"error": str(error)})
        except OSError:
            self.send_json(
                502,
                {"error": "Unable to reach Open-Meteo. Check your internet connection."},
            )
        except (KeyError, ValueError):
            self.send_json(
                502,
                {"error": "Open-Meteo returned data in an unexpected format."},
            )
        else:
            self.send_json(200, weather)

    def send_postcode(self, code):
        try:
            result = lookup_postcode(self.server.postcodes, code)
        except PostcodeNotFound as error:
            self.send_json(404, {"error": str(error)})
        except PostcodeError as error:
            self.send_json(400, {"error": str(error)})
        else:
            self.send_json(200, result)

    def send_football(self, league, team, date):
        if not league:
            self.send_json(400, {"error": "Choose a league."})
            return
        if date and not (date.isdigit() and len(date) == 8):
            self.send_json(400, {"error": "The date must be in the form YYYYMMDD."})
            return

        try:
            data = fetch_scoreboard(league, date)
            all_matches = parse_matches(data)
            matches = filter_by_team(all_matches, team)
            name = league_name(data, league)
        except FootballApiError as error:
            self.send_json(502, {"error": str(error)})
            return
        except (AttributeError, KeyError, TypeError):
            self.send_json(502, {"error": "ESPN returned data in an unexpected format."})
            return

        self.send_json(200, {
            "league": name,
            "team": team,
            "date": date,
            "total": len(all_matches),
            "matches": [
                {"result": m.result_text(), "status": m.status_text(), "started": m.started}
                for m in matches
            ],
        })

    def send_module_file(self, relative_path):
        if relative_path not in allowed_paths():
            self.send_json(404, {"error": "That lab file is not on the list."})
            return

        try:
            text = (REPO_DIR / relative_path).read_text(encoding="utf-8", errors="replace")
        except OSError:
            self.send_json(404, {"error": "That lab file could not be read."})
            return

        self.send_json(200, {"path": relative_path, "content": text})

    def send_json(self, status, data):
        body = json.dumps(data).encode("utf-8")
        self.send_bytes(status, "application/json; charset=utf-8", body)

    def send_bytes(self, status, content_type, body):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    """Load the postcode data, then serve the site on localhost until Ctrl+C."""
    try:
        server = ThreadingHTTPServer((HOST, PORT), SiteRequestHandler)
    except OSError as error:
        sys.exit(
            f"Could not start the server on port {PORT}: {error}\n"
            "Another program is probably using that port. Stop it, or pick "
            f"another port, for example: PORT={PORT + 1} python3 server.py"
        )

    print("Loading UK postcodes...")
    server.postcodes = load_postcodes()
    print(f"Site running at http://{HOST}:{PORT} (press Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
