# TVMaze Show Search

A small Python script that searches the [TVMaze](https://www.tvmaze.com/api) API for TV shows and shows the ones rated at or above a minimum rating. The search term and rating are set in a config file, so you can change them without editing the code.

It writes a log file, `automation.log`, recording each run and any errors.

## Requirements

- Python 3.7 or newer
- An internet connection (the script calls the TVMaze API)
- No extra packages. The script uses only the Python standard library.

## Files

| File | Purpose |
|---|---|
| `tvmaze_search.py` | The script |
| `config.json` | Search term and minimum rating |
| `automation.log` | Log of runs and errors, created on first run |
| `README.md` | This document |

## Configuration

Edit `config.json`:

```json
{
    "search_term": "comedy",
    "minimum_rating": 8
}
```

| Setting | Meaning |
|---|---|
| `search_term` | Text to search for. Must not be blank. |
| `minimum_rating` | Only shows rated at or above this number are displayed. Must be a number. |

`config.json` must be in the same folder as the script.

## Running the script

```bash
cd "Module-8 Lab"
python3 tvmaze_search.py
```

To use a different config file, pass its path:

```bash
python3 tvmaze_search.py path/to/other.json
```

The script prints each matching show with its name, genre and rating. If none match, it says so.

## Logging

Each run appends to `automation.log`, with a timestamp and a level:

- **INFO:** the run started, the config loaded, the search made, the number of shows matched, and the run completed.
- **ERROR:** a problem stopped the run. Covered cases:
  - the config file is missing, is not valid JSON, or has a missing or invalid setting;
  - the search term is blank;
  - the TVMaze API can't be reached;
  - the API returns data in an unexpected format.

Example log entries from a missing config file and a blank search term:

```
2026-11-19 13:42:57,823 - INFO - Automation started.
2026-11-19 13:42:57,823 - ERROR - Configuration error: Configuration file not found: /tmp/m8_does_not_exist.json
2026-11-19 13:42:57,925 - INFO - Automation started.
2026-11-19 13:42:57,925 - INFO - Loaded config from /tmp/m8_empty.json: search_term='', minimum_rating=8
2026-11-19 13:42:57,925 - ERROR - Search term is empty in config; no search was made.
```

## Testing

The test cases and results are in [`Module-7 Lab/test_log.md`](../Module-7%20Lab/test_log.md). They cover a valid search, an invalid search, an empty search, a high rating threshold, and a missing config file. The tested script is the Module 6 version. This version adds logging and an optional config path, and the same behaviour applies.

## Known limitations

- **Search results are limited.** TVMaze returns about 10 matches per search, and the rating filter only applies to those. A broad term like `comedy` may return no rated shows, so nothing is displayed at a minimum rating of 8.
- **The rating range isn't checked.** A value outside 0 to 10 gives "No shows found" rather than an error.
- **Network failure isn't tested.** The error handling is in the code and logs an ERROR line, but it hasn't been triggered in testing.

## Documentation

This README was drafted with AI assistance and then checked by hand against the script's behaviour.
