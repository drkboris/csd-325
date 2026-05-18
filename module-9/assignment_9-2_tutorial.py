'''
===========================================
Title: assignment_9-2_tutorial.py
API Tutorial: https://www.dataquest.io/blog/api-in-python/
Author: Charlie Custer
Date: 14 May 2026
Modified By: Zach Donohue
Directions:  The first is to work through a tutorial on APIs then to write
a Python program using an API of your choice. Couple of things to consider
when you work with APIs; it's best to test the connection before you start
working with the response. For example, open up a new python file and use
this code (save before running)
============================================
'''

import requests
import json

# test the connection using google like the assignment says
response = requests.get('http://www.google.com')
print(response.status_code)

# use the open notify API to get astronaut data
response = requests.get("http://api.open-notify.org/astros")
print(response.status_code)

# print the raw response
print(response.json())

# format string with indent=4 to make it readable
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# print the formatted version
jprint(response.json())
