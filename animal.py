#Create animal class

class Animal:
    def __init__(self): # initialise with built in method called __init__(self) - self refers to current class
        # we declare attributes in our methods
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breath(self):
        return "Keep breathing to stay alive."

    def eat(self):
        return "Time to eat."

    def move(self):
        return "Move left or right to stay awake."

# We need to creat an objects of this class in order to be able to use methods
cat = Animal() # Creating an object of Animal class
print(cat.breath()) # The user doesn't need to worry about functionality, method breath is abstracted
