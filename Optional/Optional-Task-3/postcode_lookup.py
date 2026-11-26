"""
Offline UK postcode lookup (Optional Task 3).

Asks for a UK postcode and shows its GPS coordinates. The postcodes and
coordinates are read from data/uk_postcodes.csv.gz, so no internet connection
is needed. The file is built from the ONS data by build_postcode_data.py.

Run it in the terminal with:  python3 postcode_lookup.py
The web page in web/server.py uses the same lookup.

Uses only the Python standard library, so no packages need installing.
"""

import csv
import gzip
import re
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data" / "uk_postcodes.csv.gz"

# A UK postcode without spaces: one or two letters, a digit, an optional
# letter or digit, a digit, then two letters. For example SW1A1AA or EC1A1BB.
POSTCODE_PATTERN = re.compile(r"^[A-Z]{1,2}[0-9][A-Z0-9]?[0-9][A-Z]{2}$")


class PostcodeError(Exception):
    """Raised when the input isn't a usable postcode or isn't in the data."""


class PostcodeNotFound(PostcodeError):
    """Raised when a well-formed postcode isn't in the data."""


def normalise_postcode(text):
    """Return the postcode in upper case with no spaces, e.g. 'SW1A1AA'."""
    return "".join(text.split()).upper()


def format_postcode(code):
    """Return the normalised postcode with the standard space, e.g. 'SW1A 1AA'."""
    return f"{code[:-3]} {code[-3:]}"


def load_postcodes(path=DATA_PATH):
    """Read the offline file into a dictionary of postcode -> (latitude, longitude).

    The keys are normalised postcodes, so lookups ignore case and spaces.
    """
    table = {}
    with gzip.open(path, "rt", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row.
        for postcode, latitude, longitude in reader:
            table[normalise_postcode(postcode)] = (float(latitude), float(longitude))
    return table


def lookup_postcode(table, text):
    """Return the postcode and its coordinates as a dictionary.

    Raises PostcodeError if the text is blank, is not in UK postcode format,
    or is not in the data.
    """
    code = normalise_postcode(text)
    if not code:
        raise PostcodeError("Enter a postcode.")
    if not POSTCODE_PATTERN.match(code):
        raise PostcodeError(f"'{text.strip()}' is not in a valid UK postcode format.")

    coordinates = table.get(code)
    if coordinates is None:
        raise PostcodeNotFound(f"'{format_postcode(code)}' was not found in the postcode list.")

    latitude, longitude = coordinates
    return {
        "postcode": format_postcode(code),
        "latitude": latitude,
        "longitude": longitude,
    }


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
