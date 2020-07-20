# Harry Potter Adventure Game

### Description

This project is my first try at producing a basic GUI. As a life long
Harry Potter fan I decided that I would attempt to make a basic game based
on the Wizarding World as imagined by JK Rowling. I decided to try to keep
the graphics simple to just get my feet wet with managing both the front end,
graphics side of things as well as the backend development.

In the game you are Harry Potter and you must traverse the castle of Hogwarts
and the accompanying grounds in order to locate and destroy all of Lord
Voldemort's horcruxes before finally battling Lord Voldemort.

### Technologies Used

#### Python

I am still getting comfortable with Python and its syntax after originally
learning C++ so I decided to push further in Python with this project.

#### Tkinter

This was my first experience programing a GUI so I decided to go with the built
in Python library Tkinter. While it is very basic I decided it fit my needs as
I did not want to make the interface complicated at all.

## Problems Encountered

The biggest problem I faced was file organization. Upon beginning the project I
was a little too excited and decided to just begin coding and to organize my
classes and file references as I go. While I knew that this was not the right
way to do it, I now know from experience that planning is VERY VERY important.
I wasted a lot of time dealing with circular references and realizing that I
had created my function within a file/class that was not going to work. While
I feel I was able to correct some of this, it took a significant amount of
time. Much more than if I had just sat down and invested several hours upfront
to decide what functions I needed and when I would need to access specific
data.

Moving forward I would first map out overall project goals on paper.
I would then create the necessary files and outlines of the classes and
functions before writing any code. This way I would know if I was accidentally
creating a circular reference before I had any code to rewrite.

Only once I had a backbone that would do everything that I needed the program
to do would I fill in the class and function definitions.

## File Map

#### utility.py

Contains global variable definitions for use throughout the files.

#### locations.py

Contains the Location Class that defines a the elements of a specific room in
the game. Also contains the following function definition.

- add_locations(root): Initializes and returns all of the locations in the game
in a dictionary that can be searched.

#### items.py

#### hero.py

#### enemies.py

Contains the Enemy Class Definition. The enemy class defines the traits of an
enemy (in this case a horcrux) as well as contains the following function
definition.

- can_kill(hero_inventory): Checks the items possessed by the hero to see if
they have the necessary item to kill the horcrux.

The file also contains the following function definitions relevant to enemies.

- add_enemies(): Creates the enemies for the game and returns them allowing
them to be saved and accessed later by each instance of the game.
- print_enemies(current_location, screen, enemies): Prints the enemies to the
screen that are located in the room the hero is currently in.

#### game.py

#### Window.py

Contains the Window Class Definition. This class defines the main window of the
game. It contains the following functions.

- start(): Starts the main loop of the Window
- print_instructions(): Prints the instruction window
- run_game(): Destroys the main tile menu and begins the game

#### start.py

Creates an instance of the window class and runs the start() function from the
window class.
