
#Program written and maintained by Matthew Meyerink

#File containing class definition for locations

from tkinter import *
from menu import *

class Location:

    def __init__(self, name, description, graphics):

        self.name = name
        self.description = description
        self.graphics = graphics

#Testing defining a canvas for a specific location on the map
great_hall_image = Canvas(root, width=800, height=600)

great_hall = Location("Great Hall", "Main hall at Hogwarts containing the four house " +
            "tables. Big feasts and daily meals occur here.")

gryf_common_room = Location("Gryffindor Common Room", "Gryffindor common room. " +
            "Many post quidditch parties and late night discussions occured here.")

shrieking_shack = Location("Shrieking_Shack", "Listed as the most haunted dwelling " +
            "in Britian. However it was built and utilized by Remus Lupin during his " +
            "werewolf transformations.")

forbidden_forest = Location("Forbidden Forest", "Strictly out of bounds to all students. " +
            "Except for detention where students will traverse the paths at night unsupervised.")
