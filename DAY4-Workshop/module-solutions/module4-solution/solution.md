### 3.4. Module 4 solution

#### 3.4.1. Practical exercise: Retrieve TV show data

**Example CoPilot prompt**

- Create a Python script that calls the TVMaze API, searches for TV shows, converts the JSON response into Python objects, and displays the show name, genre and rating for each result.

**What learners should have achieved**

- Call a REST API
- Convert JSON in Python objects
- Display selected data
- Use AI to understand unfamiliar JSON

**Example Python solution**

```python
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
```

**Example AI prompt to explain JSON**

Explain the JSON structure returned by the TVMaze search API. Show me how to access the show name, genres, and rating in Python.
