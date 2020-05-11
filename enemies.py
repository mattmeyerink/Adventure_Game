
# Program written and maintained by Matthew Meyerink

# File defining the characters in the game. Also contains handling for the
# graphics of the main character icon.

from tkinter import *

class Enemy:

    def __init__(self, root):
        self.root = root

        self.voldy_name = "Lord Voldemort"
        self.voldy_hp = 250
        self.voldy_location = "Great Hall"

# Function that will add all of the pre-made enemy objects to the game class.
# Will create a dictionary of enemy objects sorted by location
def add_enemies(root):
    #ToDo add enemies to avoid error
    return 1
