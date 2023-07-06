# pet class
class Pet:
    # create constructor
    def __init__(self):
        self.__name = ""
        self.__animalType = ""
        self.__age = 0
    
    # name scheme method
    def set_name(self, name):
        self.__name = name