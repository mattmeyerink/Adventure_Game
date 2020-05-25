
# Program written and maintained by Matthew Meyerink

# File defining the characters in the game. Also contains handling for the
# graphics of the main character icon.

from tkinter import *
from utility import *

class Enemy:

    def __init__(self, name, location, color, x_position, y_position,
        deadly_weapon):

        self.name = name
        self.location = location
        self.color = color
        self.x_position = x_position
        self.y_position = y_position
        self.deadly_weapon = deadly_weapon
        self.is_destroyed = False

    # Input: are any of the deadly weapon items present in the hero's inventory
    # Returns true if hero has necissary weapon, false otherwise
    def can_kill(self, hero_inventory):
        for i in range(len(hero_inventory)):
            if hero_inventory[i] in self.deadly_weapon:
                return True
        return False

# Function that will add all of the pre-made enemy objects to the game class.
# Will create a list of enemy objects
def add_enemies():

    #Initialize list of enemies
    enemies_list = {}

    #Initialize Lord Voldemort
    lord_voldy_weapons = ["Hogwarts a History", "wand"]
    lord_voldy = Enemy("Lord Voldemort", "Great Hall", "black",
            window_width / 2, window_height / 3.5, lord_voldy_weapons)

    #Add Lord Voldemort to list
    enemies_list[0] = lord_voldy

    #Return list of enemies
    return enemies_list

# prints the enemies located in the current location to the screen
def print_enemies(current_location, screen, enemies):

    for i in enemies:
        if (enemies[i].location == current_location and
                                            enemies[i].is_destroyed == False):

            #Calculate dimensions of character oval
            x1 = enemies[i].x_position - character_size
            y1 = enemies[i].y_position - character_size

            x2 = enemies[i].x_position + character_size
            y2 = enemies[i].y_position + character_size

            screen.create_oval(x1, y1, x2, y2, fill=enemies[i].color)
