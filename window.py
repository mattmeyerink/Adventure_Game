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

    #Start the window loop
    def start(self):
        self.root.mainloop()

    #Function to start the game
    def run_game(self):

        #Get rid of all buttons on the screen
        self.main_title.destroy()
        self.game_button.destroy()
        self.quit_button.destroy()
        #Run the game function using created game instance
        start_game(self.root)
