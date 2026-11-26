### 3.5. Module 5 solution

#### 3.5.1. Practical exercise: Externalise configuration

**Example config.json file:**

```json
{
    "search_term": "comedy",
    "minimum_rating": 8
}
```

**Example code solution:**

```python
def main():
    search_term = input("Enter a TV show search term: ").strip()
    if not search_term:
        print("Search term cannot be empty.")
        return
    results = get_tv_shows(search_term)
    display_show_details(results)


if __name__ == "__main__":
    main()
```

```python
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
```
