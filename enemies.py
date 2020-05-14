
# Program written and maintained by Matthew Meyerink

# File defining the characters in the game. Also contains handling for the
# graphics of the main character icon.

from tkinter import *
from utility import *

class Enemy:

    def __init__(self, name, location, color, x_position, y_position):

        self.name = name
        self.location = location
        self.color = color
        self.x_position = x_position
        self.y_position = y_position


# Function that will add all of the pre-made enemy objects to the game class.
# Will create a list of enemy objects
def add_enemies():

    #Initialize dictionary of enemies
    enemies_list = {}

    #Initialize Lord Voldemort
    lord_voldy = Enemy("Lord Voldemort", "Great Hall", "black",
                                        window_width / 2, window_height / 3.5)

    #Add Lord Voldemort to list
    enemies_list[0] = lord_voldy

    #Return dicitonary of enemies
    return enemies_list

# prints the enemies located in the current location to the screen
def print_enemies(current_location, screen, enemies):

    for i in enemies:
        if enemies[i].location == current_location:

            #Calculate dimensions of character oval
            x1 = enemies[i].x_position - character_size
            y1 = enemies[i].y_position - character_size

            x2 = enemies[i].x_position + character_size
            y2 = enemies[i].y_position + character_size

            screen.create_oval(x1, y1, x2, y2, fill=enemies[i].color)
