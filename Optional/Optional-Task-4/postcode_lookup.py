"""
Checking and looking up a UK postcode (Optional Task 4).

This file holds the rules: tidying up the text, checking the format, and
finding the postcode in the table. It does not read files or print anything,
so it is easy to test on its own.
"""

import re

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
