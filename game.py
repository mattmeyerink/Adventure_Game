"""
File containing the Game class. The Game class is an intance of the
Adventure game that maintains the characters, enemies, and items 
and controls what is displayed to the App window.
"""
from tkinter import *
from locations import *
from enemies import *
from hero import *
from items import *

class Game:
    """
    This is a class to represent the game itself. The class contains methods
    to manage items, characters, enemies in the game and the running of the
    game itself.
    """
    def __init__(self, root):
        """
        Initializes the game class. Contains reference to the root Tkinter
        window, a dictionary of location objects, a dictionary of enemy
        objects, the name of the current location, the current Tkinter
        canvas, the hero object, and a dictionary of items. 

        Additionally the game tracks the inventory canvas as well 
        as the messages canvas.
        """
        # Main class variables
        self.root = root
        self.locations = add_locations(self.root)
        self.enemies = add_enemies()
        self.current_location = "Great Hall"
        self.screen = self.locations[self.current_location].canvas
        self.hero = Hero(self.screen)
        self.items = add_items()

        # Define message for the game
        self.message_canvas = Canvas(self.root, width=window_width,
            height=frame_height - window_height, bg="white")
        self.message = ("Welcome to the Hogwarts! I think you will have a great" +
            " time. Much magic awaits you \nin these hallowed halls!")

        # Define the inventory for the game
        self.inventory_canvas = Canvas(self.root, width=frame_width-window_width,
            height=frame_height, highlightcolor="black", bg="white")
        self.inventory = []
        self.inventory_names = ""
        self.inventory_names_text = self.inventory_canvas.create_text(
            (frame_width - window_width)/2, frame_height/2,
            text= self.inventory_names, font=("Cochin", 14))

    def initial_place(self):
        """Function to initialize the game screen."""
        # Place the main screen canvas
        self.screen.place(anchor=NW)

        # Place the message canvas
        self.message_canvas.place(x=0, y=frame_height*0.855)

        # Place the inventory title
        inventory_title = self.inventory_canvas.create_text(
            (frame_width - window_width)/2, frame_height/16, text="Inventory",
            font=("Cochin", 20))
        inventory_line = self.inventory_canvas.create_line(0,
            frame_height/8, frame_width - window_width, frame_height/8,
            dash=(5, ), fill="black")
        self.inventory_canvas.place(x=window_width, y=0)

    def place_screen(self):
        """Place the current canvas."""
        self.screen.place(anchor=NW)

    def place_message(self):
        """Update the message displayed on the message canvas."""
        self.message_canvas.create_text(window_width/2,
            (frame_height-window_height)/2, text=self.message,
            font=("Cochin", 20))

    def restart_screen(self):
        """Rerenders the screen and re initialize the key bindings."""
        # Reprint the hero, items, enemies on the new screen
        self.hero = Hero(self.screen)
        print_enemies(self.current_location, self.screen, self.enemies)
        print_items(self.current_location, self.screen, self.items)

        # Set up the movement keys
        self.root.bind("d", self.hero.move_right)
        self.root.bind("a", self.hero.move_left)
        self.root.bind("s", self.hero.move_forward)
        self.root.bind("w", self.hero.move_backward)

        # Set up interaction and exit buttons
        self.root.bind("i", self.item_interaction)
        self.root.bind("e", self.change_locations)

        # Set up attack button
        self.root.bind("f", self.attack_enemy)

    def pick_up_item(self, item):
        """Allows hero to pick up item and add it to inventory."""
        item.picked_up = True

        # Update message
        self.message_canvas.delete('all')
        self.message = "Item added to inventory"
        self.place_message()

        # Update inventory
        self.inventory.append(item.name)
        self.inventory_names += "\n\n" + item.name
        self.inventory_canvas.itemconfig(self.inventory_names_text,
            text=self.inventory_names)

    def item_not_picked_up(self, event):
        """Alert player item not added to inventory."""
        self.message_canvas.delete('all')
        self.message = "Item not added to inventory"
        self.place_message()

    # Handle the user interacting with an item
    # Print the item description, the option to pick it up, and add to inventory
    # if yes
    def item_interaction(self, event):
        """
        Handle the user interacting with an item.
        Prints the items description, and displays option to pick it 
        up or not. Adds item to inventory if yes, prints failed message
        if no.
        """
        # Check if any item in proximity of hero
        for i in range(len(self.items)):
            # Check if item is within the x_range of hero
            x_lower_bound = self.hero.x_position > (self.items[i].x_position -
                (3 * character_size))
            x_upper_bound = self.hero.x_position < (self.items[i].x_position +
                (3 * character_size))
            x_range = x_lower_bound and x_upper_bound

            # Check if the item is within the y_range of hero
            y_lower_bound = self.hero.y_position > (self.items[i].y_position -
                                                        (3 * character_size))
            y_upper_bound = self.hero.y_position < (self.items[i].y_position +
                                                        (3 * character_size))
            y_range = y_lower_bound and y_upper_bound

            # Check if the item is within range
            within_range = x_range and y_range

            # Branch if the person is within the range and in same room
            if (within_range and (self.items[i].location
                                                    == self.current_location)):

                # Reset the game message with pickup prompt
                self.message_canvas.delete('all')
                self.message = self.items[i].description + item_prompt
                self.place_message()

                # Ensure the y/n keys are unbound before using them
                self.root.unbind_all("y")
                self.root.unbind_all("n")
                self.root.bind("y", lambda event, arg1=self.items[i]:
                    self.pick_up_item(arg1))
                self.root.bind("n", self.item_not_picked_up)

                break

            else:
                # Push keep looking message
                self.message_canvas.delete('all')
                self.message = "Nothing to interact with here. Keep looking!\n"
                self.place_message()
    
    # TODO Refractor to combine chagne room functions to cleaner statement
    # TODO Add function for initializing keys (used multiple times)
    def change_locations(self, event):
        """Update the screen when the hero changes rooms."""
        # Set bottom door range
        x_door_bottom_boundary = (self.hero.x_position > left_door_boundary and
                                    self.hero.x_position < right_door_boundary)
        y_door_bottom_boundary = self.hero.y_position >  window_height
        bottom_door = x_door_bottom_boundary and y_door_bottom_boundary

        # Set top door range
        x_door_top_boundary = (self.hero.x_position > left_door_boundary and
                                    self.hero.x_position < right_door_boundary)
        y_door_top_boundary = self.hero.y_position < 0
        top_door = x_door_top_boundary and y_door_top_boundary

        # Set left door range
        x_door_left_boundary = self.hero.x_position < 0
        y_door_left_boundary = (self.hero.y_position > upper_door_boundary and
                                    self.hero.y_position < lower_door_boundary)
        left_door = x_door_left_boundary and y_door_left_boundary

        # Set right door range
        x_door_right_boundary = self.hero.x_position > window_width
        y_door_right_boundary = (self.hero.y_position > upper_door_boundary and
                                    self.hero.y_position < lower_door_boundary)
        right_door = x_door_right_boundary and y_door_right_boundary

        # Exit the bottom door if bottom door true
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

            # Set up the movement keys
            self.root.bind("d", self.hero.move_right)
            self.root.bind("a", self.hero.move_left)
            self.root.bind("s", self.hero.move_forward)
            self.root.bind("w", self.hero.move_backward)

            # Set up interaction and exit buttons
            self.root.bind("i", self.item_interaction)
            self.root.bind("e", self.change_locations)

            # Set up attack button
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

            # Set up the movement keys
            self.root.bind("d", self.hero.move_right)
            self.root.bind("a", self.hero.move_left)
            self.root.bind("s", self.hero.move_forward)
            self.root.bind("w", self.hero.move_backward)

            # Set up interaction and exit buttons
            self.root.bind("i", self.item_interaction)
            self.root.bind("e", self.change_locations)

            # Set up attack button
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

            # Set up the movement keys
            self.root.bind("d", self.hero.move_right)
            self.root.bind("a", self.hero.move_left)
            self.root.bind("s", self.hero.move_forward)
            self.root.bind("w", self.hero.move_backward)

             # Set up interaction and exit buttons
            self.root.bind("i", self.item_interaction)
            self.root.bind("e", self.change_locations)

             # Set up attack button
            self.root.bind("f", self.attack_enemy)

    def enemy_battle(self, enemy):
        """Function to battle enemy."""
        # Destroy enemy if correct item in inventory
        if enemy.can_kill(self.inventory):

            enemy.is_destroyed = True

            # Reinitialize locations
            self.locations = add_locations(self.root)
            self.place_screen()

            # Update the message
            self.message_canvas.delete('all')
            self.message = enemy.name + " has been defeated!"
            self.place_message()

        # Special case to destroy Voldemort if all else destroyed
        elif enemy.name == "Lord Voldemort":

            horcruxes_left = False

            for i in self.enemies:
                if (self.enemies[i].is_destroyed == False and
                                self.enemies[i].name != "Lord Voldemort"):
                    horcruxes_left = True

            if horcruxes_left == False:
                enemy.is_destroyed = True

                # Reinitialize locations
                self.locations = add_locations(self.root)
                self.place_screen()

                # Update the message
                self.message_canvas.delete('all')
                self.message = enemy.name + " has been defeated!"
                self.place_message()

        # Update message to say battle not won
        else:
            # Update the message
            self.message_canvas.delete('all')
            self.message = "You dont have what it takes to win this fight yet!"
            self.place_message()

    def ran_away(self):
        """Updates message if hero runs from enemy."""
        self.message_canvas.delete('all')
        self.message = "Be better next time"
        self.place_message()

    def attack_enemy(self, event):
        """Sense/handle interaction with enemy."""
        for i in self.enemies:
            # Check if item is within the x_range of hero
            x_lower_bound = self.hero.x_position > (self.enemies[i].x_position -
                (3 * character_size))
            x_upper_bound = self.hero.x_position < (self.enemies[i].x_position +
                (3 * character_size))
            x_range = x_lower_bound and x_upper_bound

            # Check if the item is within the y_range of hero
            y_lower_bound = self.hero.y_position > (self.enemies[i].y_position -
                                                        (3 * character_size))
            y_upper_bound = self.hero.y_position < (self.enemies[i].y_position +
                                                        (3 * character_size))
            y_range = y_lower_bound and y_upper_bound

            # Check if the item is within range of hero
            within_range = x_range and y_range

            # Branch if the person is within the range and in same room
            if (within_range and self.enemies[i].location
                                                    == self.current_location):

                # Reset the message to display duel/no duel option
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

                break
            
            # Update message if no enemy in range
            else:
                self.message_canvas.delete('all')
                self.message = "No enemy here. Keep looking!\n"
                self.place_message()

def start_game(root):
    """
    Function to initilize and run an instance of the Adventure Game.
    Takes the root as input to know where to output the game.
    """

    # Initialize an instance of the game
    game = Game(root)

    # Add the enemies and items in the current location to the screen
    print_enemies(game.current_location, game.screen, game.enemies)
    print_items(game.current_location, game.screen, game.items)

    #Print the starting room
    game.initial_place()

    # Print the message
    game.place_message()

    # Set up the movement keys
    root.bind("d", game.hero.move_right)
    root.bind("a", game.hero.move_left)
    root.bind("s", game.hero.move_forward)
    root.bind("w", game.hero.move_backward)

    # Set up interaction and exit buttons
    root.bind("i", game.item_interaction)
    root.bind("e", game.change_locations)

    # Set up attack button
    root.bind("f", game.attack_enemy)
