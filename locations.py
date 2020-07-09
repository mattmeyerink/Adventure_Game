
# Program written and maintained by Matthew Meyerink

# File containing class definition for locations

from tkinter import *
from utility import *

class Location:

    def __init__(self, canvas, room_description, top_room, bottom_room,
        left_room, right_room):

        self.canvas = canvas
        self.room_description = room_description
        self.top_room = top_room
        self.bottom_room = bottom_room
        self.left_room = left_room
        self.right_room = right_room


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
    great_hall_left_room = "None"
    great_hall_right_room = "None"

    great_hall = Location(Canvas(root, width=window_width,
        height=window_height, bg="wheat2"), great_hall_description,
        great_hall_top_room, great_hall_bottom_room, great_hall_left_room,
        great_hall_right_room)

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
    main_entrance_bottom_room = "Upstairs Corridor"
    main_entrance_right_room = "Hagrid's Hut"
    main_entrance_left_room = "Dungeons"

    main_entrance = Location(Canvas(root, width=window_width,
        height=window_height, bg="wheat2"), main_entrance_description,
        main_entrance_top_room, main_entrance_bottom_room,
        main_entrance_left_room, main_entrance_right_room)

    #Making the walls
    right_wall_top = main_entrance.canvas.create_rectangle(window_width,0,window_width+10,
                                            upper_door_boundary, fill="white")
    right_wall_bottom =  main_entrance.canvas.create_rectangle(window_width,
            lower_door_boundary,window_width+10,window_height, fill="white")
    left_wall_top = main_entrance.canvas.create_rectangle(-10,0,0,
                                            upper_door_boundary, fill="white")
    left_wall_bottom =  main_entrance.canvas.create_rectangle(-10,lower_door_boundary,0,
                                            window_height, fill="white")
    top_wall_left = main_entrance.canvas.create_rectangle(0, 0,
                                left_door_boundary, 0, fill="white")
    top_wall_right = main_entrance.canvas.create_rectangle(right_door_boundary,
                    0, window_width, 0, fill="white")
    bottom_wall_left = main_entrance.canvas.create_rectangle(0, window_height,
                                left_door_boundary, window_height, fill="white")
    bottom_wall_right = main_entrance.canvas.create_rectangle(right_door_boundary,
                    window_height, window_width, window_height, fill="white")

    #Add main entrance to the list of locations
    locations_dict["Main Entrance"] = main_entrance

    #########################################################################
    #########################################################################

    #Initialize the Dungeons
    dungeons_description = "You have now entered the Dungeons!"

    #Set adjacent rooms
    dungeons_top_room = "None"
    dungeons_left_room = "None"
    dungeons_right_room = "Main Entrance"
    dungeons_bottom_room = "Upstairs Corridor"

    dungeons = Location(Canvas(root, width=window_width, height=window_height,
        bg="dark grey"), dungeons_description, dungeons_top_room,
        dungeons_bottom_room, dungeons_left_room, dungeons_right_room)

    #Set the walls
    left_wall = dungeons.canvas.create_rectangle(-10, 0, 0, window_height,
                                                                fill="white")
    top_wall = dungeons.canvas.create_rectangle(0, -10,
                                                window_width, 0, fill="white")
    bottom_wall = dungeons.canvas.create_rectangle(0, window_height,
                                    window_width, window_height, fill="white")
    right_wall_top = dungeons.canvas.create_rectangle(window_width,0,window_width+10,
                                            upper_door_boundary, fill="white")
    right_wall_bottom =  dungeons.canvas.create_rectangle(window_width,
            lower_door_boundary,window_width+10,window_height, fill="white")

    #Add dungeons to the list of locations
    locations_dict["Dungeons"] = dungeons

    #########################################################################
    #########################################################################

    #Initialize Hagrid's Hut
    hagrids_hut_description = "You are now at Hagrid's Hut!"

    #Set adjacent rooms
    hagrids_hut_top_room = "None"
    hagrids_hut_left_room = "Main Entrance"
    hagrids_hut_right_room = "None"
    hagrids_hut_bottom_room = "None"

    hagrids_hut = Location(Canvas(root, width=window_width,
        height=window_height, bg="dark olive green"), hagrids_hut_description,
        hagrids_hut_top_room, hagrids_hut_bottom_room, hagrids_hut_left_room,
        hagrids_hut_right_room)

    #Making the walls
    top_wall = hagrids_hut.canvas.create_rectangle(0, -10,
                                                window_width, 0, fill="white")
    bottom_wall = hagrids_hut.canvas.create_rectangle(0, window_height,
                                    window_width, window_height, fill="white")
    right_wall = hagrids_hut.canvas.create_rectangle(window_width, 0,
                                window_width + 10, window_height, fill="white")
    left_wall_top = hagrids_hut.canvas.create_rectangle(-10,0,0,
                                            upper_door_boundary, fill="white")
    left_wall_bottom =  hagrids_hut.canvas.create_rectangle(-10,lower_door_boundary,0,
                                            window_height, fill="white")

    #Add Hagrids Hut to the list of locations
    locations_dict["Hagrid's Hut"] = hagrids_hut

    #########################################################################
    #########################################################################

    #Initialize upstairs corridor
    upstairs_corridor_description = "You have now entered the Upstairs Corridor!"

    #Set adjacent rooms
    upstairs_corridor_top_room = "Main Entrance"
    upstairs_corridor_left_room = "Room of Requirement"
    upstairs_corridor_right_room = "Ravenclaw Common Room"
    upstairs_corridor_bottom_room = "Gryffindor Common Room"

    upstairs_corridor = Location(Canvas(root, width=window_width,
        height=window_height, bg="wheat2"), upstairs_corridor_description,
        upstairs_corridor_top_room, upstairs_corridor_bottom_room,
        upstairs_corridor_left_room, upstairs_corridor_right_room)

    #Making the walls
    right_wall_top = upstairs_corridor.canvas.create_rectangle(window_width,0,window_width+10,
                                            upper_door_boundary, fill="white")
    right_wall_bottom =  upstairs_corridor.canvas.create_rectangle(window_width,
            lower_door_boundary,window_width+10,window_height, fill="white")
    left_wall_top = upstairs_corridor.canvas.create_rectangle(-10,0,0,
                                            upper_door_boundary, fill="white")
    left_wall_bottom =  upstairs_corridor.canvas.create_rectangle(-10,lower_door_boundary,0,
                                            window_height, fill="white")
    top_wall_left = upstairs_corridor.canvas.create_rectangle(0, 0,
                                left_door_boundary, 0, fill="white")
    top_wall_right = upstairs_corridor.canvas.create_rectangle(right_door_boundary,
                    0, window_width, 0, fill="white")
    bottom_wall_left = upstairs_corridor.canvas.create_rectangle(0, window_height,
                                left_door_boundary, window_height, fill="white")
    bottom_wall_right = upstairs_corridor.canvas.create_rectangle(right_door_boundary,
                    window_height, window_width, window_height, fill="white")

    #Add upstairs corridor to locations list
    locations_dict["Upstairs Corridor"] = upstairs_corridor

    #########################################################################
    #########################################################################

    #Initialize the Room of Requirement
    room_requirement_description = "You have now entered the Room of Requirement!"

    #Set adjacent rooms
    room_requirement_top_room = "None"
    room_requirement_left_room = "None"
    room_requirement_right_room = "Upstairs Corridor"
    room_requirement_bottom_room = "None"

    room_requirement = Location(Canvas(root, width=window_width,
        height=window_height, bg="burlywood4"), room_requirement_description,
        room_requirement_top_room, room_requirement_bottom_room,
        room_requirement_left_room, room_requirement_right_room)

    #Making the walls
    left_wall = room_requirement.canvas.create_rectangle(-10, 0, 0, window_height,
                                                                fill="white")
    top_wall = room_requirement.canvas.create_rectangle(0, -10,
                                                window_width, 0, fill="white")
    bottom_wall = room_requirement.canvas.create_rectangle(0, window_height,
                                    window_width, window_height, fill="white")
    right_wall_top = room_requirement.canvas.create_rectangle(window_width,0,window_width+10,
                                            upper_door_boundary, fill="white")
    right_wall_bottom =  room_requirement.canvas.create_rectangle(window_width,
            lower_door_boundary,window_width+10,window_height, fill="white")

    #Add room of requirement to the list of locations
    locations_dict["Room of Requirement"] = room_requirement

    #########################################################################
    #########################################################################

    #Initialize Ravenclaw Common Room
    ravenclaw_common_room_description = "You have now entered the Ravenclaw Common Room!"

    #Set Adjacent rooms
    ravenclaw_top_room = "None"
    ravenclaw_left_room = "Upstairs Corridor"
    ravenclaw_right_room = "None"
    ravenclaw_bottom_room = "None"

    ravenclaw_common_room = Location(Canvas(root, width=window_width,
        height=window_height, bg="LightBlue3"), ravenclaw_common_room_description,
        ravenclaw_top_room, ravenclaw_bottom_room, ravenclaw_left_room,
        ravenclaw_right_room)

    #Making the walls
    top_wall = ravenclaw_common_room.canvas.create_rectangle(0, -10,
                                                window_width, 0, fill="white")
    bottom_wall = ravenclaw_common_room.canvas.create_rectangle(0, window_height,
                                    window_width, window_height, fill="white")
    right_wall = ravenclaw_common_room.canvas.create_rectangle(window_width, 0,
                                window_width + 10, window_height, fill="white")
    left_wall_top = ravenclaw_common_room.canvas.create_rectangle(-10,0,0,
                                            upper_door_boundary, fill="white")
    left_wall_bottom =  ravenclaw_common_room.canvas.create_rectangle(-10,lower_door_boundary,0,
                                            window_height, fill="white")

    #Add ravenclaw common room to list of locations
    locations_dict["Ravenclaw Common Room"] = ravenclaw_common_room

    #########################################################################
    #########################################################################

    #Initialize Gryffindor Common Room
    gryffindor_common_room_description = "You have now entered the Gryffindor Common Room!"

    #Set Adjacent Rooms
    gryffindor_top_room = "Upstairs Corridor"
    gryffindor_left_room = "None"
    gryffindor_right_room = "None"
    gryffindor_bottom_room = "None"

    gryffindor_common_room = Location(Canvas(root, width=window_width,
        height=window_height, bg="firebrick1"), gryffindor_common_room_description,
        gryffindor_top_room, gryffindor_bottom_room, gryffindor_left_room,
        gryffindor_right_room)

    #Setting up the walls
    bottom_wall = gryffindor_common_room.canvas.create_rectangle(0, window_height,
                                    window_width, window_height, fill="white")
    right_wall = gryffindor_common_room.canvas.create_rectangle(window_width, 0,
                                window_width + 10, window_height, fill="white")
    left_wall = gryffindor_common_room.canvas.create_rectangle(-10, 0, 0, window_height,
                                                                fill="white")
    top_wall_left = gryffindor_common_room.canvas.create_rectangle(0, 0,
                                left_door_boundary, 0, fill="white")
    top_wall_right = gryffindor_common_room.canvas.create_rectangle(right_door_boundary,
                    0, window_width, 0, fill="white")

    #Add Gryffindor Common Room to locations list
    locations_dict["Gryffindor Common Room"] = gryffindor_common_room

    #########################################################################
    #########################################################################

    #Return the completed dictionary of locations
    return locations_dict

#########################################################################
#########################################################################
#########################################################################
