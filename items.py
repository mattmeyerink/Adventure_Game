
#Program written and maintained by Matthew Meyerink

#File containing class definitions for Items and Horcruxes

class Item:

    def __init__(self, name, description, location):

        self.name = name
        self.description = description
        self.location = location

class Horcrux:

    killed_by = {'Basilisk Fang', 'Sword of Gryffindor'}

    def __init__(self, name, description, location):
        self.name = name
        self.description = description

    #Check if the weapon used kills the Horcrux
    def is_killed(self, weapon):
        return weapon in killed_by
