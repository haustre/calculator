"""
This module calculates the result of a given mathematical equation.
"""

__author__ = 'Wuersch Marcel'
__license__ = "GPLv3"

import re  # regular expressions


class Solver:
    """
    This Class parses a given string and calculates the result
    The calculation is solved using recursion
    The following operators are allowed: +-*/()
    """
    def __init__(self):
        pass

    def calculate(self, string):
        """
        :param string: calculation to solve
        :return: result (float)
        """
        try:
            string = string.replace(" ", "")
            result = self._find_parentheses(string)
            return result
        except ValueError:
            return 'wrong format'
        except ZeroDivisionError:
            return 'zero division'

    def _find_parentheses(self, string):
        """ find all the parentheses and replace them with the result """
        while True:
            pattern = r"\([^\(\)]+\)"  # regular expression for inner parentheses
            match = re.search(pattern, string)
            if match:
                substring = match.group()
                substring = substring[1:-1]
                result = str(self._find_parentheses(substring))
                new_string = string[0:match.start()]+result + string[match.end()::]
                string = new_string
            else:
                break
        return self._find_basic_operations(string)

    def _find_basic_operations(self, string):
        """ solve all basic math operations using recursion
        """
        # regular expression for addition and subtraction
        pattern_add      = r"(?P<number1>.*[^*\/])(?P<operator>[+\-])(?P<number2>.+)"
        # regular expression for multiplication and division
        pattern_multiply = r"(?P<number1>.+)(?P<operator>[*\/])(?P<number2>.+)"
        match_add = re.search(pattern_add, string)
        match_multiply = re.search(pattern_multiply, string)
        if match_add:  # first search for +- operation
            match = match_add
        elif match_multiply:  # second search for */
            match = match_multiply
        else:  # last try to convert to a number
            return float(string)

        number1_str = match.group('number1')
        number2_str = match.group('number2')
        number1 = self._find_basic_operations(number1_str)
        number2 = self._find_basic_operations(number2_str)
        operator = match.group('operator')
        return self._basic_operation(number1, number2, operator)

    def _basic_operation(self, number1, number2, operator):
        """ execute basic mathematics operation """
        operators = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y,
            '/': lambda x, y: x/y,
        }
        return operators[operator](number1, number2)
