
# Creating a parrot Object
class Parrot:
    def __init__(self):
        age = 10
        self.name = 'Bob'  # put name in self
        self.color = 'white'
        species = 'X'
        # above we define the parrot attributes

    def singing(self):
        print('The parrot is singing')
        # Now access name from self
        print('My name is ', self.name, ' And the color is ', self.color)
        # this function represents a behavior

    def dancing(self):
        print('Parrot is dancing')
        # this function represents a behavior







