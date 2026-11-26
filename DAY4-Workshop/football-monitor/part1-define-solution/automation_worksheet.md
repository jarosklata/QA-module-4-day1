# Automation Definition Worksheet: Football Match Monitor

> **DRAFT.** Filled in from the workshop scenario in the exercise guide. Items marked **TBC** need a decision.

**Scenario:** A sports media team regularly checks football fixtures and results from different leagues. They want an automation that retrieves match information from an online service, applies simple business rules, and produces a report that other systems can use.

---

## 1. What is the problem?

Someone checks fixtures and results by hand, league by league. This is slow, and the report depends on who makes it. **TBC:** how often the check happens and who uses the report.

## 2. What are the inputs?

- **League**, as an ESPN league code such as `sco.1` (Scottish Premiership) or `eng.1` (English Premier League).
- **Team filter**, the name of the team to report on, such as `Celtic`.
- **Output file**, the name of the report file, such as `football_report.txt`.
- **Match data** from the ESPN Football API:
  `https://site.api.espn.com/apis/site/v2/sports/soccer/<league>/scoreboard`

The three settings come from `config.json`, so they can change without editing the code.

## 3. What processing is required?

1. Read the settings from `config.json`.
2. Call the ESPN API for the chosen league.
3. Extract each match: home team, away team, status and score.
4. Apply the business rules to filter the matches.
5. Create the report.
6. Record what happened in the log.

## 4. What are the outputs?

- **Match report** (`football_report.txt`), with one line per match, for example `Celtic 2 - 1 Rangers`, then `Status: Final`.
- **Log file** (`automation.log`), recording the start, the league, the number of matches processed, the file created, and any errors.

## 5. What are the business rules?

Choose at least one (**TBC** which ones):

- [ ] Only show matches involving the selected team.
- [ ] Only show completed matches.
- [ ] Only show matches scheduled today.
- [ ] Our own rule: **TBC**

## 6. Is the task suitable for automation?

**Yes.** It repeats, the data comes in a fixed JSON structure, and the rules are clear. **TBC:** what still needs a person, such as judging unusual match statuses.

## 7. What could go wrong?

| Risk | What the automation should do |
|---|---|
| No internet, or the API is down | Log the error and stop with a clear message. |
| The team name isn't found | Report that no matches were found, and log it. |
| `config.json` is missing or invalid | Stop with a clear message and log it. |
| The API only returns the current matchday, so there may be no completed matches | **TBC:** whether to add a date to the request. |

---

## Discussion

**Which parts are repeatable?**
**TBC**

**Which parts require human judgement?**
**TBC**

**Would Power Automate or Python be more appropriate?**
**TBC**
