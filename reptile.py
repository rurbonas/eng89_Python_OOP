# Create reptile class to inherit Animal class

from animal import Animal

class Reptile(Animal): # inheriting from Animal class
    def __init__(self):
        super().__init__() # super is used to inherit everything from the parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chamber = [3, 4]

    def seek_heat(self):
        return "It's chilly, go look for a sunny spot."

    def hunt(self):
        return "Keep working hard to find food."

    def use_venom(self):
        return "If I have it, I will use it."

# Create an object of reptile class
smart_reptile = Reptile()
print(smart_reptile.breath()) # Breath method is inherited from Animal class
print(smart_reptile.hunt()) # Hunt method is a Reptile class