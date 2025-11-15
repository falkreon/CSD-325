# CSD325: Advanced Python
# Module 6.2: Forest Fire Simulation: Program and Revised Flowchart
# Isaac Ellingson and Sara White
# 11/10/2025

"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time, math

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
WATER = 'W'
EMPTY = ' '

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


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
                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif ((forest[(x, y)] == TREE)
                    and (isAdjacent(forest, x, y, FIRE))):
                    # This tree was adjacent to a fire. Light it on fire too.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree was burning last round. Put it out now.
                    nextForest[(x, y)] = EMPTY

                    # We do not need to include water tiles here because
                    # They will just copy over using the case below.

                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def isAdjacent(forest, x, y, cellType):
    for ix in range(-1, 2):
        for iy in range(-1, 2):
            if forest.get((x + ix, y + iy)) == cellType:
                return True
    return False


def createNewForest():
    """Returns a dictionary for a new forest data structure."""

    # Pick a lake center and radius. Numbers have been picked to place
    # the lake "approximately in the center" each time.
    lakeX = int( random.random() * 20 + 30 ) # random(30..50)
    lakeY = int( random.random() *  3 + 10 ) # random(10..13)
    lakeRadius = random.random() * 5 + 6     # random( 6..11)

    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # We're using the pythagorean theorem to find the distance of
            # this cell from the center of the lake: a^2 + b^2 = c^2
            # So sqrt(dx*dx + dy*dy) is the distance.
            # Note: negative numbers cancel out here in the multiplication,
            # otherwise I'd want to take the abs of dxToLake and dyToLake.
            dxToLake = lakeX - x
            dyToLake = lakeY - y
            distanceToCenter = math.sqrt((dxToLake * dxToLake) + (dyToLake * dyToLake))

            # So, with all the above, if we're "within the radius", we're a lake tile.
            if distanceToCenter < lakeRadius:
                forest[(x, y)] = WATER # Start as part of the lake
            elif (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
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
