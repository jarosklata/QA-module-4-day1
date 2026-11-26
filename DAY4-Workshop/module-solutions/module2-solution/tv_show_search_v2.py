"""
Simple TV show search automation.
"""


def retrieve_data(search_term):
    """Simulate retrieving data."""
    print(f"\nSearching for '{search_term}'...")
    print("Retrieving data from service...")
    return 5


def display_summary(search_term, result_count):
    """Display a summary of the search."""
    print("\nSearch Summary")
    print("-" * 30)
    print(f"Search term : {search_term}")
    print(f"Results found: {result_count}")


def main():
    print("TV Show Search Automation")
    print("=" * 30)
    search_term = input("Enter a search term: ").strip()
    if not search_term:
        print("A search term is required.")
        return
    result_count = retrieve_data(search_term)
    display_summary(search_term, result_count)


if __name__ == "__main__":
    main()
