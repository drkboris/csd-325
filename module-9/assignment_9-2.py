'''
===========================================
Title: assignment_9-2.py
API Tutorial: https://www.dataquest.io/blog/api-in-python/
Author: Charlie Custer
Date: 14 May 2026
Modified By: Zach Donohue
Directions:  The first is to work through a tutorial on APIs then to write
a Python program using an API of your choice. Couple of things to consider
when you work with APIs; it's best to test the connection before you start
working with the response. For example, open up a new python file and use
this code (save before running):


Using the Open Trivia Database - https://opentdb.com
No API key needed which makes it easy to work with

import requests
response = requests.get('http://www.google.com')
print(response.status_code)

============================================
'''

import requests
import json

# same jprint function from the tutorial, reusing it here for formatting
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Task 6(b) - test the connection
url = "https://opentdb.com/api.php"
params = {
    "amount": 5,
    "type": "multiple",
    "difficulty": "medium"
}

response = requests.get(url, params=params)
print("Status Code:", response.status_code)

# Task 6(c) - print the raw response with no formatting
print(response.json())

# Task 6(d) - print the formatted version using jprint
jprint(response.json())