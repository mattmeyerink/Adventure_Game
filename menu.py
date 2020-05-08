from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hogwarts Adventure")
root.geometry("1200x800")

def start_game():
    main_title.destroy()
    game_button.destroy()
    quit_button.destroy()
    construction_message = Label(root, text="Working on the game!", font=("Cochin", 40, "bold"))
    construction_message.place(relx=0.5, rely=0.5, anchor=CENTER)

#Main Menu Title
main_title = Label(root, text="Welcome to a Hogwarts Adventure!", font=("Cochin", 40, "bold"))
main_title.place(rely=0.25, relx=0.5, anchor=CENTER)

#Main Game Menu
game_button = Button(root, text="Start Game", font=("Cochin", 20, "bold"), justify=CENTER, padx=10, pady=10, command=start_game)
game_button.place(rely=0.45, relx=0.5, anchor=CENTER)

quit_button = Button(root, text="Quit", font=("Cochin", 20, "bold"), justify=CENTER, padx=10, pady=10, command=root.destroy)
quit_button.place(rely=0.60, relx=0.5, anchor=CENTER)

root.mainloop()
