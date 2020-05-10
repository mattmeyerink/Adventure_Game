
# Program written and maintained by Matthew Meyerink

# File defining the class that contains all of the characters in the game.

from tkinter import *
from locations import Location

class Enemy:

    def __init__(self, root):
        self.root = root

        self.voldy_name = "Lord Voldemort"
        self.voldy_hp = 250
        self.voldy_location = "Great Hall"

class Hero:

    hp = 250
    window_height = 600
    window_width = 800

    def __init__(self, root):

        self.root = root

        self.hero_figure = Canvas(self.root, width=self.window_width,
            height=self.window_height, bg="wheat2")
        self.hero_figure.config(bg='')

    def is_alive(self):
        return self.hp > 0

    # Add player canvas that has the shape of the player as a shape on a
    # transparent background
