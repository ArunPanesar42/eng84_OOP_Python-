from snake import Snake
class Python(Snake):
    def __init__(self):
        super(Python, self).__init__()
        self.venom = False
        self.large = True
        self.two_lungs = True

    def climb(self):
        return "Up we go"
    def swallow(self):
        return "I Will eat but not chew"

python_object = Python()
print(python_object.breathe()) # function from our Animal class
print(python_object.hunt()) # function from our Reptile class
print(python_object.use_venom())# fucntion from our Snake class
print(python_object.shed_skin()) # function from our python class