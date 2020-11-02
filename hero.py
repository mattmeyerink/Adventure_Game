"""
Contains the hero class for the game that handles hero attributes and 
hero movement.
"""
from tkinter import *
from utility import *


class Hero:
    """Defines a hero in the adventure game."""
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

        self.initial_overlap = self.canvas.find_overlapping(self.x1,
                                                    self.y1, self.x2, self.y2)

    def move_right(self, event):
        """Moves the hero right on screen."""
        self.canvas.move(self.widget, movement_amount, 0)

        # Determine the new hero coordinates
        x1, y1, x2, y2 = self.canvas.coords(self.widget)

        # Undo the movement if it causes overlap
        if (not self.canvas.find_overlapping(x1, y1, x2, y2) ==
                                                        self.initial_overlap):
            self.canvas.move(self.widget, -movement_amount, 0)
            x1, y1, x2, y2 = self.canvas.coords(self.widget)

        # Update the position of the character
        self.x_position = x1 + character_size
        self.y_position = y1 + character_size

    def move_left(self, event):
        """Moves the hero left on the screen."""
        self.canvas.move(self.widget, -movement_amount, 0)

        # Determine the new hero coordinates
        x1, y1, x2, y2 = self.canvas.coords(self.widget)

        # Undo the movement if it causes overlap
        if (not self.canvas.find_overlapping(x1, y1, x2, y2) ==
                                                        self.initial_overlap):
            self.canvas.move(self.widget, movement_amount, 0)
            x1, y1, x2, y2 = self.canvas.coords(self.widget)

        # Update the position of the character
        self.x_position = x1 + character_size
        self.y_position = y1 + character_size

    def move_forward(self, event):
        """Moves the hero forward on the screen."""
        self.canvas.move(self.widget, 0, movement_amount)

        # Determine the new hero coordinates
        x1, y1, x2, y2 = self.canvas.coords(self.widget)

        # Undo the movement if it causes overlap
        if (not self.canvas.find_overlapping(x1, y1, x2, y2) ==
                                                        self.initial_overlap):
            self.canvas.move(self.widget, 0, -movement_amount)
            x1, y1, x2, y2 = self.canvas.coords(self.widget)

        # Update the position of the character
        self.x_position = x1 + character_size
        self.y_position = y1 + character_size

    def move_backward(self, event):
        """Moves the hero backward on the screen."""
        self.canvas.move(self.widget, 0, -movement_amount)

        # Determine the new hero coordinates
        x1, y1, x2, y2 = self.canvas.coords(self.widget)

        # Undo the movement if it causes overlap
        if (not self.canvas.find_overlapping(x1, y1, x2, y2) ==
                                                        self.initial_overlap):
            self.canvas.move(self.widget, 0, movement_amount)
            x1, y1, x2, y2 = self.canvas.coords(self.widget)

        # Update the position of the character
        self.x_position = x1 + character_size
        self.y_position = y1 + character_size
