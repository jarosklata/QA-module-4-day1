"""
TVMaze show search (Module 6 Lab).

Reads the search term and minimum rating from config.json, calls the TVMaze
search API, converts each JSON result into a Show object, and displays the
shows that meet the minimum rating.

Uses only the Python standard library, so no packages need installing.
"""

import json
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

API_URL = "https://api.tvmaze.com/search/shows"
CONFIG_PATH = Path(__file__).resolve().parent / "config.json"


@dataclass
class Show:
    """A TV show, converted from the JSON returned by the API."""

    name: str
    genres: List[str]
    rating: Optional[float]

    def genre_text(self):
        """Return the genres as one comma-separated string."""
        return ", ".join(self.genres) if self.genres else "Unknown"

    def rating_text(self):
        """Return the rating, or a message when TVMaze has none."""
        return str(self.rating) if self.rating is not None else "No rating"


def load_config(path=CONFIG_PATH):
    """Read search_term and minimum_rating from config.json.

    Returns a (search_term, minimum_rating) tuple. Stops with a helpful
    message if the file is missing, is not valid JSON, or lacks a setting.
    """
    try:
        with open(path, encoding="utf-8") as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        raise SystemExit(
            f"Configuration file not found: {path}\n"
            "Create config.json in the same folder as this script."
        )
    except json.JSONDecodeError as error:
        raise SystemExit(f"config.json is not valid JSON: {error}")

    try:
        search_term = str(config["search_term"]).strip()
        minimum_rating = float(config["minimum_rating"])
    except KeyError as error:
        raise SystemExit(f"config.json is missing the {error} setting.")
    except (TypeError, ValueError):
        raise SystemExit("config.json: minimum_rating must be a number.")

    return search_term, minimum_rating


def search_shows(search_term):
    """Call the TVMaze search API and return the decoded JSON list."""
    query = urllib.parse.urlencode({"q": search_term})
    with urllib.request.urlopen(f"{API_URL}?{query}", timeout=10) as response:
        return json.load(response)


def parse_show(result):
    """Convert one search result from the JSON into a Show object.

    Each result looks like {"score": ..., "show": {...}}. The show details
    are under "show", and "rating" may hold {"average": None}.
    """
    show_data = result["show"]
    rating_data = show_data.get("rating") or {}
    return Show(
        name=show_data["name"],
        genres=show_data.get("genres", []),
        rating=rating_data.get("average"),
    )


def filter_by_rating(shows, minimum_rating):
    """Keep only shows rated at or above minimum_rating.

    Shows with no rating are left out, because they can't meet the threshold.
    """
    return [
        show
        for show in shows
        if show.rating is not None and show.rating >= minimum_rating
    ]


def display_shows(shows):
    """Print the name, genre and rating of each show."""
    for show in shows:
        print(f"Show name: {show.name}")
        print(f"Genre    : {show.genre_text()}")
        print(f"Rating   : {show.rating_text()}")
        print("-" * 30)


def main():
    """Load the config, search TVMaze, and display the highly rated shows."""
    search_term, minimum_rating = load_config()
    if not search_term:
        print("config.json must include a non-empty search_term.")
        return

    try:
        results = search_shows(search_term)
    except (urllib.error.URLError, OSError) as error:
        print(f"Unable to reach the TVMaze API: {error}")
        return

    shows = [parse_show(result) for result in results]
    matching = filter_by_rating(shows, minimum_rating)
    if not matching:
        print(
            f"No shows found for '{search_term}' "
            f"with a rating of {minimum_rating:g} or higher."
        )
        return

    display_shows(matching)


if __name__ == "__main__":
    main()
