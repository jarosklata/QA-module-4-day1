"""
Loading the offline UK postcode file (Optional Task 4).

The file is the same one used by Optional Task 3, so it is read from that
folder rather than copied here. It is built by build_postcode_data.py in
Optional-Task-3.
"""

import csv
import gzip
from pathlib import Path

from postcode_lookup import normalise_postcode

DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "Optional-Task-3" / "data" / "uk_postcodes.csv.gz"
)


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
