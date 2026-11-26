"""
Catalogue of the Module 1-8 lab files shown on the Modules page.

Only the files listed here can be read through the web server. Paths are
relative to the repository root.
"""

MODULES = [
    {
        "number": 1,
        "title": "Tools walkthrough",
        "topic": "Planning an automation with a worksheet.",
        "files": [
            {"path": "DAY1-Labs/Module-1 Lab/automation_planning_worksheet.md", "label": "Automation planning worksheet"},
        ],
    },
    {
        "number": 2,
        "title": "Define an automation solution",
        "topic": "Describing a customer enquiries automation: problem, inputs, processing and outputs.",
        "files": [
            {"path": "DAY1-Labs/Module-2 Lab/instrcutions.md", "label": "Lab brief"},
            {"path": "DAY1-Labs/Module-2 Lab/automation_worksheet.md", "label": "Automation worksheet"},
        ],
    },
    {
        "number": 3,
        "title": "Generate your first script",
        "topic": "A search script written with AI assistance.",
        "files": [
            {"path": "DAY1-Labs/Module-3 Lab/tv_show_search.py", "label": "Search script"},
        ],
    },
    {
        "number": 4,
        "title": "Improve AI-generated code",
        "topic": "Refactoring the AI-generated search script for people to read.",
        "files": [
            {"path": "DAY1-Labs/Module-4 Lab/improved_search.py", "label": "Improved search script"},
        ],
    },
    {
        "number": 5,
        "title": "Retrieve TV show data",
        "topic": "Calling the TVMaze API and showing the results.",
        "files": [
            {"path": "DAY1-Labs/Module-5 Lab/tvmaze_search.py", "label": "TVMaze script"},
            {"path": "DAY1-Labs/Module-5 Lab/README.md", "label": "README"},
            {"path": "DAY1-Labs/Module-5 Lab/json_structure.md", "label": "JSON structure"},
            {"path": "DAY1-Labs/Module-5 Lab/sample_output.txt", "label": "Sample output"},
        ],
    },
    {
        "number": 6,
        "title": "Externalise configuration",
        "topic": "Moving the search term and minimum rating into config.json.",
        "files": [
            {"path": "DAY1-Labs/Module-6 Lab/tvmaze_search.py", "label": "TVMaze script"},
            {"path": "DAY1-Labs/Module-6 Lab/config.json", "label": "Configuration"},
        ],
    },
    {
        "number": 7,
        "title": "Test and break the automation",
        "topic": "Testing valid, invalid, empty and missing-config cases.",
        "files": [
            {"path": "DAY1-Labs/Module-7 Lab/test_log.md", "label": "Test log"},
        ],
    },
    {
        "number": 8,
        "title": "Prepare for workplace use",
        "topic": "Adding logging, error logging and documentation.",
        "files": [
            {"path": "DAY1-Labs/Module-8 Lab/tvmaze_search.py", "label": "Script with logging"},
            {"path": "DAY1-Labs/Module-8 Lab/config.json", "label": "Configuration"},
            {"path": "DAY1-Labs/Module-8 Lab/automation.log", "label": "Log file"},
            {"path": "DAY1-Labs/Module-8 Lab/README.md", "label": "README"},
        ],
    },
]

# The module solutions from the exercise guide, section 3. The numbering follows
# the guide: its "Module 1 solution" answers the guide's Module 2 lab, and so on.
_SOLUTIONS_DIR = "DAY4-Workshop/module-solutions"


def _solution(number, title, topic, files):
    folder = f"{_SOLUTIONS_DIR}/module{number}-solution"
    return {
        "number": number,
        "title": title,
        "topic": topic,
        "files": [{"path": f"{folder}/{name}", "label": label} for name, label in files],
    }


SOLUTIONS = [
    _solution(1, "Define an automation solution", "The completed automation planning worksheet.", [
        ("solution.md", "Solution"),
    ]),
    _solution(2, "Generate your first automation script", "Two prompts and the scripts they produce.", [
        ("solution.md", "Solution"),
        ("tv_show_search_v1.py", "Script from prompt 1"),
        ("tv_show_search_v2.py", "Improved script (prompt 2)"),
    ]),
    _solution(3, "Improve AI-generated code", "A hard-to-maintain script, and a cleaner version.", [
        ("solution.md", "Solution"),
        ("original_script.py", "Original script"),
        ("improved_script.py", "Improved script"),
    ]),
    _solution(4, "Retrieve TV show data", "Calling the TVMaze API and showing name, genres and rating.", [
        ("solution.md", "Solution"),
        ("tvmaze_search.py", "TVMaze script"),
    ]),
    _solution(5, "Externalise configuration", "Reading the search term and minimum rating from config.json.", [
        ("solution.md", "Solution"),
        ("tvmaze_search.py", "TVMaze script"),
        ("config.json", "Configuration"),
    ]),
    _solution(6, "Test and break the automation", "A test table, the problems it found, and the improved script.", [
        ("solution.md", "Solution"),
        ("tvmaze_search.py", "Improved script"),
        ("config.json", "Configuration"),
    ]),
    _solution(7, "Prepare for workplace use", "Adding logging and a report file.", [
        ("solution.md", "Solution"),
        ("tvmaze_search.py", "Script with logging"),
        ("config.json", "Configuration"),
    ]),
]


def allowed_paths():
    """Return the set of file paths the server may read."""
    return {
        item["path"]
        for group in (MODULES, SOLUTIONS)
        for module in group
        for item in module["files"]
    }
