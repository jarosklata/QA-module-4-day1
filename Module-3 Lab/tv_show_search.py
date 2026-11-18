"""
TV show search automation (Module 3 Lab).

Asks the user for a search term, simulates retrieving data,
and displays a summary of the search.
"""


def display_welcome():
    """Print the welcome banner."""
    print("=" * 40)
    print("Welcome to the TV Show Search Automation")
    print("=" * 40)


def get_search_term():
    """Ask the user for a search term and return it without surrounding spaces."""
    return input("Enter a TV show search term: ").strip()


def retrieve_data(search_term):
    """Simulate retrieving data for the search term.

    No real service is called in this module, so a fixed result count is returned.
    """
    print(f"\nSearching for '{search_term}'...")
    print("Retrieving data from service...")
    return 5


def display_summary(search_term, result_count):
    """Print a summary of the search."""
    print("\nSearch Summary")
    print("-" * 30)
    print(f"{'Search term':<14}: {search_term}")
    print(f"{'Results found':<14}: {result_count}")


def main():
    """Run the search: welcome, ask for a term, retrieve data, show a summary."""
    display_welcome()

    search_term = get_search_term()
    if not search_term:
        print("A search term is required.")
        return

    result_count = retrieve_data(search_term)
    display_summary(search_term, result_count)


if __name__ == "__main__":
    main()
