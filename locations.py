
# Program written and maintained by Matthew Meyerink

# File containing class definition for locations

from tkinter import *

class Location:

    window_height = 600
    window_width = 800

    def __init__(self, root):

        self.root = root

        #Great Hall Data
        self.great_hall_canvas = Canvas(self.root, width=self.window_width,
            height=self.window_height, bg="wheat2")

        #Four house Tables
        self.great_hall_canvas.create_rectangle(100, 250, 175 , 500, fill="MistyRose4")
        self.great_hall_canvas.create_rectangle(275, 250, 350, 500, fill="MistyRose4")
        self.great_hall_canvas.create_rectangle(450, 250, 525, 500, fill="MistyRose4")
        self.great_hall_canvas.create_rectangle(625, 250, 700, 500, fill="MistyRose4")

        #High Table
        self.great_hall_canvas.create_rectangle(200, 50, 600, 125, fill="MistyRose4")

        #Lord Voldemort Graphics (Circle Radius of 20)
        self.great_hall_canvas.create_oval(380, 155, 420, 195, fill="black")
