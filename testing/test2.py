# test on city_function.py

from city_function import city_country
import unittest

class test_city_country(unittest.TestCase):

    def test_it(self):
        self.assertEqual( city_country("santiago", "chile",90000), "Santiago, Chile - Population=90000")

unittest.main()