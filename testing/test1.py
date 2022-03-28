# test name_function.py

import unittest
import sys
from name_function import formatted_name, print_formatted_name


# unit test on formatted_name()

class NamesTestCase(unittest.TestCase):     # class that contains a series of test case

    def test_full_name(self):
        self.assertEqual( formatted_name("zi qing", "chew"), 'Zi Qing Chew' )


unittest.main()

print("Enter 'q' or 'Q' to exit at any time.")
print("**************************************")


def is_exit(prompt):
    if prompt == 'q' or prompt == 'Q':
        sys.exit()

while True:
    first = input("Enter first name:")
    is_exit(first)

    last = input("Enter last name: ")
    is_exit(last)

    print_formatted_name( formatted_name(first, last) )





