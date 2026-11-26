"""
Offline UK postcode lookup, split into several files (Optional Task 4).

Asks for a UK postcode and shows its GPS coordinates. This file only handles
the terminal: asking for input and printing results. The other files do the
work:

    postcode_data.py    reads the offline postcode file
    postcode_lookup.py  checks the format and finds the postcode

Run it in the terminal with:  python3 main.py

Uses only the Python standard library, so no packages need installing.
"""

from postcode_data import load_postcodes
from postcode_lookup import PostcodeError, lookup_postcode


def display_postcode(result):
    """Print the postcode and its coordinates in the terminal."""
    print(f"Postcode  : {result['postcode']}")
    print(f"Latitude  : {result['latitude']}")
    print(f"Longitude : {result['longitude']}")


def main():
    """Ask for a postcode and show its GPS coordinates."""
    print("Loading UK postcodes...")
    table = load_postcodes()

    text = input("Enter a UK postcode: ")
    try:
        result = lookup_postcode(table, text)
    except PostcodeError as error:
        print(error)
        return

    display_postcode(result)


if __name__ == "__main__":
    main()
