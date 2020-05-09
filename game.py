from tkinter import *
from locations import Location
from characters import Enemy

class Game:

    def __init__(self, root):
        #The main window that needs to be pased into the game
        self.root = root

        #Set up an instance of all of the locations
        self.locations = Location(self.root)

        #Set up an instance for all of the enemies
        self.enemies = Enemy(self.root)

        #Canvas for a location that will appear on the screen
        self.screen = self.locations.great_hall_canvas

    #Changes the screen to a new location
    def change_location(self, location):
        return

    #Adjusts the position of the player on the screen
    def adjust_player_position(self):
        return

#Function to run a game using the game class
def start_game(game):
    game.screen.pack()
