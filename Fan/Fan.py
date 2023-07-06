# fan class
# create class
from colorama import Fore,Style
class Fan:
    slow=1
    medium=2
    fast=3

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
    
# radius setter method
    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            raise ValueError("Invalid radius value")

# checks if on method
    def is_on(self):
        return self.__on

# turns fan on method 
    def set_on(self, on):
        self.__on = on
        
# color checker method
    def get_color(self):
        return self.__color
    
# set color method
    def set_color(self, color):
        self.__color = color

 def display_fan_properties(self):
        print(Style.BRIGHT + Fore.CYAN + "  Speed      : " + '\033[0m', Fore.YELLOW, self.__speed)
        print(Style.BRIGHT + Fore.CYAN + "  Radius     : " + '\033[0m', Fore.YELLOW, self.__radius)
        print(Style.BRIGHT + Fore.CYAN + "  Color      : " + '\033[0m', Fore.YELLOW, self.__color)
        print(Style.BRIGHT + Fore.CYAN + "  Status(ON) : " + '\033[0m', Fore.YELLOW, self.__status, '\033[0m', "\n")
        
# HONTIVEROS, JEROME ANDREI O.
# BSCPE 1-5