'''
============================================
# Title: Assignment 7.2
# Author: Zach Donohue
# Date: 30 April 2026
===========================================
Title: city_functions.py
Author: Eric Matthes
Date: 20 March 2026
Modified By: Zach Donohue
Description: This program is used provide functions for the test_cities.py program to test
============================================
'''

# Optional parameters set with =None
def city_country(city, country, population=None, language=None):
    result = f"{city}, {country}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language}"
    return result


# City, Country only
print(city_country("Santiago", "Chile"))

# City, Country, Population
print(city_country("New York City", "United States", 8600000000))

# City, Country, Population, Language
print(city_country("Dublin", "Ireland", 1500000, "Gaeilge"))



