"""
Simple TV show search demonstration (Module 4 Lab, improved version).

Asks the user for a search term and lists a sample set of shows.

Changes from the original AI-generated script:
- Meaningful names instead of a, data and s
- Functions for each step instead of top-level code
- Sample data kept in a named constant
- Comments and docstrings explaining each part
"""

# Sample data set used in place of a real search.
SAMPLE_SHOWS = ["Doctor Who", "Sherlock", "Luther"]


def get_search_term():
    """Ask the user for a search term and return it."""
    return input("Enter a search term: ")


def display_shows(shows):
    """Print each show on its own line."""
    for show in shows:
        print(show)


def main():
    """Run the search: read the term, report it, list the sample shows."""
    search_term = get_search_term()
    print(f"Searching for {search_term}")
    display_shows(SAMPLE_SHOWS)
    print("Done")


if __name__ == "__main__":
    main()
