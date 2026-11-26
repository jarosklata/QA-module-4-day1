# Football Match Monitor

A small Python script that gets football fixtures and results from the ESPN Football API, keeps the matches involving a chosen team, and writes a text report. Settings are read from a config file, so they can change without editing the code.

## Purpose

A sports media team checks fixtures and results from several leagues. This script does the check the same way every time and produces a report that can be shared with other systems. It also keeps a log of what it did.

## How to run

```
python3 football_monitor.py
```

To use a different config file:

```
python3 football_monitor.py path/to/other_config.json
```

The script prints the report, saves it next to the script, and exits with `0` if it worked or `1` if something went wrong.

## Configuration settings

Settings are in `config.json`, next to the script.

| Setting | Required | Meaning |
|---|---|---|
| `league` | Yes | ESPN league code, such as `sco.1` (Scottish Premiership) or `eng.1` (English Premier League). Other leagues use the first three letters of the country, for example `fra.1` or `ger.1`. |
| `team_filter` | No | Only keep matches where the home or away team name contains this text, ignoring upper and lower case. Leave it as `""` to keep every match. |
| `output_file` | Yes | Name of the report file, saved next to the script. |
| `date` | No | A date in the form `YYYYMMDD`. Without it the API returns the current matchday. |

Example:

```json
{
    "league": "sco.1",
    "team_filter": "Celtic",
    "output_file": "football_report.txt"
}
```

## Dependencies

- Python 3.9 or later.
- Nothing to install. The script uses only the Python standard library.
- An internet connection, to reach the ESPN API.

## Inputs

- `config.json`, described above.
- Match data from `https://site.api.espn.com/apis/site/v2/sports/soccer/<league>/scoreboard`.

## Outputs

- **Report** (`football_report.txt` by default): the league, team filter, date, and number of matches, then one entry per match, for example:

  ```
  Celtic 4 - 1 St Mirren
  Status: Full Time
  ```

  Matches that haven't started show `Celtic v St Mirren` and a status such as `Scheduled - Sat 28 Nov 15:00 UTC`.
- **Log** (`automation.log`): the start, the settings loaded, the league selected, the number of matches processed, the output file created, and any warnings or errors. Each run adds to the end of the log.

## Testing

`test_results.txt` records the tests run against this version: Scottish and English leagues, a valid and an invalid team, a missing config file, and some other bad configs. The tests use the live API, so match counts depend on the day.

## Known limitations

- **Current matchday only.** Without a `date`, the API shows only the matches for the current matchday. A team that isn't playing then gives a report with no matches. This is why the example config (`Celtic`) often returns nothing.
- **Team names are matched as text.** `United` matches every team with United in its name. A misspelt team name gives no matches, not an error.
- **Times are in UTC.**
- **Needs the ESPN API.** If the API is down, or ESPN changes the shape of its data, the script logs an error and stops. Matches that don't have the expected data are skipped and logged.
- **The log grows.** Nothing deletes old entries.
- **One league per run.**
