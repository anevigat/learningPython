"""Test for nevigato."""
import unittest

import calc


class TestCalc(unittest.TestCase):
    """Test calculator."""

    def test_my_first_test(self):
        """Test add."""
        self.assertEqual(5, calc.add(3, 2))

    def test_div_with_two_numbers(self):
        """Test div."""
        self.assertEqual(3.0, calc.div(6, 2))

    def test_div_with_zero(self):
        """Other one."""
        with self.assertRaises(ZeroDivisionError):
            calc.div(3, 0)
