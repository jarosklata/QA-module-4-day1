def retrieve_data(search_term):
    print(f"Searching for '{search_term}'...")
    print("Retrieving data...")
    return 5


def main():
    print("TV Show Search Automation")
    print("-" * 30)
    search_term = input("Enter a search term: ")
    results = retrieve_data(search_term)
    print()
    print("Summary")
    print(f"Search term: {search_term}")
    print(f"Results found: {results}")


if __name__ == "__main__":
    main()
