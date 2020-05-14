
# Program written and maintained by Matthew Meyerink

# File containing the setup for the game. Sets up the game class that calls
# other classes as well as the start_game function that actually runs
# the game

from tkinter import *
from locations import *
from enemies import *
from hero import *

class Game:

    def __init__(self, root):

        self.root = root
        self.locations = add_locations(self.root)
        self.enemies = add_enemies()
        self.current_location = "Great Hall"
        self.screen = self.locations["Great Hall"].canvas
        self.hero = Hero(self.screen)


#Function to run a game using the game class
def start_game(root):

    #Initialize an instance of the game
    game = Game(root)

    #Add the enemies in the current location to the screen
    print_enemies(game.current_location, game.screen, game.enemies)

    #Print the starting room
    game.screen.pack()

    #Set up the movement keys
    root.bind("d", game.hero.move_right)
    root.bind("a", game.hero.move_left)
    root.bind("s", game.hero.move_forward)
    root.bind("w", game.hero.move_backward)
