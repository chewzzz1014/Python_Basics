import unittest
from Employee import Employee

class testEmployee(unittest.TestCase):

    def test_give_default_raise(self):
        e1 = Employee("zi qing","chew",3500)
        e1.give_raise()
        self.assertEqual(8500, e1.salary)

    def test_give_custom_raise(self):
        e2 = Employee("john","smith", 5600)
        e2.give_raise(2000)
        self.assertEqual(7600, e2.salary)

    def setUp(self):
        e1 = Employee("zi qing", "chew", 3500)
        e1.give_raise()
        self.assertEqual(8500, e1.salary)

        e1.give_raise(1000)
        self.assertEqual(9500, e1.salary)


unittest.main()