from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x400")

def in_progress():
    msg = messagebox.showinfo("Game", "Hogwarts Under Construction!")

#Main Menu Title
main_title = Label(root, text="Welcome to a Hogwarts Adventure!", justify=CENTER)
main_title.grid(ipady=50)

#Main Game Menu
game_button = Button(root, text="Start Game", justify=CENTER, command=in_progress)
game_button.grid(pady=50)
quit_button = Button(root, text="Quit", justify=CENTER, command=root.destroy)
quit_button.grid(pady=50)

root.mainloop()
