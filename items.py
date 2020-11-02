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
