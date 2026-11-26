"""
TVMaze show search (Module 5 Lab).

Calls the TVMaze search API, converts each JSON result into a Show object,
and displays the show name, genre and rating.

Uses only the Python standard library, so no packages need installing.
"""

import json
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import List, Optional

API_URL = "https://api.tvmaze.com/search/shows"


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


def display_shows(shows):
    """Print the name, genre and rating of each show."""
    for show in shows:
        print(f"Show name: {show.name}")
        print(f"Genre    : {show.genre_text()}")
        print(f"Rating   : {show.rating_text()}")
        print("-" * 30)


def main():
    """Ask for a search term, call the API, and display the results."""
    search_term = input("Enter a TV show search term: ").strip()
    if not search_term:
        print("A search term is required.")
        return

    try:
        results = search_shows(search_term)
    except (urllib.error.URLError, OSError) as error:
        print(f"Unable to reach the TVMaze API: {error}")
        return

    shows = [parse_show(result) for result in results]
    if not shows:
        print(f"No shows found for '{search_term}'.")
        return

    display_shows(shows)


if __name__ == "__main__":
    main()
