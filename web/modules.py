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
            {"path": "Module-1 Lab/automation_planning_worksheet.md", "label": "Automation planning worksheet"},
        ],
    },
    {
        "number": 2,
        "title": "Define an automation solution",
        "topic": "Describing a customer enquiries automation: problem, inputs, processing and outputs.",
        "files": [
            {"path": "Module-2 Lab/instrcutions.md", "label": "Lab brief"},
            {"path": "Module-2 Lab/automation_worksheet.md", "label": "Automation worksheet"},
        ],
    },
    {
        "number": 3,
        "title": "Generate your first script",
        "topic": "A search script written with AI assistance.",
        "files": [
            {"path": "Module-3 Lab/tv_show_search.py", "label": "Search script"},
        ],
    },
    {
        "number": 4,
        "title": "Improve AI-generated code",
        "topic": "Refactoring the AI-generated search script for people to read.",
        "files": [
            {"path": "Module-4 Lab/improved_search.py", "label": "Improved search script"},
        ],
    },
    {
        "number": 5,
        "title": "Retrieve TV show data",
        "topic": "Calling the TVMaze API and showing the results.",
        "files": [
            {"path": "Module-5 Lab/tvmaze_search.py", "label": "TVMaze script"},
            {"path": "Module-5 Lab/README.md", "label": "README"},
            {"path": "Module-5 Lab/json_structure.md", "label": "JSON structure"},
            {"path": "Module-5 Lab/sample_output.txt", "label": "Sample output"},
        ],
    },
    {
        "number": 6,
        "title": "Externalise configuration",
        "topic": "Moving the search term and minimum rating into config.json.",
        "files": [
            {"path": "Module-6 Lab/tvmaze_search.py", "label": "TVMaze script"},
            {"path": "Module-6 Lab/config.json", "label": "Configuration"},
        ],
    },
    {
        "number": 7,
        "title": "Test and break the automation",
        "topic": "Testing valid, invalid, empty and missing-config cases.",
        "files": [
            {"path": "Module-7 Lab/test_log.md", "label": "Test log"},
        ],
    },
    {
        "number": 8,
        "title": "Prepare for workplace use",
        "topic": "Adding logging, error logging and documentation.",
        "files": [
            {"path": "Module-8 Lab/tvmaze_search.py", "label": "Script with logging"},
            {"path": "Module-8 Lab/config.json", "label": "Configuration"},
            {"path": "Module-8 Lab/automation.log", "label": "Log file"},
            {"path": "Module-8 Lab/README.md", "label": "README"},
        ],
    },
]


def allowed_paths():
    """Return the set of file paths the server may read."""
    return {item["path"] for module in MODULES for item in module["files"]}
