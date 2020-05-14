from tkinter import *
from utility import *

class Hero:

    def __init__(self, screen):

        self.variable = 1
        self.hero_color = "red"
        self.x_position = window_width / 2
        self.y_position = window_height * (3 / 4)
        self.canvas = screen

        self.x1 = self.x_position - character_size
        self.y1 = self.y_position - character_size

        self.x2 = self.x_position + character_size
        self.y2 = self.y_position + character_size

        self.widget =  self.canvas.create_oval(self.x1, self.y1,
                                        self.x2, self.y2, fill=self.hero_color)

    #Functions to move the hero right, left, forward, and backward
    def move_right(self, event):
        self.canvas.move(self.widget, movement_amount, 0)

    def move_left(self, event):
        self.canvas.move(self.widget, -movement_amount, 0)

    def move_forward(self, event):
        self.canvas.move(self.widget, 0, movement_amount)

    def move_backward(self, event):
        self.canvas.move(self.widget, 0, -movement_amount)
