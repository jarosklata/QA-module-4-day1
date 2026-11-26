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
