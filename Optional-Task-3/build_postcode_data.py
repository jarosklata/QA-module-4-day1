"""
Build the offline UK postcode file used by postcode_lookup.py.

Reads the ONS National Statistics Postcode Lookup (NSPL) CSV and writes a
compressed file containing only live postcodes, with their latitude and
longitude.

Source: ONS National Statistics Postcode Lookup, Open Government Licence.
Download the full CSV from the ONS Open Geography Portal, then run:

    python3 build_postcode_data.py path/to/nspl.csv

The output is written to data/uk_postcodes.csv.gz.
"""

import csv
import gzip
import sys
from pathlib import Path

OUTPUT_PATH = Path(__file__).resolve().parent / "data" / "uk_postcodes.csv.gz"


def build(input_path, output_path=OUTPUT_PATH):
    """Write live postcodes with coordinates to a gzip CSV file.

    Returns the number of postcodes written.
    """
    written = 0
    # utf-8-sig removes the byte-order mark at the start of the ONS file.
    with open(input_path, newline="", encoding="utf-8-sig") as source, \
            gzip.open(output_path, "wt", newline="", encoding="utf-8") as target:
        reader = csv.DictReader(source)
        writer = csv.writer(target)
        writer.writerow(["postcode", "latitude", "longitude"])

        for row in reader:
            # In this file, "doterm" is "0" for live postcodes and a date
            # (YYYYMM) for terminated ones.
            if row["doterm"].strip() not in ("", "0"):
                continue
            if not row["lat"] or not row["long"]:
                continue
            writer.writerow([row["pcds"].strip(), row["lat"], row["long"]])
            written += 1

    return written


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 build_postcode_data.py path/to/nspl.csv")
    count = build(sys.argv[1])
    print(f"Wrote {count} live postcodes to {OUTPUT_PATH}")
