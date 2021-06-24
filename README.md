# Python OOP

## What are the Pillars of Object Oriented Programming?

- **Abstraction**

    Applying abstraction means that each object should only expose a high-level mechanism for using it.
    This mechanism should hide internal implementation details. It should only reveal operations relevant for the other objects.

  
- **Inheritance**
  
   Inheritance helps us reuse the common logic and extract the unique logic into a separate class.
  
    It means that we create a (child) class by deriving from another (parent) class. This way, we form a hierarchy.
  
    The child class reuses all fields and methods of the parent class (common part) and can implement its own (unique part).
  *i.e: Animal >> Reptile >> Snake >> Cobra*
  

- **Encapsulation**
  
  Encapsulation is achieved when each object keeps its state private, inside a class. Other objects don’t have direct access to this state. Instead, they can only call a list of public functions — called methods.

    So, the object manages its own state via methods — and no other class can touch it unless explicitly allowed. If one wants to communicate with the object, they should use the methods provided. But (by default), they can’t change the state.
  

- **Polymorphism**
    
    Polymorphism gives a way to use a class exactly like its parent so there’s no confusion with mixing types. But each child class keeps its own methods as they are.

    This typically happens by defining a (parent) interface to be reused. It outlines a bunch of common methods. Then, each child class implements its own version of these methods.

    *i.e: Triangle, Circle, Rectangle are different shapes, but can use the same method to calculate area.*

### Functions and good practice of functions
#### DRY - Don't Repeat Yourself

```python
# First Iterations
def greeting():
    print("Welcome on Board! enjoy your trip")
#pass # pass is the keyword that allows the interpreter to skip this without any errors

greeting() # if we didn't call the function it would execute the code with no error but no outcome
# DRY Don't Repeat your self by declaring functions and reusing code
```
- Return statement in a function
```python
# Second Iteration using RETURN statement
def greeting():
    print("Good Morning")
    return "Welcome on board! Enjoy your trip!!"
print(greeting())

```

````python
# Third Iteration with user name as a string as an argument/args

def greeting(name): # name is the arg
#    print(name)
    return "Welcome on Board " + name
print(greeting("James Bond")) # we have to provide 1 arg as a string 

````

```python
# Create a function to prompt the user to enter their name and display the name back to user with greeting message
def greeting(name):
    return "Welcome on board " + name

name1 = input("What is your name? ")
print(greeting(name1))

```

```python
# Let's create a function with multiple args as an int

def add(num1, num2):
    return num1 + num2

print(add(9, 3))

# Code after the return statement doesn't get executed as functions exits after the return statement

def multiply(num1, num2):
    print("This functions multiplies 2 numbers ")
    return num1 * num2
    print(" this is the required outcome of 2 numbers ") # this line of code will not execute as return statement is last line of code that function executes
print(multiply(3, 3))

```
## Object Oriented Programming
### Create animal class
```python
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

```
### Create reptile class to inherit Animal class ^
```python
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
```
### create a Snake class to inherit Reptile class ^
```python
from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True

# Lets add specific methods/behaviours
    def use_tongue_to_smell(self):
        return "If I can touch it, I can smell it."

# Let's create an object of snake class
smart_snake = Snake()
# print(smart_snake.move())
# print(smart_snake.use_tongue_to_smell())
```
### create a Python class to inherit Snake class ^
```python
from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True

    def digest_large_prey(self):
        return "I can digest anything without chewing."

    def climb(self):
        return "Up we go..."

    def __shed_skin(self): # This is encapsulation - no one can find this
        return "I'm growing out of my skin."

# Let's create and object
fast_python = Python()
print(fast_python.climb())
print(fast_python.use_tongue_to_smell())
print(fast_python.eyes)
```