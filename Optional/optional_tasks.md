# Optional Tasks

## Optional Task 2: Weather

Retrieve the current weather or weather forecast for a given location.

**Optional link:** [BBC Weather](https://www.bbc.co.uk/weather), or any other weather website.

## Optional Task 3: Postcode to GPS Coordinates

Create a simple Python program that:

- asks the user for a UK postcode;
- converts the postcode into GPS coordinates;
- works without internet access.

> **Hint:** To work offline, the project must include the complete list of UK postcodes and their GPS coordinates. The program can then perform the lookup without internet access.

**Optional link:** [postcodes.io](https://postcodes.io)

## Optional Task 4: Refactor into Several Files

Refactor the program from Optional Task 3 so that the code is split across several files.

## Optional Task 5: Income Tax Calculator

Create a simple Python program that:

- asks the user for an annual salary and rejects anything that is not a positive number;
- reads the tax bands (thresholds and rates) from a config file, such as `tax_bands.json`, so the rates can change without editing the code;
- works out the income tax on the salary, band by band;
- shows the amount of tax paid in each band and the total.

Use the salary as the taxable income and ignore National Insurance and the personal allowance taper (for incomes above £100,000).

> **Hint:** Use these example figures to practise. They are not guaranteed to be current, so check the rates for the current tax year before relying on them.
>
> | Band | Taxable income | Rate |
> |---|---|---|
> | Personal allowance | Up to £12,570 | 0% |
> | Basic rate | £12,571 to £50,270 | 20% |
> | Higher rate | £50,271 to £125,140 | 40% |
> | Additional rate | Over £125,140 | 45% |

Write tests for at least these salaries, which give the expected total tax:

| Salary | Expected tax |
|---|---|
| £12,570 | £0 |
| £30,000 | £3,486 |
| £50,270 | £7,540 |
| £60,000 | £11,432 |

**Optional link:** [GOV.UK: Income Tax rates and bands](https://www.gov.uk/income-tax-rates)
