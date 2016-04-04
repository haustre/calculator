__author__ = 'Wuersch Marcel'
__license__ = "GPLv3"

import sys
import re
import csv
from solver import Solver


class Persistence:
    filename = "last_calculations.txt"
    fieldnames = ["calculation", "result"]

    def __init__(self):
        pass

    def add_calculation(self, calculation, result):
        with open(self.filename, 'w') as file:
            writer = csv.DictWriter(file, self.fieldnames)
            writer.writerow({"calculation": calculation, "result": result})
            file.flush()

    def get_last_calculations(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file, self.fieldnames)
                for line in reader:
                    return line["calculation"], line["result"]
        except FileNotFoundError:
            return None


if __name__ == "__main__":
    solver = Solver()
    persistence = Persistence()
    output_str = """
    Welcome to Calculator
    Allowed operators: +-*/()
    Example: "3*(5-7)"
    Enter q to quit
    """
    print(output_str)
    data_last = persistence.get_last_calculations()  # Get last calculation from file
    if data_last is not None:  # Only show it if available
        last_calculation, last_result = data_last
        print("Last calculation: %s = %s" % (last_calculation, last_result))
    else:
        last_result = ""
    while True:
        user_input = input('calculation: ')  # Get user input
        pattern = r"^[+\-*\/]{1}"  # regular expressions for leading operator
        match = re.search(pattern, user_input)  # search in user input
        if match:  # if leading operator is found add last result in front of input
            user_input = str(last_result) + user_input
        if user_input == "q":  # close program
            del persistence
            print("Bye")
            sys.exit()
        result = solver.calculate(user_input)  # solve the equation
        if result == 'wrong format':  # solver didn't understand the equation
            print("                  Wrong input format")
        elif result == 'zero division':
            print("                  Division by zero!")
        else:  #
            print("                  Result: " + str(result))
            last_result = result
            persistence.add_calculation(user_input, str(result))
