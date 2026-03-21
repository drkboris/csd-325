'''
============================================
# Title: Assignment 1.3
# Author: Zach Dnohue
# Date: 20 March 2026
===========================================
Title: BeerBottles.py
Author: Zach Donohue
Date: 20 March 2026
Modified By: Zach Donohue
Description: This program takes a number from a user and uses it
#   to cycle through the bottles of beer on the wall song
============================================
'''

def beer_countdown(bottles):
    while bottles > 0:
        if bottles == 1:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print(f"Take one down and pass it around, 0 bottle(s) of beer on the wall.")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.")
        bottles -= 1
        print()

def main():
    bottles = int(input("Enter number of bottles: "))
    beer_countdown(bottles)
    print("Time to buy more bottles of beer.")
    print()

main()