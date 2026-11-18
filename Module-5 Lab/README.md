# TVMaze Show Search

A small Python script that searches the [TVMaze](https://www.tvmaze.com/api) TV show database and displays the **show name**, **genre** and **rating** for each match.

It is the Module 5 lab: it calls a REST API, converts the JSON response into Python objects, and displays selected data.

---

## Features

- Searches TVMaze for any TV show title or keyword
- Converts each JSON result into a `Show` object (a Python dataclass)
- Shows "Unknown" when a show has no genres and "No rating" when it has no rating
- Handles an empty search term, no matches, and network errors with clear messages
- Uses only the Python standard library, so there is nothing to install

## Requirements

- Python 3.7 or newer
- An internet connection

## Usage

From this folder, run:

```bash
python3 tvmaze_search.py
```

Then type a search term when prompted:

```text
Enter a TV show search term: Sherlock
```

### Example output

Searching for `Sherlock` (first three results shown):

```text
Enter a TV show search term: Show name: Sherlock
Genre    : Drama, Crime, Mystery
Rating   : 8.9
------------------------------
Show name: Young Sherlock
Genre    : Action, Crime, Mystery
Rating   : 7.3
------------------------------
Show name: Miss Sherlock
Genre    : Drama, Crime, Mystery
Rating   : 7.3
------------------------------
...
```

The full output is in [`sample_output.txt`](sample_output.txt).

### Other messages

| You enter | Result |
|---|---|
| *(nothing)* | `A search term is required.` |
| A term with no matches | `No shows found for '<term>'.` |
| No internet, or the API is down | `Unable to reach the TVMaze API: <reason>` |

## How it works

| Step | Function | What it does |
|---|---|---|
| 1 | `main()` | Reads the search term and checks it is not empty. |
| 2 | `search_shows()` | Calls `https://api.tvmaze.com/search/shows?q=<term>` and decodes the JSON. |
| 3 | `parse_show()` | Converts each result into a `Show` object with `name`, `genres` and `rating`. |
| 4 | `display_shows()` | Prints the name, genre and rating of each show. |

The `Show` class is a dataclass with two display helpers, `genre_text()` and `rating_text()`, so formatting stays out of the rest of the code.

## Files

| File | Purpose |
|---|---|
| `tvmaze_search.py` | The script. |
| `sample_output.txt` | Output from a real search for "Sherlock". |
| `json_structure.md` | Explanation of the TVMaze JSON response and how the script reads it. |
| `README.md` | This file. |

## Notes and limitations

- **Needs the internet.** The script calls the live TVMaze API every time it runs. There is no offline mode or cache.
- **Ratings are often missing.** Many shows have no average rating, so they display "No rating".
- **Results are not filtered.** The script shows every match TVMaze returns. The Module 6 lab adds a minimum-rating filter and configuration file.
- **Search results can include duplicates.** TVMaze returns separate entries for shows with the same title, such as the several "Sherlock Holmes" entries.
- **No API key is needed.** TVMaze's search endpoint is public, but please keep request volumes reasonable.
