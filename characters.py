
#Program written and maintained by Matthew Meyerink

#File containing class definitions for all characters

class Enemy:

    def __init__(self, name, hp, location, spell):
        self.name = name
        self.hp = hp
        self.location = location
        self.spell = spell

    def is_alive(self)
        return self.hp > 0

class Hero:

    hp = 250

    def __init__(self, name, spells):
        self.name = name
        self.spells = spells

    def is_alive(self):
        return self.hp > 0
