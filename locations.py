
# Program written and maintained by Matthew Meyerink

# File containing class definition for locations

from tkinter import *
from utility import *

class Location:

    def __init__(self, canvas, exit):

        self.canvas = canvas

        #Adding the exit points to the locations 
        self.exit = exit


# Function that will add all of the pre-made location objects to the game class.
# Will create a Dictionary of location objects
def add_locations(root):

    #Initialize dictionary of locaitons
    locations_dict = {}

    #Initialize the Great Hall
    great_hall_exit = (window_height - character_size)
    great_hall = Location(Canvas(root, width=window_width,
                                            height=window_height, bg="wheat2"))

    #Add house tables
    great_hall.canvas.create_rectangle(100, 250, 175 , 500, fill="MistyRose4")
    great_hall.canvas.create_rectangle(275, 250, 350, 500, fill="MistyRose4")
    great_hall.canvas.create_rectangle(450, 250, 525, 500, fill="MistyRose4")
    great_hall.canvas.create_rectangle(625, 250, 700, 500, fill="MistyRose4")

    #Add high table
    great_hall.canvas.create_rectangle(200, 50, 600, 125, fill="MistyRose4")

    #Add great_hall to the list of locations
    locations_dict["Great Hall"] = great_hall

    #Return the completed dictionary of locations
    return locations_dict
