"""
Income tax calculator (Optional Task 5).

Asks for an annual salary and shows the income tax due, band by band. The tax
bands and rates are read from tax_bands.json, so they can change without
changing the code. National Insurance and the personal allowance taper (for
incomes above £100,000) are not included.

Run it in the terminal with:  python3 tax_calculator.py

Uses only the Python standard library, so no packages need installing.
"""

import json
import math
from pathlib import Path

BANDS_PATH = Path(__file__).resolve().parent / "tax_bands.json"


class SalaryError(ValueError):
    """Raised when the salary is not a positive number."""


def load_bands(path=BANDS_PATH):
    """Return the list of tax bands from the config file."""
    with open(path, encoding="utf-8") as file:
        return json.load(file)["bands"]


def parse_salary(text):
    """Return the salary as a number.

    Spaces, commas and a £ sign are ignored. Raises SalaryError if the text is
    not a number or the number is not positive.
    """
    cleaned = text.strip().replace("£", "").replace(",", "")
    try:
        salary = float(cleaned)
    except ValueError:
        raise SalaryError("Enter a number, for example 30000.") from None
    if not math.isfinite(salary) or salary <= 0:
        raise SalaryError("The salary must be a positive number.")
    return salary


def calculate_tax(salary, bands):
    """Work out the tax on each band the salary reaches.

    Returns a list of (band name, income in band, rate, tax in band) and the
    total tax. A band with an up_to of None has no upper limit.
    """
    rows = []
    lower = 0
    for band in bands:
        upper = band["up_to"]
        top = salary if upper is None else min(salary, upper)
        income = max(0, top - lower)
        tax = round(income * band["rate"], 2)
        rows.append((band["name"], income, band["rate"], tax))
        if upper is None or salary <= upper:
            break
        lower = upper

    total = round(sum(row[3] for row in rows), 2)
    return rows, total


def display_tax(salary, rows, total):
    """Print the tax on each band and the total in the terminal."""
    print(f"Income tax on a salary of £{salary:,.2f}:")
    for name, income, rate, tax in rows:
        print(f"  {name:<20} income £{income:,.2f} at {rate:.0%} = £{tax:,.2f}")
    print(f"Total income tax: £{total:,.2f}")


def main():
    """Ask for a salary and show the income tax due."""
    bands = load_bands()

    text = input("Enter your annual salary: £")
    try:
        salary = parse_salary(text)
    except SalaryError as error:
        print(f"Error: {error}")
        return

    rows, total = calculate_tax(salary, bands)
    display_tax(salary, rows, total)


if __name__ == "__main__":
    main()
