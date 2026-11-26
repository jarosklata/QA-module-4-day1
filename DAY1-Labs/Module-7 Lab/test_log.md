# Test Log: TVMaze Automation (Module 6 script)

**Script tested:** `Module-6 Lab/tvmaze_search.py`
**Config for the tests:** a scratch copy of the script, with a different `config.json` for each case. The real `config.json` was not changed.

| # | Test | Config input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Valid search term | `search_term`: "Breaking Bad", `minimum_rating`: 8 | Matching show(s) displayed with name, genre and rating | Shows "Breaking Bad", genre "Drama, Crime, Thriller", rating 9.2 | **Pass** |
| 2 | Invalid search term | `search_term`: "zzqxjwkvbq", `minimum_rating`: 8 | Message that no shows were found | "No shows found for 'zzqxjwkvbq' with a rating of 8 or higher." | **Pass** |
| 3 | Empty search term | `search_term`: "", `minimum_rating`: 8 | Script rejects the input with a message | "config.json must include a non-empty search_term." No search is made | **Pass** |
| 4 | High rating threshold | `search_term`: "Breaking Bad", `minimum_rating`: 10 | No shows displayed, with a message | "No shows found for 'Breaking Bad' with a rating of 10 or higher." | **Pass** |
| 5 | Missing configuration file | No `config.json` in the script's folder | Helpful error message, no traceback | "Configuration file not found: .../config.json. Create config.json in the same folder as this script." | **Pass** |

## Summary

All five required tests passed. No code changes were needed.

## Notes

- Test 1 uses "Breaking Bad" rather than "comedy", because the "comedy" search returned no rated shows (see the Module 6 notes).
- The script doesn't check that `minimum_rating` is between 0 and 10. A value such as 15 gives "No shows found" rather than an error. This is not in the Module 7 test list, so it is recorded here for later.
- Network failure was not tested, because it needs the API to be unreachable. The script handles it with a message, but this log doesn't show that.
