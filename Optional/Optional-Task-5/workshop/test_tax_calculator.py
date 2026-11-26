import unittest

from tax_calculator import calculate_tax


class BasicRateTests(unittest.TestCase):
    def test_zero_salary_pays_no_tax(self):
        self.assertEqual(calculate_tax(0), 0)

    def test_salary_at_personal_allowance_pays_no_tax(self):
        self.assertEqual(calculate_tax(12_570), 0)

    def test_first_pound_above_personal_allowance_is_taxed_at_20_percent(self):
        self.assertEqual(calculate_tax(12_571), 0.20)

    def test_typical_salary(self):
        self.assertEqual(calculate_tax(30_000), 3_486)

    def test_salary_at_top_of_basic_rate_band(self):
        self.assertEqual(calculate_tax(50_270), 7_540)


class InvalidSalaryTests(unittest.TestCase):
    def test_negative_salary_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_tax(-1)

    def test_salary_above_basic_rate_band_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_tax(50_271)


if __name__ == "__main__":
    unittest.main()
