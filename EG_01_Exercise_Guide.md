# AI Assisted Scripting — Low-code Pathway — Exercise Guide

## Contents

1. Module Labs
   1.1. Module 1 Lab
   1.2. Module 2 Lab
   1.3. Module 3 Lab
   1.4. Module 4 Lab
   1.5. Module 5 Lab
   1.6. Module 6 Lab
   1.7. Module 7 Lab
   1.8. Module 8 Lab
2. Workshop
   2.1. Build a football match monitor automation
   2.2. Workshop Part 1 — Define the solution
   2.3. Workshop Part 2 — Use AI to generate a starting script
   2.4. Workshop Part 3 — Process match data
   2.5. Workshop Part 4 — Add business rules
   2.6. Workshop Part 5 — Add configuration
   2.7. Workshop Part 6 — Test and validate
   2.8. Workshop Part 7 — Add logging
   2.9. Workshop Part 8 — Create documentation
   2.10. Final deliverables
3. Module solutions
   3.1. Module 1 solution
   3.2. Module 2 solution
   3.3. Module 3 solution
   3.4. Module 4 solution
   3.5. Module 5 solution
   3.6. Module 6 solution
   3.7. Module 7 solution

---

## 1. Module Labs

### 1.1. Module 1 Lab

**Tasks**

Your trainer will introduce and walk through the tools discussed in the module.

There are no additional tasks for this module.

### 1.2. Module 2 Lab

#### 1.2.1. Practical exercise: Define an automation solution

**Scenario**

A team receives a CSV file containing customer enquiries each day and wants to automate the process of identifying high-priority enquiries.

**Tasks**

Complete an Automation Planning Worksheet:

- What is the problem?
- What are the inputs?
- What processing is required?
- What are the outputs?
- Is the task suitable for automation?

**Discussion**

- Which parts are repeatable?
- Which parts require human judgement?
- Would Power Automate or Python be more appropriate?

**Deliverable**

Completed automation worksheet (one page).

### 1.3. Module 3 Lab

#### 1.3.1. Practical exercise: Generate your first automation script

**Scenario**

- Generate a Python script that:
- Asks for a search term
- Displays a welcome message
- Simulates retrieving data
- Displays a summary

**Tasks**

Use Copilot to:

- Generate the script
- Explain the code
- Improve the prompt
- Improve the generated code

**Deliverable**

Working Python script.

Example prompts used during development.

### 1.4. Module 4 Lab

#### 1.4.1. Practical exercise: Improve AI-generated code

**Scenario**

You have received an AI-generated script that works but is difficult to maintain.

```python
a = input("Enter a search term: ")
print(f"Searching for {a}")
data = ["Doctor Who", "Sherlock", "Luther"]
for s in data:
    print(s)
print("Done")
```

**Tasks**

Identify:

- Poor variable names
- Missing comments
- Missing functions
- Opportunities to improve readability

Refactor the script.

**Deliverable**

Improved version of the script.

### 1.5. Module 5 Lab

#### 1.5.1. Practical exercise: Retrieve TV show data

**Scenario**

Use the TVMaze API to retrieve information about television programmes.

**Tasks**

- Call the API
- Convert JSON into Python objects
- Display:
  - Show name
  - Genre
  - Rating
- Use AI to explain the JSON structure

**Deliverable**

Working API script and sample output.

### 1.6. Module 6 Lab

#### 1.6.1. Practical exercise: Externalise configuration

**Scenario**

The TVMaze automation should support different search terms and rating thresholds.

**Tasks**

Create the following configuration file:

```json
{
    "search_term": "comedy",
    "minimum_rating": 8
}
```

Update the script to:

- Load the configuration
- Use the configuration values
- Run without code changes

**Deliverable**

Working config.json and updated script.

### 1.7. Module 7 Lab

#### 1.7.1. Practical exercise: Test and break the automation

**Scenario**

The TVMaze automation works correctly.

Your task is to prove it.

**Tasks**

Test:

- Valid search term
- Invalid search term
- Empty search term
- High rating threshold
- Missing configuration file

Record:

- Expected result
- Actual result
- Pass/Fail

**Deliverable**

Completed test log.

### 1.8. Module 8 Lab

#### 1.8.1. Practical exercise: Prepare for workplace use

**Scenario**

Your TVMaze automation is ready for deployment.

**Tasks**

Add:

- Logging
- Error logging
- Documentation

Create:

- automation.log
- README.md
- Use AI to assist with documentation.

**Deliverable**

- Log file
- README document
- Evidence that an error was logged successfully.

---

## 2. Workshop

### 2.1. Build a football match monitor automation

#### 2.1.1. Workshop overview

A sports media team regularly monitor football fixtures and results from different leagues. The team would like an automation solution that retrieves match information from an online service, applies simple business rules, and produces a report that can be shared with other systems.

In this workshop, you will build a complete automation solution using the skills developed throughout the course. You will use AI tools to assist development, retrieve football data from an API, configure the automation, test the solution, add logging, and prepare it for workplace use.

#### 2.1.2. Learning outcomes

By completing this workshop, you will be able to:

- Define an automation solution
- Use AI to generate and improve code
- Retrieve data from an API
- Process JSON data
- Apply business rules
- Use configuration files
- Test and validate automation
- Add logging and monitoring information
- Create workplace documentation

#### 2.1.3. Scenario

You have been asked to create a Football Match Monitor.

The automation should:

- Connect to the ESPN Football API
- Retrieve fixture and result information
- Filter information according to user requirements
- Create an output report
- Record activity in a log file
- Be configurable without changing code

#### 2.1.4. API Endpoint

Learners may choose either:

**Scottish Premiership**

https://site.api.espn.com/apis/site/v2/sports/soccer/**sco.1**/scoreboard

**English Premier League**

https://site.api.espn.com/apis/site/v2/sports/soccer/**eng.1**/scoreboard

Or the learner can choose by using the first three characters of the country name, for example, **fra.1** for the French Ligue 1 and **ger.1** for the German Bundesliga.

### 2.2. Workshop Part 1 — Define the solution

Complete an Automation Definition Worksheet.

**Inputs**

- League
- Team filter
- Output file

**Processing**

- Call API
- Extract match data
- Apply filters
- Create report

**Outputs**

- Match report
- Log file

**Business Rules**

Examples:

- Only show matches involving a specific team
- Only show completed matches
- Only show fixtures scheduled today

### 2.3. Workshop Part 2 — Use AI to generate a starting script

Use Copilot to generate code that:

- Calls the ESPN API
- Retrieves JSON data
- Displays basic match information

**Review**

Can you explain:

- The API URL?
- The requests library?
- The JSON response?
- The generated code?
- What prompt improvements could produce better code?

### 2.4. Workshop Part 3 — Process match data

**Extract**:

- Home team
- Away team
- Match status
- Score

Display the information in a readable format.

**Example**:

- Celtic 2 - 1 Rangers
- Status: Final

### 2.5. Workshop Part 4 — Add business rules

Choose at least one:

**Option A**

- Only display matches involving a selected team.

**Option B**

- Only display completed matches.

**Option C**

- Only display scheduled matches.

**Option D**

- Create your own rule.

### 2.6. Workshop Part 5 — Add configuration

Create the following json configuration file:

```json
{
    "league": "sco.1",
    "team_filter": "Celtic",
    "output_file": "football_report.txt"
}
```

Update the script so that settings are read from the configuration file.

### 2.7. Workshop Part 6 — Test and validate

**Test:**

- Scottish league
- English league
- Valid team
- Invalid team
- Missing configuration file

**Record:**

| Test | Pass/Fail |
|---|---|
| API returned data | |
| Report created | |
| Team filter worked | |
| Configuration loaded | |

### 2.8. Workshop Part 7 — Add logging

**Record:**

- Script started
- League selected
- Number of matches processed
- Output file created
- Errors encountered

**Create:**

- automation.log

### 2.9. Workshop Part 8 — Create documentation

Use AI to assist with documentation.

**Document:**

- Purpose
- Configuration settings
- Dependencies
- Inputs
- Outputs
- Known limitations

**Create:**

- README.md

### 2.10. Final deliverables

At the end of the workshop, you should have:

| Test | File | Confirm (y/n) |
|---|---|---|
| Main automation script | football_monitor.py | |
| Configuration Settings | config.json | |
| Generated report | football_report.txt | |
| Execution log | automation.log | |
| Test results | test_results.txt | |
| Support documentation | README.md | |

#### 2.10.1. Workshop success criteria

Your automation should:

- ✓ Retrieve football data from the ESPN API
- ✓ Apply at least one business rule
- ✓ Use a configuration file
- ✓ Generate an output report
- ✓ Record activity in a log file
- ✓ Be tested and validated
- ✓ Include supporting documentation

**Workshop takeaway**

Build an automation that is not only **functional**, but **configurable**, **testable**, **supportable**, and **ready** for workplace use.

---

## 3. Module solutions

### 3.1. Module 1 solution

#### 3.1.1. Practical exercise: Define an automation solution

**Completed automation planning worksheet**

- **Problem:** Staff spend time manually reviewing customer enquiries.
- **Inputs:** CSV file containing enquiries.
- **Processing:**
  - Read file.
  - Identify priority = High.
  - Create summary.
- **Outputs:**
  - Summary report.
  - Email notification.
- **Suitable for automation?** Yes.
- **Approach:** Hybrid.
- **Reason:**
  - Python can process the CSV data.
  - Power Automate can distribute notifications.

### 3.2. Module 2 solution

#### 3.2.1. Practical exercise: Generate your first automation script

**Example Prompt 1**

Create a Python script that:

- Displays a welcome message
- Prompts the user for a TV show search term
- Simulates retrieving data from an online service
- Displays a summary message showing the search term
- Uses a main() function

**Example generated script**

```python
def retrieve_data(search_term):
    print(f"Searching for '{search_term}'...")
    print("Retrieving data...")
    return 5


def main():
    print("TV Show Search Automation")
    print("-" * 30)
    search_term = input("Enter a search term: ")
    results = retrieve_data(search_term)
    print()
    print("Summary")
    print(f"Search term: {search_term}")
    print(f"Results found: {results}")


if __name__ == "__main__":
    main()
```

**Example Prompt 2 (improved prompt)**

Improve the previous script by:

- Adding functions
- Using clear variable names
- Displaying a more professional summary
- Adding comments explaining the code
- Handling empty user input

```python
"""
Simple TV show search automation.
"""


def retrieve_data(search_term):
    """Simulate retrieving data."""
    print(f"\nSearching for '{search_term}'...")
    print("Retrieving data from service...")
    return 5


def display_summary(search_term, result_count):
    """Display a summary of the search."""
    print("\nSearch Summary")
    print("-" * 30)
    print(f"Search term : {search_term}")
    print(f"Results found: {result_count}")


def main():
    print("TV Show Search Automation")
    print("=" * 30)
    search_term = input("Enter a search term: ").strip()
    if not search_term:
        print("A search term is required.")
        return
    result_count = retrieve_data(search_term)
    display_summary(search_term, result_count)


if __name__ == "__main__":
    main()
```

### 3.3. Module 3 solution

#### 3.3.1. Practical exercise: Improve AI-generated code

**Scenario**

You have received an AI-generated script that works but is difficult to maintain.

```python
a = input("Enter a search term: ")
print(f"Searching for {a}")
data = ["Doctor Who", "Sherlock", "Luther"]
for s in data:
    print(s)
print("Done")
```

**Problems:**

- Variable name a, data and s are not meaningful
- No functions
- No comments or docstrings
- No validation
- No clear program structure

**Example improved solution**

```python
""" Simple TV show search demonstration. """


def get_search_term():
    """Prompt the user for a search term."""
    return input("Enter a search term: ").strip()


def display_results(show_list):
    """Display the matching shows."""
    print("\nResults")
    print("-" * 20)
    for show in show_list:
        print(show)


def main():
    search_term = get_search_term()
    if not search_term:
        print("A search term is required.")
        return
    print(f"\nSearching for '{search_term}'...")
    shows = [ "Doctor Who", "Sherlock", "Luther" ]
    display_results(shows)
    print("\nSearch completed.")


if __name__ == "__main__":
    main()
```

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

### 3.7. Module 7 solution

#### 3.7.1. Practical exercise: Prepare for workplace use

**Example solution code:**

```python
import json
import logging
import requests

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_config(config_file):
    """Load configuration settings."""
    with open(config_file) as file:
        return json.load(file)


def get_tv_shows(search_term):
    """Retrieve TV show information from the TVMaze API."""
    logging.info("Searching for '%s'", search_term)
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def save_report(results, minimum_rating, report_file):
    """Save matching shows to a report file."""
    with open(report_file, "w") as file:
        file.write("TV Show Report\n")
        file.write("=" * 40 + "\n\n")

        count = 0
        for result in results:
            show = result["show"]
            rating = show["rating"]["average"]

            if rating is not None and rating >= minimum_rating:
                genres = ", ".join(show["genres"])
                file.write(f"Name   : {show['name']}\n")
                file.write(f"Genres : {genres}\n")
                file.write(f"Rating : {rating}\n")
                file.write("-" * 40 + "\n")
                count += 1

    logging.info("%s shows written to report.", count)


def main():
    logging.info("Automation started.")
    config = load_config("config.json")
    results = get_tv_shows(config["search_term"])
    save_report(
        results,
        config["minimum_rating"],
        "tv_report.txt"
    )
    logging.info("Automation completed successfully.")


if __name__ == "__main__":
    main()
```
