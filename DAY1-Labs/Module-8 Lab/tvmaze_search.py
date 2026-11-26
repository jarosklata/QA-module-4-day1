"""
TVMaze show search (Module 8 Lab).

Reads the search term and minimum rating from config.json, calls the TVMaze
search API, and displays the shows that meet the minimum rating. Progress and
errors are written to automation.log in the same folder as this script.

Usage:
    python3 tvmaze_search.py                    # uses config.json next to the script
    python3 tvmaze_search.py path/to/other.json # uses another config file

Uses only the Python standard library, so no packages need installing.
"""

import json
import logging
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

API_URL = "https://api.tvmaze.com/search/shows"
SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = SCRIPT_DIR / "config.json"
LOG_PATH = SCRIPT_DIR / "automation.log"

logger = logging.getLogger("tvmaze_search")


class ConfigError(Exception):
    """Raised when config.json is missing or contains unusable settings."""


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


def configure_logging(log_path=LOG_PATH):
    """Send log messages to automation.log, with a timestamp and level."""
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def load_config(path=CONFIG_PATH):
    """Read search_term and minimum_rating from the config file.

    Returns a (search_term, minimum_rating) tuple. Raises ConfigError if the
    file is missing, is not valid JSON, or lacks a usable setting.
    """
    try:
        with open(path, encoding="utf-8") as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        raise ConfigError(
            f"Configuration file not found: {path}\n"
            "Create config.json in the same folder as this script."
        )
    except json.JSONDecodeError as error:
        raise ConfigError(f"config.json is not valid JSON: {error}")

    try:
        search_term = str(config["search_term"]).strip()
        minimum_rating = float(config["minimum_rating"])
    except KeyError as error:
        raise ConfigError(f"config.json is missing the {error} setting.")
    except (TypeError, ValueError):
        raise ConfigError("config.json: minimum_rating must be a number.")

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
    """Load the config, search TVMaze, display and log the results."""
    configure_logging()
    logger.info("Automation started.")

    config_path = Path(sys.argv[1]) if len(sys.argv) > 1 else CONFIG_PATH
    try:
        search_term, minimum_rating = load_config(config_path)
    except ConfigError as error:
        logger.error("Configuration error: %s", error)
        print(f"Configuration error: {error}")
        return
    logger.info(
        "Loaded config from %s: search_term='%s', minimum_rating=%g",
        config_path, search_term, minimum_rating,
    )

    if not search_term:
        logger.error("Search term is empty in config; no search was made.")
        print("config.json must include a non-empty search_term.")
        return

    logger.info("Searching TVMaze for '%s'.", search_term)
    try:
        results = search_shows(search_term)
    except (urllib.error.URLError, OSError) as error:
        logger.error("TVMaze API request failed for '%s': %s", search_term, error)
        print(f"Unable to reach the TVMaze API: {error}")
        return

    try:
        shows = [parse_show(result) for result in results]
    except (KeyError, TypeError) as error:
        logger.error("Unexpected data in TVMaze response: %s", error)
        print("TVMaze returned data in an unexpected format.")
        return

    matching = filter_by_rating(shows, minimum_rating)
    logger.info(
        "TVMaze returned %d shows; %d met the minimum rating of %g.",
        len(shows), len(matching), minimum_rating,
    )

    if not matching:
        print(
            f"No shows found for '{search_term}' "
            f"with a rating of {minimum_rating:g} or higher."
        )
    else:
        display_shows(matching)

    logger.info("Automation completed.")


if __name__ == "__main__":
    main()
