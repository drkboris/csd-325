

"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""
"""
===========================================
Title: forestfiresim_325.py
Author: Sue Sampson (Based on program by Al Sweigart)
Date: 23 April 2026
Modified By: Zach Donohue
Description: modified to Add lake for Module 6.2 Assignment
===========================================
Task 3 Modifications
  - Added a lake roughly centered in the display.
  - Lake uses '~' character rendered in blue (not 'A' or '@').
  - Lake cells are permanent: they are set once at forest creation and
    are never overwritten by trees, fire, or empty space during simulation.
  - The lake acts as a firebreak: fire cannot spread to water cells.
To find any modification in program search 'Task 3 modification'
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
# Task 3 modification - new constant for water
WATER = '~'


# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.25  # Amount of forest that starts with trees.
GROW_CHANCE = 0.02  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.03  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5

# Task 3 modification - Lake geography characteristics
# The display is 79 columns wide and 22 rows tall.
# These values define a rectangle roughly centered on the screen.
# Center of screen is approximately x=39, y=11.
LAKE_X_START = 33  # Left edge of the lake
LAKE_X_END   = 46  # Right edge of the lake
LAKE_Y_START = 8   # Top edge of the lake
LAKE_Y_END   = 14  # Bottom edge of the lake



def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue


                # Task 3 modification -  Water cells are permanent and
                # act as a firebreak. If the current cell is WATER, copy
                # it unchanged into the next generation and skip all
                # other logic. This prevents trees from growing in the
                # lake and prevents fire from replacing water cells.
                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER
                    continue


                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Task 3 modification - Fire spreads to neighboring
                            # trees only if the neighbor is NOT water.
                            # This makes the lake act as a firebreak.  Flames
                            # cannot jump across water cells.
                            neighbor = forest.get((x + ix, y + iy))
                            if neighbor == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    """Task 3 Modification - After randomly placing trees and empty spaces,
    any cellthat falls within the lake boundary rectangle is overwritten with
    WATER. The lake boundary is checked using a simple x/y range comparison.
    """
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.

    # Task 3 Modification - Place the lake onto the forest grid.
    # Any cell within the rectangle defined by the lake boundary constants
    # is set to WATER, overwriting whatever was randomly placed there.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if LAKE_X_START <= x <= LAKE_X_END and LAKE_Y_START <= y <= LAKE_Y_END:
                forest[(x, y)] = WATER 

    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            # Task 3 Modification - Render water cells in blue using
            # the '~' character.
            elif forest[(x, y)] == WATER:
                bext.fg('blue')
                print(WATER, end='')          	
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
