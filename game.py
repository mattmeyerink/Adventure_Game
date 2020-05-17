
# Program written and maintained by Matthew Meyerink

# File containing the setup for the game. Sets up the game class that calls
# other classes as well as the start_game function that actually runs
# the game

from tkinter import *
from locations import *
from enemies import *
from hero import *
from items import *

class Game:

    def __init__(self, root):

        #Main class variables
        self.root = root
        self.locations = add_locations(self.root)
        self.enemies = add_enemies()
        self.current_location = "Great Hall"
        self.screen = self.locations["Great Hall"].canvas
        self.hero = Hero(self.screen)
        self.items = add_items()

        #Define message and inventory canvas
        self.message_canvas = Canvas(self.root, width=window_width,
            height=frame_height - window_height, bg="white")
        self.message = ("Welcome to the Hogwarts! I think you will have a great" +
            " time. Much magic awaits you \nin these hallowed halls!")
        self.inventory_canvas = Canvas(self.root, width=frame_width-window_width,
            height=frame_height, highlightcolor="black", bg="white")
        self.inventory = {}

    #Function to place the screen including the location, inventory, message
    def place_screen(self):

        #Place the main screen canvas
        self.screen.place(anchor=NW)

        #Place the message canvas
        self.message_canvas.place(x=0, y=frame_height*0.855)

        #Place the inventory title
        inventory_title = self.inventory_canvas.create_text(
            (frame_width - window_width)/2, frame_height/16, text="Inventory",
            font=("Cochin", 20))
        inventory_line = self.inventory_canvas.create_line(0,
            frame_height/8, frame_width - window_width, frame_height/8,
            dash=(5, ), fill="black")
        self.inventory_canvas.place(x=window_width, y=0)

    #function to update the message
    def place_message(self):
        self.message_canvas.create_text(window_width/2,
            (frame_height-window_height)/2, text=self.message,
            font=("Cochin", 20))

    # Handle the user interacting with an item
    # Print the item description, the option to pick it up, and add to inventory
    # if yes
    def item_interaction(self):

        for i in self.items:

            #Check if item is within the range of the hero
            x_range = (((hero.x_position - character_size) >= self.items[i]) or
                ((hero.x_position + character_size) <= self.items[i]))
            y_range = (((hero.y_position - character_size) >= self.items[i]) or
                ((hero.y_position + character_size) <= self.items[i]))
            within_range = x_range and y_range

            #Branch if the person is within the range
            if (within_range and self.item[i] == self.current_location):



#Function to run a game using the game class
def start_game(root):

    #Initialize an instance of the game
    game = Game(root)

    #Add the enemies and items in the current location to the screen
    print_enemies(game.current_location, game.screen, game.enemies)
    print_items(game.current_location, game.screen, game.items)

    #Print the starting room
    game.place_screen()

    #Print the message
    game.place_message()

    #Set up the movement keys
    root.bind("d", game.hero.move_right)
    root.bind("a", game.hero.move_left)
    root.bind("s", game.hero.move_forward)
    root.bind("w", game.hero.move_backward)
