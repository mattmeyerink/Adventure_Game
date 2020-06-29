
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

    #Function to place the initial screen including the location, inventory,
    #message
    def initial_place(self):

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


    def place_screen(self):
        self.screen.place(anchor=NW)

    #function to update the message
    def place_message(self):
        self.message_canvas.create_text(window_width/2,
            (frame_height-window_height)/2, text=self.message,
            font=("Cochin", 20))

    def restart_screen(self):

        # Reprint the hero, items, enemies on the new screen
        self.hero = Hero(self.screen)
        print_enemies(self.current_location, self.screen, self.enemies)
        print_items(self.current_location, self.screen, self.items)

        #Set up the movement keys
        self.root.bind("d", self.hero.move_right)
        self.root.bind("a", self.hero.move_left)
        self.root.bind("s", self.hero.move_forward)
        self.root.bind("w", self.hero.move_backward)

        #Set up interaction and exit buttons
        self.root.bind("i", self.item_interaction)
        self.root.bind("e", self.change_locations)

        #Set up attack button
        self.root.bind("f", self.attack_enemy)

    #########################################################################
    #########################################################################
    #########################################################################

    #Function to add an item to the inventory
    def pick_up_item(self, item):

        item.picked_up = True
        self.inventory.append(item.name)
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

        #DELETE ME, FOR TESTING ONLY

        for i in range(len(self.items)):

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

    #Change the screen when the character exits a room
    def change_locations(self, event):

        # Bottom door Range
        x_door_bottom_boundary = (self.hero.x_position > left_door_boundary and
                                    self.hero.x_position < right_door_boundary)
        y_door_bottom_boundary = self.hero.y_position >  window_height
        bottom_door = x_door_bottom_boundary and y_door_bottom_boundary

        # Top door Range
        x_door_top_boundary = (self.hero.x_position > left_door_boundary and
                                    self.hero.x_position < right_door_boundary)
        y_door_top_boundary = self.hero.y_position < 0
        top_door = x_door_top_boundary and y_door_top_boundary

        # Left Door Range
        x_door_left_boundary = self.hero.x_position < 0
        y_door_left_boundary = (self.hero.y_position > upper_door_boundary and
                                    self.hero.y_position < lower_door_boundary)
        left_door = x_door_left_boundary and y_door_left_boundary

        # Right Door Range
        x_door_right_boundary = self.hero.x_position > window_width
        y_door_right_boundary = (self.hero.y_position > upper_door_boundary and
                                    self.hero.y_position < lower_door_boundary)
        right_door = x_door_right_boundary and y_door_right_boundary

        if (bottom_door):

            # Reinitialize locations
            self.locations = add_locations(self.root)

            # Reset the screen and place the screen
            self.screen = self.locations[
                    self.locations[self.current_location].bottom_room].canvas
            self.place_screen()

            # Reset the current location
            self.current_location = self.locations[
                                            self.current_location].bottom_room

            # Print the hero, items, and enemies to the new screen
            self.hero = Hero(self.screen)
            print_enemies(self.current_location, self.screen, self.enemies)
            print_items(self.current_location, self.screen, self.items)

            # Update the message
            self.message_canvas.delete('all')
            self.message = self.locations[self.current_location].room_description
            self.place_message()

            #Set up the movement keys
            self.root.bind("d", self.hero.move_right)
            self.root.bind("a", self.hero.move_left)
            self.root.bind("s", self.hero.move_forward)
            self.root.bind("w", self.hero.move_backward)

            #Set up interaction and exit buttons
            self.root.bind("i", self.item_interaction)
            self.root.bind("e", self.change_locations)

            #Set up attack button
            self.root.bind("f", self.attack_enemy)

        elif (top_door):

            # Reinitialize locations
            self.locations = add_locations(self.root)

            # Reset the screen and place the screen
            self.screen = self.locations[
                self.locations[self.current_location].top_room].canvas
            self.place_screen()

            # Reset the current location
            self.current_location = self.locations[
                                                self.current_location].top_room

            # Reprint the hero, items, enemies on the new screen
            self.hero = Hero(self.screen)
            print_enemies(self.current_location, self.screen, self.enemies)
            print_items(self.current_location, self.screen, self.items)

            # Update the message
            self.message_canvas.delete('all')
            self.message = self.locations[self.current_location].room_description
            self.place_message()

            #Set up the movement keys
            self.root.bind("d", self.hero.move_right)
            self.root.bind("a", self.hero.move_left)
            self.root.bind("s", self.hero.move_forward)
            self.root.bind("w", self.hero.move_backward)

            #Set up interaction and exit buttons
            self.root.bind("i", self.item_interaction)
            self.root.bind("e", self.change_locations)

            #Set up attack button
            self.root.bind("f", self.attack_enemy)

        elif (left_door):

             # Reinitialize locations
            self.locations = add_locations(self.root)

             # Reset the screen and place the screen
            self.screen = self.locations[
                 self.locations[self.current_location].left_room].canvas
            self.place_screen()

             # Reset the current location
            self.current_location = self.locations[
                                                 self.current_location].left_room

             # Reprint the hero, items, enemies on the new screen
            self.hero = Hero(self.screen)
            print_enemies(self.current_location, self.screen, self.enemies)
            print_items(self.current_location, self.screen, self.items)

             # Update the message
            self.message_canvas.delete('all')
            self.message = self.locations[self.current_location].room_description
            self.place_message()

             #Set up the movement keys
            self.root.bind("d", self.hero.move_right)
            self.root.bind("a", self.hero.move_left)
            self.root.bind("s", self.hero.move_forward)
            self.root.bind("w", self.hero.move_backward)

             #Set up interaction and exit buttons
            self.root.bind("i", self.item_interaction)
            self.root.bind("e", self.change_locations)

             #Set up attack button
            self.root.bind("f", self.attack_enemy)

        elif (right_door):

             # Reinitialize locations
            self.locations = add_locations(self.root)

             # Reset the screen and place the screen
            self.screen = self.locations[
                 self.locations[self.current_location].right_room].canvas
            self.place_screen()

             # Reset the current location
            self.current_location = self.locations[
                                                 self.current_location].right_room

             # Reprint the hero, items, enemies on the new screen
            self.hero = Hero(self.screen)
            print_enemies(self.current_location, self.screen, self.enemies)
            print_items(self.current_location, self.screen, self.items)

             # Update the message
            self.message_canvas.delete('all')
            self.message = self.locations[self.current_location].room_description
            self.place_message()

             #Set up the movement keys
            self.root.bind("d", self.hero.move_right)
            self.root.bind("a", self.hero.move_left)
            self.root.bind("s", self.hero.move_forward)
            self.root.bind("w", self.hero.move_backward)

             #Set up interaction and exit buttons
            self.root.bind("i", self.item_interaction)
            self.root.bind("e", self.change_locations)

             #Set up attack button
            self.root.bind("f", self.attack_enemy)


    #########################################################################
    #########################################################################
    #########################################################################

    #Function to carry out the enemy battle
    def enemy_battle(self, enemy):
        if enemy.can_kill(self.inventory):

            enemy.is_destroyed = True

            # Reinitialize locations
            self.locations = add_locations(self.root)
            self.place_screen()

            #self.restart_screen()

            # Update the message
            self.message_canvas.delete('all')
            self.message = enemy.name + " has been defeated!"
            self.place_message()

        else:

            # Update the message
            self.message_canvas.delete('all')
            self.message = "You dont have what it takes to win this fight yet!"
            self.place_message()

    #Function if the hero runs away from the enemy
    def ran_away(self):

        # Update the message
        self.message_canvas.delete('all')
        self.message = "Be better next time"
        self.place_message()

    # Function to handle enemy interaction
    def attack_enemy(self, event):

        for i in self.enemies:

            #Check if item is within the x_range
            x_lower_bound = self.hero.x_position > (self.enemies[i].x_position -
                (3 * character_size))
            x_upper_bound = self.hero.x_position < (self.enemies[i].x_position +
                (3 * character_size))
            x_range = x_lower_bound and x_upper_bound

            #Check if the item is within the y_range
            y_lower_bound = self.hero.y_position > (self.enemies[i].y_position -
                                                        (3 * character_size))
            y_upper_bound = self.hero.y_position < (self.enemies[i].y_position +
                                                        (3 * character_size))
            y_range = y_lower_bound and y_upper_bound

            #Check if the item is within range
            within_range = x_range and y_range

            #Branch if the person is within the range
            if (within_range and self.enemies[i].location
                                                    == self.current_location):

                #Reset the game message, clear the canvas, and put the message
                #On the canvas
                self.message_canvas.delete('all')
                self.message =  ("Would you like to duel " + self.enemies[i].name
                    + " (y/n)")
                self.place_message()

                #Ensure the y/n keys are unbound before using them
                self.root.unbind_all("y")
                self.root.unbind_all("n")
                self.root.bind("y", lambda event, arg1=self.enemies[i]:
                    self.enemy_battle(arg1))
                self.root.bind("n", self.ran_away)

            else:
                self.message_canvas.delete('all')
                self.message = "No enemy here. Keep looking!\n"
                self.place_message()

#Function to run a game using the game class
def start_game(root):

    #Initialize an instance of the game
    game = Game(root)

    #Add the enemies and items in the current location to the screen
    print_enemies(game.current_location, game.screen, game.enemies)
    print_items(game.current_location, game.screen, game.items)

    #Print the starting room
    game.initial_place()

    #Print the message
    game.place_message()

    #Set up the movement keys
    root.bind("d", game.hero.move_right)
    root.bind("a", game.hero.move_left)
    root.bind("s", game.hero.move_forward)
    root.bind("w", game.hero.move_backward)

    #Set up interaction and exit buttons
    root.bind("i", game.item_interaction)
    root.bind("e", game.change_locations)

    #Set up attack button
    root.bind("f", game.attack_enemy)
