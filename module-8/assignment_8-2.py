'''
============================================
# Title: Assignment 8.2
# Author: Zach Donohue
# Date: 8 May 2026
===========================================
Title: assignment_8-2.py
Author: Zach Donohue
Date: 8 May 2026
Modified By: Zach Donohue
Description: Read and update JSON file of a student list
============================================
'''

import json
import os
 
# File path for the JSON file
JSON_FILE = "Student.json"
 
def print_students(student_list):
    """Loop through the student list and print each record."""
    for student in student_list:
        print(f"  {student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")
 
 
def main():
    # Use the JSON load() function to load the file into a Python class list.
    with open(JSON_FILE, "r") as f:
        students = json.load(f)
 

    # Print original list
    print("=" * 55)
    print("         Original Student List")
    print("=" * 55)
    print_students(students)
 

    # Append a new student record
    new_student = {
        "F_Name": "Zach",
        "L_Name": "Donohue",
        "Student_ID": 8675309,
        "Email": "zldonohue@choraspeace.com"
    }
    students.append(new_student)
 

    # Print updated list
    print()
    print("=" * 55)
    print("         Updated Student List")
    print("=" * 55)
    print_students(students)
 

    # Write updated list back to the JSON file (dump)
    with open(JSON_FILE, "w") as f:
        json.dump(students, f, indent=4)
 
    print()
    print("=" * 55)
    print(f"  SUCCESS: '{JSON_FILE}' has been updated with the")
    print("  new student record.")
    print("=" * 55)
 
 
if __name__ == "__main__":
    main()