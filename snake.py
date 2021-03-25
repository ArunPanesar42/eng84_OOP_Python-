
from reptile import Reptile
class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.limbs = False
        self.venom = True
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return "I use my tongue to smell the food"
    def shed_skin(self):
        return "growing out"

snake_object = Snake()
# print(snake_object.limbs)
# print(snake_object.breathe())
# We have double inheritance and Encapsulated in fucntions in parent classes