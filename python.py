# Let's create Python class

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