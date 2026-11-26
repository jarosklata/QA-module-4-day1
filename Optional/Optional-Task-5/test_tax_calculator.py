import unittest

from tax_calculator import SalaryError, calculate_tax, load_bands, parse_salary


class TaxBandsConfigTests(unittest.TestCase):
    def test_config_has_all_four_bands_in_order(self):
        names = [band["name"] for band in load_bands()]
        self.assertEqual(names, ["Personal allowance", "Basic rate", "Higher rate", "Additional rate"])


class CalculateTaxTests(unittest.TestCase):
    def setUp(self):
        self.bands = load_bands()

    def tax_on(self, salary):
        _, total = calculate_tax(salary, self.bands)
        return total

    def test_salary_at_personal_allowance_pays_no_tax(self):
        self.assertEqual(self.tax_on(12_570), 0)

    def test_first_pound_above_personal_allowance_is_taxed_at_20_percent(self):
        self.assertEqual(self.tax_on(12_571), 0.20)

    def test_typical_basic_rate_salary(self):
        self.assertEqual(self.tax_on(30_000), 3_486)

    def test_salary_at_top_of_basic_rate_band(self):
        self.assertEqual(self.tax_on(50_270), 7_540)

    def test_first_pound_above_basic_rate_band_is_taxed_at_40_percent(self):
        self.assertEqual(self.tax_on(50_271), 7_540.40)

    def test_typical_higher_rate_salary(self):
        self.assertEqual(self.tax_on(60_000), 11_432)

    def test_salary_at_top_of_higher_rate_band(self):
        self.assertEqual(self.tax_on(125_140), 37_488)

    def test_first_pound_above_higher_rate_band_is_taxed_at_45_percent(self):
        self.assertEqual(self.tax_on(125_141), 37_488.45)

    def test_breakdown_lists_each_band_reached(self):
        rows, total = calculate_tax(60_000, self.bands)
        self.assertEqual(
            [(name, income, tax) for name, income, _, tax in rows],
            [
                ("Personal allowance", 12_570, 0),
                ("Basic rate", 37_700, 7_540),
                ("Higher rate", 9_730, 3_892),
            ],
        )
        self.assertEqual(total, 11_432)


class ParseSalaryTests(unittest.TestCase):
    def test_plain_number(self):
        self.assertEqual(parse_salary("30000"), 30_000)

    def test_pound_sign_and_commas_are_ignored(self):
        self.assertEqual(parse_salary(" £30,000 "), 30_000)

    def test_text_is_rejected(self):
        with self.assertRaises(SalaryError):
            parse_salary("thirty thousand")

    def test_zero_is_rejected(self):
        with self.assertRaises(SalaryError):
            parse_salary("0")

    def test_negative_salary_is_rejected(self):
        with self.assertRaises(SalaryError):
            parse_salary("-5000")

    def test_not_a_finite_number_is_rejected(self):
        for text in ("nan", "inf"):
            with self.subTest(text=text):
                with self.assertRaises(SalaryError):
                    parse_salary(text)


if __name__ == "__main__":
    unittest.main()
