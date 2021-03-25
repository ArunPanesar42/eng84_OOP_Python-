# Lets import from animal

from animal import Animal # This is to ensure Animal class is inherited
class Reptile(Animal):  # We Need to pass the animal class as an arg in our reptile class

    def __init__(self):
        super(Reptile, self).__init__() # super is to make everything available from parent class
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chamebers = [3,4]

    def hunt(self):
        return "Working hard to catch next meal"
    def use_venom(self):
        return "Will attack"
    def seek_heat(self):
        return "Looking for sun"

reptile_object = Reptile()
# print(reptile_object.hunt())
# print(reptile_object.breathe())