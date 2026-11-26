""" Simple TV show search demonstration. """


def get_search_term():
    """Prompt the user for a search term."""
    return input("Enter a search term: ").strip()


def display_results(show_list):
    """Display the matching shows."""
    print("\nResults")
    print("-" * 20)
    for show in show_list:
        print(show)


def main():
    search_term = get_search_term()
    if not search_term:
        print("A search term is required.")
        return
    print(f"\nSearching for '{search_term}'...")
    shows = [ "Doctor Who", "Sherlock", "Luther" ]
    display_results(shows)
    print("\nSearch completed.")


if __name__ == "__main__":
    main()
