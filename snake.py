# Let's create a Snake class

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