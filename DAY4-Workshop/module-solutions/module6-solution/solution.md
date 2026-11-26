### 3.6. Module 6 solution

#### 3.6.1. Practical exercise: Test and break the automation

> **Note:** Depending on the AI Code initially generated, you may get different results from below.

| Test | Expected Result | Actual Result | Result |
|---|---|---|---|
| Valid search term | API returns matching shows | Shows returned successfully | **Pass** |
| Invalid search term | No matching results displayed | No results displayed | **Pass** |
| Empty search term | Script rejects the input | Script continued with blank search | **Fail** |
| High rating threshold | No shows meet the threshold | No shows displayed | **Pass** |
| Missing config.json | Helpful error message displayed | FileNotFoundError traceback displayed | **Fail** |

**Issues identified:**

- Blank search terms are not validated.
- A missing configuration file causes the script to stop with a traceback.
- The user is not told when no matching shows are found.
- API connection failures are not handled.
- File creation errors are not handled.

**Example Copilot prompts:**

- Suggest normal, boundary and invalid test cases for this TVMaze automation
- Review this script and identify any missing input validation or error handling
- Explain this error message and suggest a safe fix

**Original main() (before fixes)**

```python
def main():
    config = load_config("config.json")
    search_term = config["search_term"]
    minimum_rating = config["minimum_rating"]
    results = get_tv_shows(search_term)
    display_filtered_shows(results, minimum_rating)


if __name__ == "__main__":
    main()
```

**Example improved solution:**

```python
import json
import requests


def load_config(config_file):
    """Load and validate configuration settings."""
    try:
        with open(config_file) as file:
            config = json.load(file)
    except FileNotFoundError:
        print(f"Configuration file not found: {config_file}")
        return None
    except json.JSONDecodeError:
        print("The configuration file contains invalid JSON.")
        return None

    search_term = config.get("search_term", "").strip()
    minimum_rating = config.get("minimum_rating")

    if not search_term:
        print("Search term cannot be empty.")
        return None

    if not isinstance(minimum_rating, (int, float)):
        print("Minimum rating must be a number.")
        return None

    if minimum_rating < 0 or minimum_rating > 10:
        print("Minimum rating must be between 0 and 10.")
        return None

    return config


def get_tv_shows(search_term):
    """Retrieve TV show data from the TVMaze API."""
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Unable to retrieve TV show data: {error}")
        return []

    return response.json()


def filter_shows(results, minimum_rating):
    """Return shows that meet the minimum rating."""
    matching_shows = []

    for result in results:
        show = result["show"]
        rating = show["rating"]["average"]
        if rating is not None and rating >= minimum_rating:
            matching_shows.append(show)

    return matching_shows


def save_results(shows, output_file):
    """Save matching show names to an output file."""
    try:
        with open(output_file, "w") as file:
            for show in shows:
                file.write(f"{show['name']} - Rating: "
                           f"{show['rating']['average']}\n")
    except OSError as error:
        print(f"Unable to create output file: {error}")
        return False

    return True


def main():
    config = load_config("config.json")

    if config is None:
        return

    search_term = config["search_term"]
    minimum_rating = config["minimum_rating"]
    output_file = config.get("output_file", "results.txt")

    results = get_tv_shows(search_term)

    if not results:
        print("No results were returned.")
        return

    matching_shows = filter_shows(results, minimum_rating)

    if not matching_shows:
        print("No shows met the minimum rating.")
        return

    if save_results(matching_shows, output_file):
        print(f"{len(matching_shows)} matching shows saved to {output_file}")


if __name__ == "__main__":
    main()
```

**Expected learning points:**

- Testing should include successful, unusual, and invalid scenarios.
- Expected and actual results should be compared.
- Failed tests identify improvements rather than simply proving the scripts is broken.
- Input, API, and file errors should be handled separately.
- After changes are made, the failed tests should be repeated.
- AI can suggest test cases and explain errors, **but learners must verify the fixes!**
