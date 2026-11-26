"""
Football Match Monitor, Part 5: add configuration.

Reads the league, team filter and output file from config.json, gets the
matches from the ESPN Football API, keeps the matches involving the chosen
team, and writes a report.

config.json settings:
    league        ESPN league code, such as "sco.1" or "eng.1"
    team_filter   only matches involving this team; "" keeps every match
    output_file   report file name, saved next to this script
    date          optional, YYYYMMDD. Without it the API returns the current
                  matchday. With it you can look at earlier results.

Usage:
    python3 football_monitor.py                    # uses config.json next to the script
    python3 football_monitor.py path/to/other.json # uses another config file

Uses only the Python standard library, so no packages need installing.
"""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

API_URL = "https://site.api.espn.com/apis/site/v2/sports/soccer/{league}/scoreboard"
TIMEOUT_SECONDS = 10
SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = SCRIPT_DIR / "config.json"


class ConfigError(Exception):
    """Raised when config.json is missing or contains unusable settings."""


class ApiError(Exception):
    """Raised when the ESPN API can't be reached or returns unusable data."""


@dataclass
class Match:
    """One match, converted from the JSON returned by the API."""

    home_team: str
    away_team: str
    home_score: str
    away_score: str
    status: str
    kickoff: str
    started: bool

    def result_text(self):
        """Return 'Celtic 2 - 1 Rangers', or 'Celtic v Rangers' before kick-off."""
        if self.started:
            return f"{self.home_team} {self.home_score} - {self.away_score} {self.away_team}"
        return f"{self.home_team} v {self.away_team}"

    def status_text(self):
        """Return the status, with the kick-off time for matches not yet played."""
        if self.started:
            return self.status
        return f"{self.status} - {self.kickoff}"


def load_config(path):
    """Read and check the config file. Returns a dictionary of settings."""
    try:
        with open(path, encoding="utf-8") as file:
            config = json.load(file)
    except FileNotFoundError:
        raise ConfigError(f"Config file not found: {path}") from None
    except json.JSONDecodeError as error:
        raise ConfigError(f"Config file is not valid JSON: {error}") from None
    except OSError as error:
        raise ConfigError(f"Config file could not be read: {error}") from None

    if not isinstance(config, dict):
        raise ConfigError("Config file must contain a JSON object.")

    for key in ("league", "output_file"):
        value = config.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ConfigError(f"Config setting '{key}' must be a non-empty text value.")

    team_filter = config.get("team_filter", "")
    if not isinstance(team_filter, str):
        raise ConfigError("Config setting 'team_filter' must be text.")

    date = config.get("date", "")
    if not isinstance(date, str) or (date and not (date.isdigit() and len(date) == 8)):
        raise ConfigError("Config setting 'date' must be in the form YYYYMMDD.")

    return {
        "league": config["league"].strip(),
        "team_filter": team_filter.strip(),
        "output_file": config["output_file"].strip(),
        "date": date,
    }


def fetch_scoreboard(league, date=""):
    """Call the ESPN API and return the JSON as a dictionary."""
    url = API_URL.format(league=urllib.parse.quote(league, safe=""))
    if date:
        url += "?" + urllib.parse.urlencode({"dates": date})

    try:
        with urllib.request.urlopen(url, timeout=TIMEOUT_SECONDS) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        raise ApiError(f"ESPN returned HTTP {error.code} for league '{league}'.") from None
    except OSError as error:
        raise ApiError(f"Could not reach the ESPN API: {error}") from None
    except json.JSONDecodeError:
        raise ApiError("ESPN returned data that is not valid JSON.") from None


def format_kickoff(text):
    """Turn '2026-11-28T15:00Z' into 'Sat 28 Nov 15:00 UTC'."""
    try:
        return datetime.strptime(text, "%Y-%m-%dT%H:%MZ").strftime("%a %d %b %H:%M UTC")
    except ValueError:
        return text


def league_name(data, fallback):
    """Return the league's full name from the API's JSON, or the fallback."""
    try:
        return data["leagues"][0]["name"]
    except (KeyError, IndexError, TypeError):
        return fallback


def parse_matches(data):
    """Return a list of Match objects from the API's JSON."""
    matches = []
    for event in data.get("events", []):
        try:
            teams = {c["homeAway"]: c for c in event["competitions"][0]["competitors"]}
            status = event["status"]["type"]
            matches.append(Match(
                home_team=teams["home"]["team"]["displayName"],
                away_team=teams["away"]["team"]["displayName"],
                home_score=str(teams["home"].get("score", "0")),
                away_score=str(teams["away"].get("score", "0")),
                status=status["description"],
                kickoff=format_kickoff(event["date"]),
                started=status["state"] != "pre",
            ))
        except (KeyError, IndexError, TypeError):
            continue  # Skip a match whose data is not in the expected shape.
    return matches


def filter_by_team(matches, team):
    """Return the matches where the home or away team name contains `team`.

    The comparison ignores upper and lower case. A blank team keeps every match.
    """
    team = team.strip().lower()
    if not team:
        return matches
    return [m for m in matches if team in m.home_team.lower() or team in m.away_team.lower()]


def build_report(name, config, matches):
    """Return the report as text."""
    lines = [
        "Football Match Monitor",
        f"League: {name}",
        f"Team filter: {config['team_filter'] or 'none'}",
        f"Date: {config['date'] or 'current matchday'}",
        f"Generated: {datetime.now():%Y-%m-%d %H:%M}",
        f"Matches: {len(matches)}",
        "",
    ]
    if not matches:
        lines.append("No matches found.")
    for match in matches:
        lines.append(match.result_text())
        lines.append(f"Status: {match.status_text()}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_report(output_file, text):
    """Save the report next to this script, and return the path."""
    path = SCRIPT_DIR / output_file
    path.write_text(text, encoding="utf-8")
    return path


def main(argv=None):
    """Run the monitor. Returns 0 on success and 1 if something went wrong."""
    argv = sys.argv[1:] if argv is None else argv
    config_path = Path(argv[0]) if argv else CONFIG_PATH

    try:
        config = load_config(config_path)
        data = fetch_scoreboard(config["league"], config["date"])
        matches = filter_by_team(parse_matches(data), config["team_filter"])
        report = build_report(league_name(data, config["league"]), config, matches)
        path = write_report(config["output_file"], report)
    except (ConfigError, ApiError, OSError) as error:
        print(f"Error: {error}")
        return 1

    print(report)
    print(f"Report saved to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
