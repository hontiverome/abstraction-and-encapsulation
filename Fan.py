# fan class
# create class
# intialize variables
# method creation
class Fan:
    __slow=1
    __medium=2
    __fast=3
    
    def __init__(self, speed=1,radius=5,color="blue",on=False) -> None:
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on