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
