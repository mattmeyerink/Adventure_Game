
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
        self.screen = self.locations[self.current_location].canvas
        self.hero = Hero(self.screen)
        self.items = add_items()

        #Define message for the game
        self.message_canvas = Canvas(self.root, width=window_width,
            height=frame_height - window_height, bg="white")
        self.message = ("Welcome to the Hogwarts! I think you will have a great" +
            " time. Much magic awaits you \nin these hallowed halls!")

        #Define the inventory for the game
        self.inventory_canvas = Canvas(self.root, width=frame_width-window_width,
            height=frame_height, highlightcolor="black", bg="white")
        self.inventory = []
        self.inventory_names = ""
        self.inventory_names_text = self.inventory_canvas.create_text(
            (frame_width - window_width)/2, frame_height/2,
            text= self.inventory_names, font=("Cochin", 14))


    #########################################################################
    #########################################################################
    #########################################################################

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

    #########################################################################
    #########################################################################
    #########################################################################

    #Function to add an item to the inventory
    def pick_up_item(self, item):

        item.picked_up = True
        self.inventory.append(item)
        self.message_canvas.delete('all')
        self.message = "Item added to inventory"
        self.place_message()

        self.inventory_names += "\n\n" + item.name
        self.inventory_canvas.itemconfig(self.inventory_names_text,
            text=self.inventory_names)

    #Print message item not added to inventory
    def item_not_picked_up(self, event):
        self.message_canvas.delete('all')
        self.message = "Item not added to inventory"
        self.place_message()

    #########################################################################
    #########################################################################
    #########################################################################

    # Handle the user interacting with an item
    # Print the item description, the option to pick it up, and add to inventory
    # if yes
    def item_interaction(self, event):

        for i in self.items:

            #Check if item is within the x_range
            x_lower_bound = self.hero.x_position > (self.items[i].x_position -
                (3 * character_size))
            x_upper_bound = self.hero.x_position < (self.items[i].x_position +
                (3 * character_size))
            x_range = x_lower_bound and x_upper_bound

            #Check if the item is within the y_range
            y_lower_bound = self.hero.y_position > (self.items[i].y_position -
                                                        (3 * character_size))
            y_upper_bound = self.hero.y_position < (self.items[i].y_position +
                                                        (3 * character_size))
            y_range = y_lower_bound and y_upper_bound

            #Check if the item is within range
            within_range = x_range and y_range

            #Branch if the person is within the range
            if (within_range and self.items[i].location
                                                    == self.current_location):

                #Reset the game message, clear the canvas, and put the message
                #On the canvas
                self.message_canvas.delete('all')
                self.message = self.items[i].description + item_prompt
                self.place_message()

                #Ensure the y/n keys are unbound before using them
                self.root.unbind_all("y")
                self.root.unbind_all("n")
                self.root.bind("y", lambda event, arg1=self.items[i]:
                    self.pick_up_item(arg1))
                self.root.bind("n", self.item_not_picked_up)

            else:
                self.message_canvas.delete('all')
                self.message = "Nothing to interact with here. Keep looking!\n"
                self.place_message()


    #########################################################################
    #########################################################################
    #########################################################################

    
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
    root.bind("i", game.item_interaction)
