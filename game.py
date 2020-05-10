
# Program written and maintained by Matthew Meyerink

# File containing the setup for the game. Sets up the game class that calls
# other classes as well as the start_game function that actually runs
# the game

from tkinter import *
from locations import Location
from characters import *

class Game:

    def __init__(self, root):
        #The main window that needs to be pased into the game
        self.root = root

        #Set up button
        self.up_arrow = Button(self.root, text="^", padx=10,
            command=self.root.destroy)
        self.up_arrow.place(relx=0.85, rely=0.875)

        #Set right button
        self.right_arrow = Button(self.root, text=">", padx=10,
            command=self.root.destroy)
        self.right_arrow.place(relx=0.88, rely=0.90)

        #Set left button
        self.left_arrow = Button(self.root, text="<", padx=10,
            command=self.root.destroy)
        self.left_arrow.place(relx=0.82, rely=0.90)

        #Set back button
        self.back_arrow = Button(self.root, text="v", font=(30), padx=10,
            command=self.root.destroy)
        self.back_arrow.place(relx=0.85, rely=0.925)

        #Set up an instance of all of the locations
        self.locations = Location(self.root)

        #Set up an instance for all of the enemies
        self.enemies = Enemy(self.root)

        #Set up the hero
        self.hero = Hero(self.root)

        #Canvas for a location that will appear on the screen
        self.screen = self.locations.great_hall_canvas

    #Changes the screen to a new location
    def change_location(self, location):
        return true

    #Adjusts the position of the player on the screen
    def adjust_player_position(self):
        return true


#Function to run a game using the game class
def start_game(game):
    game.screen.place(relx=0.35, rely=0.5, anchor=CENTER)
