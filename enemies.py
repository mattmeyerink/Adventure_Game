
# Program written and maintained by Matthew Meyerink

# File defining the characters in the game. Also contains handling for the
# graphics of the main character icon.

from tkinter import *
from utility import *

class Enemy:

    def __init__(self, name, graphics):

        self.name = name
        self.graphics = graphics


# Function that will add all of the pre-made enemy objects to the game class.
# Will create a dictionary of enemy objects sorted by location
def add_enemies(canvas):

    #Initialize dictionary of enemies
    enemies_dict = {}

    #Initialize Lord Voldemort
    lord_voldy_canvas = canvas.create_oval((window_width / 2) - character_size,
        100 - character_size, (window_width / 2) + character_size,
        100 + character_size, fill="black")
    lord_voldy = Enemy("Lord Voldemort", lord_voldy_canvas)

    #Add Lord Voldemort to dictionary
    enemies_dict[lord_voldy.name] = lord_voldy

    #Return dicitonary of enemies
    return enemies_dict
