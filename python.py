from snake import Snake
class Python(Snake):
    def __init__(self):
        super(Python, self).__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False # Polymorphism for attributes

    def climb(self):
        return "Up we go"
    def swallow(self):
        return "I Will eat but not chew"

    # polymorphism for methods. The previous value of the method is changed
    def hunt(self):
        return "Working hard to catch next meal"

python_object = Python()
print(python_object.breathe()) # function from our Animal class
print(python_object.hunt()) # function from our Reptile class
print(python_object.climb())# function from our Snake class
print(python_object.shed_skin()) # function from our Snake class