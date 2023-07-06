# pet class
class Pet:
    # create constructor
    def __init__(self, name, animalType, age):
        self.__name = ""
        self.__animalType = ""
        self.__age = 0
    
# name scheme method
    # sets name
    def setName(self, name):
        self.__name = name
    
    # gets name
    def getName(self):
        return self.__name
    
# animal type method
    # sets animal type 
    def setAnimalType(self, animal_type):
        self.__animal_type = animal_type
    
    # gets animal type
    def getAnimalType(self):
        return self.__animal_type
    
# age method
    # sets age
    def setAge(self, age):
        self.__age = age
    
    # gets age
    def getAge(self):
        return self.__age

# HONTIVEROS, JEROME ANDREI O.
# BSCPE 1-5