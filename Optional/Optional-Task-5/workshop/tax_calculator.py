"""Income tax calculator, Part 1: personal allowance and basic rate only."""

PERSONAL_ALLOWANCE = 12_570  # the first £12,570 is tax-free (0%)
BASIC_RATE_LIMIT = 50_270    # the basic rate applies up to this salary
BASIC_RATE = 0.20            # 20%


def calculate_tax(salary):
    """Return the income tax due on a salary, in pounds."""
    if salary < 0:
        raise ValueError("Salary cannot be negative.")
    if salary > BASIC_RATE_LIMIT:
        raise ValueError("Salaries above £50,270 need the higher rate, which is not supported yet.")

    taxable_income = max(0, salary - PERSONAL_ALLOWANCE)
    return round(taxable_income * BASIC_RATE, 2)


def main():
    text = input("Enter your annual salary: £")
    try:
        salary = float(text)
    except ValueError:
        print("Error: please enter a number.")
        return

    try:
        tax = calculate_tax(salary)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"Income tax: £{tax:,.2f}")


if __name__ == "__main__":
    main()
