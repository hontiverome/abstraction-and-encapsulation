# fan class
# create class
class Fan:
    __slow=1
    __medium=2
    __fast=3

# intialize variables
    def __init__(self, speed=1,radius=5,color="blue",on=False) -> None:
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
        
# method creation
# get speed method
    def get_speed(self):
        return self.__speed
    
# set speed method
    def set_speed(self, speed):
        if speed in (Fan.__slow, Fan.__medium, Fan.__fast):
            self.__speed = speed   
        else:
            raise ValueError("Invalid speed value.")
        
# get radius method
    def get_radius(self):
        return self.__radius