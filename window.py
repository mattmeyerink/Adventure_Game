from tkinter import *
from tkinter import messagebox
from game import *
from utility import *

class Window:

    def __init__(self):

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

    ##########################################################################
    ##########################################################################
    ##########################################################################


    # Start the window loop
    def start(self):
        self.root.mainloop()

    # Prints a pop up window that contains the game instructions
    def print_instructions(self):

        window = Tk()
        window.title("Instructions")
        window.geometry("700x550")

        main_title = Label(window, text="Instructions", font=("Cochin", 30, "bold"),
            anchor=CENTER)
        main_title.pack()

        list = Label(window, text="Attempt to find and destroy all of the horcruxes " +
            "before attempting to destory\nLord Voldemort freeing the wizarding " +
            "world from his tyranny.\n"

            " View your current item inventory on the right" +
            " and any important messages\non the bottom\n",
            font=("Cochin", 20))
        list.pack()

        list2 = Label(window, text="Index", font=("Cochin", 24, "bold"))
        list2.pack()

        list3 = Label(window, text="Square = Magical Item\n" +
            "Black Circle = Lord Voldemort\n" +
            "Red Circle = Harry Potter\n" +
            "Other Circles = Horcruxes\n",
            font=("Cochin", 20))
        list3.pack()

        list4 = Label(window, text="Controls", font=("Cochin", 24, "bold"))
        list4.pack()

        list5 = Label(window, text="w = move forward\n" +
            "s = move backward\na = move left\nd = move right\ni = interact\ne = exit room\n" +
            "f = fight enemy",
            font=("Cochin", 20))
        list5.pack()

        window.mainloop()

    # Function to start the game
    def run_game(self):

        #Get rid of all buttons on the screen
        self.main_title.destroy()
        self.game_button.destroy()
        self.quit_button.destroy()

        #Run the game function using created game instance
        start_game(self.root)

        #Initialize and place the instructions button
        self.insturctions_button = Button(self.root, text="Instructions",
            font=("Cochin", 20, "bold"), justify=CENTER, padx=42.5, pady=39,
            command=self.print_instructions)
        self.insturctions_button.place(relx=0.80, rely=0.85, anchor=NW)
