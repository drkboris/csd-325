'''
============================================
# Title: Assignment 7.2
# Author: Zach Donohue
# Date: 30 April 2026
===========================================
Title: test_cities.py
Author: Eric Matthes
Date: 20 March 2026
Modified By: Zach Donohue
Description: This program is used to test the city_functions.py program
============================================
'''

import unittest
from city_functions import city_country


class TestCityCountry(unittest.TestCase):

    def test_city_country(self):
        result = city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()