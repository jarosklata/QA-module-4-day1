"""
Football Match Monitor, Part 4: add a business rule.

Calls the ESPN Football API for the Scottish Premiership and prints only the
matches involving one team (Option A in the workshop). The team name is set
in TEAM_FILTER for now. It moves to a config file in Part 5.

Run it in the terminal with:  python3 football_monitor.py

Uses only the Python standard library, so no packages need installing.
"""

import json
import urllib.request
from dataclasses import dataclass
from datetime import datetime

API_URL = "https://site.api.espn.com/apis/site/v2/sports/soccer/sco.1/scoreboard"
TIMEOUT_SECONDS = 10
TEAM_FILTER = "Celtic"


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


def fetch_scoreboard():
    """Call the ESPN API and return the JSON as a dictionary."""
    with urllib.request.urlopen(API_URL, timeout=TIMEOUT_SECONDS) as response:
        return json.load(response)


def format_kickoff(text):
    """Turn '2026-11-28T15:00Z' into 'Sat 28 Nov 15:00 UTC'."""
    try:
        return datetime.strptime(text, "%Y-%m-%dT%H:%MZ").strftime("%a %d %b %H:%M UTC")
    except ValueError:
        return text


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


def main():
    matches = filter_by_team(parse_matches(fetch_scoreboard()), TEAM_FILTER)

    if not matches:
        print(f"No matches found for '{TEAM_FILTER}'.")
        return

    for match in matches:
        print(match.result_text())
        print(f"Status: {match.status_text()}")
        print()


if __name__ == "__main__":
    main()
