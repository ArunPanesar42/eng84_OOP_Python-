# Lets create our first class
# syntax : class_____():

# Creating an animal class

class Animal():
    name = "Dog" # Class Variable
    def __init__(self): # self refers the current class
        self.alive = True
        self.spine = True
        self.lungs = True

    def move(self):
        return "Moveing left, right and center"
    def eat(self):
        return "Keep Eating to stay alive"
    def breathe(self):
        return "Keep breathing to live"
#
cat = Animal()
