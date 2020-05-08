from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hogwarts Adventure")
root.geometry("600x400")

def in_progress():
    msg = messagebox.showinfo("Game", "Hogwarts Under Construction!")

#Main Menu Title
main_title = Label(root, text="Welcome to a Hogwarts Adventure!", justify=CENTER, font=("Helvetica",20,"bold"))
main_title.place(rely=0.25, relx=0.5, anchor=CENTER)

#Main Game Menu
game_button = Button(root, text="Start Game", justify=CENTER, command=in_progress)
game_button.place(rely=0.50, relx=0.5, anchor=CENTER)

quit_button = Button(root, text="Quit", justify=CENTER, command=root.destroy)
quit_button.place(rely=0.60, relx=0.5, anchor=CENTER)

root.mainloop()
