
# Program written and maintained by Matthew Meyerink

# File containing the setup for the game. Sets up the game class that calls
# other classes as well as the start_game function that actually runs
# the game

from tkinter import *
from locations import *
from characters import *

class Game:

    def __init__(self, root):

        self.root = root
        self.locations = add_locations(self.root)
        #Current canvas
        self.screen = self.locations["Great Hall"].canvas

        #self.hero = Hero(self.root)
        #self.enemies = add_enemies(self.screen)

        #Current canvas
        self.screen = self.locations["Great Hall"].canvas


#Function to run a game using the game class
def start_game(root):

    #Initialize an instance of the game
    game = Game(root)

    game.screen.pack()
