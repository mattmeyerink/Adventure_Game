
#Program written and maintained by Matthew Meyerink

#File containing class definition for locations

class Location:

    def __init__(self, name, description):

        self.name = name
        self.description = description

great_hall = Location("Great Hall", "Main hall at Hogwarts containing the four house " +
            "tables. Big feasts and daily meals occur here.")

gryf_common_room = Location("Gryffindor Common Room", "Gryffindor common room. " +
            "Many post quidditch parties and late night discussions occured here.")

shrieking_shack = Location("Shrieking_Shack", "Listed as the most haunted dwelling " +
            "in Britian. However it was built and utilized by Remus Lupin during his " +
            "werewolf transformations.")

forbidden_forest = Location("Forbidden Forest", "Strictly out of bounds to all students. " +
            "Except for detention where students will traverse the paths at night unsupervised.")
