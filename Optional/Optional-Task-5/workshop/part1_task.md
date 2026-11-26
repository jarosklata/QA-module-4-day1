# Day 4 Workshop: Part 1 - Income Tax Calculator

Create a program that works out UK income tax on a salary.

For this part, support only the first two bands:

| Band | Taxable income | Rate |
|---|---|---|
| Personal allowance | Up to £12,570 | 0% |
| Basic rate | £12,571 to £50,270 | 20% |

Requirements:

- Ask the user for an annual salary.
- Show the income tax due, for example `Income tax: £3,486.00`.
- Reject negative salaries and salaries above £50,270. Higher rates come in Part 2.
- Write tests for these boundaries: £0, £12,570, £12,571 and £50,270.

Run the tests from the `day4-workshop` folder with:

```
python3 -m unittest
```

Reference: [GOV.UK: Income Tax rates and bands](https://www.gov.uk/income-tax-rates)
