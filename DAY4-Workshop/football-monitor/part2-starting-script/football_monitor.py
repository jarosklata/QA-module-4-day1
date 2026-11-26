"""
Football Match Monitor, Part 2: starting script.

Calls the ESPN Football API for the Scottish Premiership and prints basic
information about each match.

Notes for the review questions:
- The API URL ends in .../soccer/sco.1/scoreboard. "sco.1" is the league code
  (eng.1 is the English Premier League). "scoreboard" returns the matches for
  the current matchday.
- This script uses urllib from the standard library to make the request, so
  no packages need installing. The requests library does the same job.
- The JSON response has a top-level "events" list. Each event is one match,
  with a "name", a "date", a "status" and the teams under "competitions".

Run it in the terminal with:  python3 football_monitor.py
"""

import json
import urllib.request

API_URL = "https://site.api.espn.com/apis/site/v2/sports/soccer/sco.1/scoreboard"


def main():
    with urllib.request.urlopen(API_URL, timeout=10) as response:
        data = json.load(response)

    for event in data["events"]:
        print(f"{event['name']} ({event['date']})")


if __name__ == "__main__":
    main()
