
#Program written and maintained by Matthew Meyerink

#File containing class definitions and functions for items that can be picked up

from utility import *

class Item:

    def __init__(self, name, description, location, color, x_position,
        y_position):

        self.name = name
        self.description = description
        self.location = location
        self.color = color
        self.x_position = x_position
        self.y_position = y_position
        self.picked_up = False

# Function that will add all of the pre-made items to the game class. Will
# return a list of items objects.
def add_items():

    #Initialize list of items
    items_list = {}

    #Initialize Hogwarts a History object

    hogwarts_a_history = Item("Hogwarts a History", "Fantastic book detailing "
        + "the history of Hogwarts School of Witchcraft and Wizardry\n",
        "Great Hall", "blue", window_width/25, window_height/2)

    #Add Hogwarts a History to items list
    items_list[0] = hogwarts_a_history

    #Returns list of items
    return items_list

#Prints items located in current location
def print_items(current_location, screen, items):

    for i in items:
        if (items[i].location == current_location) and (items[i].picked_up == False):

            x1 = items[i].x_position - item_size
            y1 = items[i].y_position - item_size

            x2 = items[i].x_position + item_size
            y2 = items[i].y_position + item_size

            screen.create_rectangle(x1, y1, x2, y2, fill=items[i].color)
