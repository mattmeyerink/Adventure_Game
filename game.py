from locations import *

class Game:

    def __init__(self, root):
        #The main window that needs to be pased into the game
        self.root = root

        #Canvas for a location that will appear on the screen
        self.screen = great_hall.graphics

    #Changes the screen to a new location
    def change_location(self, location):
        return

    #Adjusts the position of the player on the screen
    def adjust_player_position(self):
        return

#Function to run a game using the game class
def start_game(game):
