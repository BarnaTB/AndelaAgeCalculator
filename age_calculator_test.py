import unittest
from age_calculator import ageCalculator


class TestSwitchReverser(unittest.TestCase):
    def test_correct_age_is_calculated(self):
        birth_year = 1990
        assert ageCalculator(birth_year) == 28

    def test_only_integer_is_accepted(self):
        birth_year = 'Nineteen Ninty'
        self.assertEqual(ageCalculator(birth_year), 'Please enter a number.')

    def test_string_to_integer_is_accepted(self):
        birth_year = '1990'
        self.assertEqual(ageCalculator(int(birth_year)), 28)
