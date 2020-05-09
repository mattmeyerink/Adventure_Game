
#Program written and maintained by Matthew Meyerink

#File containing class definition for locations

from tkinter import *

class Location:

    window_height = 600
    window_width = 800

    def __init__(self, root):

        self.root = root

        #Great Hall Data
        great_hall_image = PhotoImage(file="Great_Hall.gif")
        self.great_hall_canvas = Canvas(self.root, width=self.window_width, height=self.window_height)
        #First two inputs are placement of center of the image
        self.great_hall_canvas.create_image(self.window_width/2, self.window_height/2, anchor=CENTER, image=great_hall_image)
        self.great_hall_canvas.image = great_hall_image
