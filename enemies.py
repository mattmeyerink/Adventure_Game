
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
    enemies_list = dict()

    #Initialize Lord Voldemort
    lord_voldy_weapons = ["None"]
    lord_voldy = Enemy("Lord Voldemort", "Great Hall", "black",
            window_width / 2, window_height / 3.5, lord_voldy_weapons)

    #Add Lord Voldemort to list
    enemies_list[0] = lord_voldy

    horcrux_weapons = ["Sword of Gryffindor", "Basalisk Fang"]

    #Initialize Tom Riddle's Diary
    riddles_diary = Enemy("Tom Riddle's Diary", "Upstairs Corridor", "OliveDrab4",
            window_width / 2, window_height / 3.5, horcrux_weapons)

    enemies_list[1] = riddles_diary

    #Initialize The Gaunt Ring
    gaunt_ring = Enemy("The Gaunt Ring", "Dungeons", "gray16",
            window_width / 2, window_height / 3.5, horcrux_weapons)

    enemies_list[2] = gaunt_ring

    #Initialize The Locket
    locket = Enemy("The Locket", "Ravenclaw Common Room", "gold2",
        window_width / 2, window_height / 3.5, horcrux_weapons)

    enemies_list[3] = locket

    #Initialize Hufflepuff's Cup
    hufflepuffs_cup = Enemy("Hufflepuff's Cup", "Gryffindor Common Room", "yellow2",
        window_width / 2, window_height / 3.5, horcrux_weapons)

    enemies_list[4] = hufflepuffs_cup

    #Initialize Ravenclaw's Diadem
    ravenclaws_diadem = Enemy("Ravenclaw's Diadem", "Room of Requirement", "SkyBlue4",
        window_width / 2, window_height / 3.5, horcrux_weapons)

    enemies_list[5] = ravenclaws_diadem

    #Initialize the Snake
    snake = Enemy("Nagini", "Hagrid's Hut", "orange4",
        window_width / 2, window_height / 3.5, horcrux_weapons)

    enemies_list[6] = snake

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
