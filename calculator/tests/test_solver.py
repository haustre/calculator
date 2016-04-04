"""
This module contains unittests for the calculation .
"""

__author__ = 'Wuersch Marcel'
__license__ = "GPLv3"


from unittest import TestCase
from calculator.solver import Solver


class TestMathematicalOperations(TestCase):
    """
    Unittest + - * / ()
    all calculations are given as string
    """

    def setUp(self):
        self.solver = Solver()

    def test_basic_operations(self):
        """ Test + - */ """
        self.assertEqual(self.solver.calculate("3*5"), 15)
        self.assertEqual(self.solver.calculate("3/5"), 0.6)
        self.assertEqual(self.solver.calculate("3+5"), 8)
        self.assertEqual(self.solver.calculate("5-3"), 2)
        self.assertEqual(self.solver.calculate("3-5"), -2)
        self.assertEqual(self.solver.calculate("3*-7"), -21)
        self.assertEqual(self.solver.calculate("3/-4"), -0.75)

    def test_multiple_basic_operations(self):
        """ Test multiple operations in one string"""
        self.assertEqual(self.solver.calculate("3+5+7"), 15)
        self.assertEqual(self.solver.calculate("3+5*7"), 38)
        self.assertAlmostEqual(self.solver.calculate("3+5/7"), 3.714285714)

    def test_divide_0(self):
        """ Test divide by 0 exception"""
        self.assertRaises(ZeroDivisionError, lambda: self.solver.calculate("3/0"))

    def test_parentheses(self):
        """ Test calculation with single parentheses"""
        self.assertEqual(self.solver.calculate("(3+5)*7"), 56)
        self.assertAlmostEqual(self.solver.calculate("(3-5)/7"), -0.285714286)

    def test_multiple_parentheses(self):
        """ Test calculation with multiple parentheses"""
        self.assertEqual(self.solver.calculate("(3+5)*(7-11)"), -32)
        self.assertAlmostEqual(self.solver.calculate("(3-5)/(7/11)"), -3.142857143)

    def test_with_spaces(self):
        """ Test string whit white spaces"""
        self.assertEqual(self.solver.calculate("(3 +5 ) *(7 -11 ) "), -32)

    def test_wrong_input(self):
        """ Test return value for false input"""
        self.assertEqual(self.solver.calculate("(3 +5 ) **(7 -11 ) "), False)
        self.assertEqual(self.solver.calculate("(3 +5 ) *(7 -11 ) a"), False)

