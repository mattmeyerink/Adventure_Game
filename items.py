"""
Contains Item class defining an item in the game and add items
function to initialize all items in the game and add them into a dictionary
to be used by the game class.
"""
from utility import *


class Item:
    """Class that defines an item in the game."""
    def __init__(self, name, description, location, color, x_position,
        y_position):
        """Initializes an instance of item class."""
        self.name = name
        self.description = description
        self.location = location
        self.color = color
        self.x_position = x_position
        self.y_position = y_position
        self.picked_up = False

def add_items():
    """Returns a dictionary of items necissary for Adventure Game."""
    items_list = dict()

    # Initialize Hogwarts a History object
    hogwarts_a_history = Item("Hogwarts a History", "Fantastic book detailing "
        + "the history of Hogwarts School of Witchcraft and Wizardry\n",
        "Great Hall", "blue", window_width/25, window_height/2)

    items_list[0] = hogwarts_a_history

    # Initialize the Sword of Gryffindor
    sword_of_gryffindor = Item("Sword of Gryffindor", "Powerful sword embedded with "
        + "basalisk venom. Presents itself to any worthy Gryffindor\n",
        "Gryffindor Common Room", "red", window_width/25, window_height/2)

    items_list[1] = sword_of_gryffindor

    # Initialize Basalisk Fang
    basalisk_fang = Item("Basalisk Fang", "Basalisk fang containing highly toxic "
        + "basalisk venom. Can be used to destroy horcruxes\n",
        "Dungeons", "white", window_width/25, window_height/2)

    items_list[2] = basalisk_fang

    # Initialize Firebolt
    firebolt = Item("Firebolt", "Firebolt. An international standard broom with "
        + "stellar speed and handling.\n", "Main Entrance",
        "burlywood4", window_width*3/4, window_height/2)
    
    items_list[3] = firebolt

    # Initialize Hedwig
    hedwig = Item("Hedwig", "Hedwig. A beautiful snow owl. A wonderful companion "
        + "for your dangerous journey.\n", "Hagrid's Hut", "white",
        window_width*3/4, window_height/2)

    items_list[4] = hedwig

    # Initialize Butterbeer
    butterbeer = Item("Butterbeer", "Butterbeer. A tasty treat served warm or cold.\n",
        "Upstairs Corridor", "yellow", window_width/2, window_height/2)
    
    items_list[5] = butterbeer

    # Initialize invisibility cloak
    invisibility_cloak = Item("Invisibility Cloak", "Invisibility Cloak. Not a" 
        + " bad thing to have just in case!\n", "Room of Requirement", 
        "white", window_width/2, window_height/2)

    items_list[6] = invisibility_cloak

    # Initialize wizard chess set
    wizard_chess = Item("Wizard Chess", "Wizard Chess. A fun, slightly more brutal,"
        + " take on normal chess.\n", "Ravenclaw Common Room", "gray52",
        window_width/2, window_height/2)

    items_list[7] = wizard_chess

    # Returns list of items
    return items_list

def print_items(current_location, screen, items):
    """Adds all items in the current location to the current canvas."""
    for i in items:
        if (items[i].location == current_location) and (items[i].picked_up == False):

            x1 = items[i].x_position - item_size
            y1 = items[i].y_position - item_size

            x2 = items[i].x_position + item_size
            y2 = items[i].y_position + item_size

            screen.create_rectangle(x1, y1, x2, y2, fill=items[i].color)
