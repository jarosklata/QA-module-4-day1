import requests


def get_tv_shows(search_term):
    """Call the TVMaze API and return search results."""
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    response = requests.get(url)
    if response.status_code != 200:
        print("API request failed")
        return []
    return response.json()


def display_show_details(results):
    """Display show name, genres and rating."""
    for result in results:
        show = result["show"]
        name = show["name"]
        genres = ", ".join(show["genres"])
        rating = show["rating"]["average"]
        if rating is None:
            rating = "No rating"
        print(f"Show name: {name}")
        print(f"Genres: {genres}")
        print(f"Rating: {rating}")
        print("-" * 30)


# Added so the script can be run: the guide's solution stops after the two functions.
def main():
    search_term = input("Enter a TV show search term: ").strip()
    if not search_term:
        print("Search term cannot be empty.")
        return
    display_show_details(get_tv_shows(search_term))


if __name__ == "__main__":
    main()
