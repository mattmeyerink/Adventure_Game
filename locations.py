
# Program written and maintained by Matthew Meyerink

# File containing class definition for locations

from tkinter import *
from utility import *

class Location:

    def __init__(self, canvas, room_description, top_room, bottom_room):

        self.canvas = canvas
        self.room_description = room_description
        self.top_room = top_room
        self.bottom_room = bottom_room



# Function that will add all of the pre-made location objects to the game class.
# Will create a Dictionary of location objects
def add_locations(root):

    #Initialize dictionary of locaitons
    locations_dict = {}

    #########################################################################
    #########################################################################

    #Initialize the Great Hall
    great_hall_description = "You have entered the Great Hall!"

    great_hall_top_room = "None"
    great_hall_bottom_room = "Main Entrance"

    great_hall = Location(Canvas(root, width=window_width,
        height=window_height, bg="wheat2"), great_hall_description,
        great_hall_top_room, great_hall_bottom_room)

    #Add house tables
    great_hall.canvas.create_rectangle(100, 250, 175 , 500, fill="MistyRose4")
    great_hall.canvas.create_rectangle(275, 250, 350, 500, fill="MistyRose4")
    great_hall.canvas.create_rectangle(450, 250, 525, 500, fill="MistyRose4")
    great_hall.canvas.create_rectangle(625, 250, 700, 500, fill="MistyRose4")

    #Making the walls
    right_wall = great_hall.canvas.create_rectangle(window_width, 0,
                                window_width + 10, window_height, fill="white")
    left_wall = great_hall.canvas.create_rectangle(-10, 0, 0, window_height,
                                                                fill="white")
    top_wall = great_hall.canvas.create_rectangle(0, -10,
                                                window_width, 0, fill="white")
    bottom_wall_left = great_hall.canvas.create_rectangle(0, window_height,
                                left_door_boundary, window_height, fill="white")
    bottom_wall_right = great_hall.canvas.create_rectangle(right_door_boundary,
                    window_height, window_width, window_height, fill="white")

    #Add high table
    great_hall.canvas.create_rectangle(200, 50, 600, 125, fill="MistyRose4")

    #Add great_hall to the list of locations
    locations_dict["Great Hall"] = great_hall

    #########################################################################
    #########################################################################

    #Initialize the main entrance
    main_entrance_description = "You have now entered the Main Entrance!"

    main_entrance_top_room = "Great Hall"
    main_entrance_bottom_room = "None"

    main_entrance = Location(Canvas(root, width=window_width,
        height=window_height, bg="wheat2"), main_entrance_description,
        main_entrance_top_room, main_entrance_bottom_room)

    main_entrance.canvas.create_rectangle(0, upper_door_boundary, 30,
        lower_door_boundary, fill="wheat1")

    #Making the walls
    right_wall = main_entrance.canvas.create_rectangle(window_width, 0,
                                window_width + 10, window_height, fill="white")
    left_wall = main_entrance.canvas.create_rectangle(-10, 0, 0, window_height,
                                                                fill="white")
    top_wall_left = main_entrance.canvas.create_rectangle(0, 0,
                                left_door_boundary, 0, fill="white")
    top_wall_right = main_entrance.canvas.create_rectangle(right_door_boundary,
                    0, window_width, 0, fill="white")
    bottom_wall = main_entrance.canvas.create_rectangle(0, window_height,
                                    window_width, window_height, fill="white")

    locations_dict["Main Entrance"] = main_entrance

    #Return the completed dictionary of locations
    return locations_dict

#########################################################################
#########################################################################
#########################################################################
