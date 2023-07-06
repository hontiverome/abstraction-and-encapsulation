# pet class
class Pet:
    # create constructor
    def __init__(self):
        self.__name = ""
        self.__animalType = ""
        self.__age = 0
    
# name scheme method
    # sets name
    def set_name(self, name):
        self.__name = name
    
    # gets name
    def get_name(self):
        return self.__name
    
# animal type method
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
# age method
    def set_age(self, age):
        self.__age = age