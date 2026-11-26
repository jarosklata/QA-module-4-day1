import json
import requests


def load_config(config_file):
    """Load settings from a JSON configuration file."""
    with open(config_file) as file:
        return json.load(file)


def get_tv_shows(search_term):
    """Call the TVMaze API and return search results."""
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    response = requests.get(url)

    if response.status_code != 200:
        print("API request failed")
        return []
    return response.json()


def display_filtered_shows(results, minimum_rating):
    """Display shows that meet the minimum rating."""
    for result in results:
        show = result["show"]
        name = show["name"]
        rating = show["rating"]["average"]

        if rating is not None and rating >= minimum_rating:
            print(f"{name} - Rating: {rating}")


# Added so the script can be run: it reads the search term and minimum rating
# from config.json. The guide's own main() (in solution.md) asks for the search
# term instead and doesn't use the config file.
def main():
    config = load_config("config.json")
    results = get_tv_shows(config["search_term"])
    display_filtered_shows(results, config["minimum_rating"])


if __name__ == "__main__":
    main()
