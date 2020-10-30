"""Contains the Window class for the Adventure Game App."""
from tkinter import *
from tkinter import messagebox
from game import *
from utility import *


class Window:
    """
    This is a class to represent the GUI window. Game operations, 
    instances are utilized to within this class to display the game.
    """
    def __init__(self):
        """Initializes the Tkinter window with a the main menu."""
        self.root = Tk()
        self.root.title("Hogwarts Adventure")
        self.root.geometry(str(frame_width)+ "x" + str(frame_height))

        #Initialize the main title of the game
        self.main_title = Label(self.root, text="Welcome to a Hogwarts Adventure!",
            font=("Cochin", 40, "bold"))
        self.main_title.place(rely=0.25, relx=0.5, anchor=CENTER)

        #Initialize the game button
        self.game_button = Button(self.root, text="Start Game",
            font=("Cochin", 20, "bold"), justify=CENTER,
            padx=10, pady=10, command=self.run_game)
        self.game_button.place(rely=0.45, relx=0.5, anchor=CENTER)

        #Initialize quit button
        self.quit_button = Button(self.root, text="Quit", font=("Cochin", 20, "bold"),
            justify=CENTER, padx=10, pady=10, command=self.root.destroy)
        self.quit_button.place(rely=0.60, relx=0.5, anchor=CENTER)

    def start(self):
        """Begin displaying the game window."""
        self.root.mainloop()

    # Prints a pop up window that contains the game instructions
    def print_instructions(self):
        """
        Pop Up window displaying instructions when the instructions
        button is clicked
        """
        window = Tk()
        window.title("Instructions")
        window.geometry("700x550")

        # Display the main instructions for the title
        main_title = Label(window, text="Instructions", font=("Cochin", 30, "bold"),
            anchor=CENTER)
        main_title.pack()

        # Display the header of instructions list
        list1 = Label(window, text="Attempt to find and destroy all of the horcruxes " +
            "before attempting to destory\nLord Voldemort freeing the wizarding " +
            "world from his tyranny.\n"

            " View your current item inventory on the right" +
            " and any important messages\non the bottom\n",
            font=("Cochin", 20))
        list1.pack()

        # Display the title for instructions index
        list2 = Label(window, text="Index", font=("Cochin", 24, "bold"))
        list2.pack()

        # Display the index of different item/characters
        list3 = Label(window, text="Square = Magical Item\n" +
            "Black Circle = Lord Voldemort\n" +
            "Red Circle = Harry Potter\n" +
            "Other Circles = Horcruxes\n",
            font=("Cochin", 20))
        list3.pack()

        # Display the header for list of controls
        list4 = Label(window, text="Controls", font=("Cochin", 24, "bold"))
        list4.pack()

        # Display the list of commands
        list5 = Label(window, text="w = move forward\n" +
            "s = move backward\na = move left\nd = move right\ni = interact\ne = exit room\n" +
            "f = fight enemy",
            font=("Cochin", 20))
        list5.pack()

        # Run the instructions window
        window.mainloop()

    def run_game(self):
        """Runs the adventure game within the window."""
        # Get rid of all buttons from the menu screen
        self.main_title.destroy()
        self.game_button.destroy()
        self.quit_button.destroy()

        # Run the game function using created game instance
        start_game(self.root)

        # Initialize and place the instructions button
        self.insturctions_button = Button(self.root, text="Instructions",
            font=("Cochin", 20, "bold"), justify=CENTER, padx=42.5, pady=39,
            command=self.print_instructions)
        self.insturctions_button.place(relx=0.80, rely=0.85, anchor=NW)
