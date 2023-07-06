# car class
# class creation
class Car:
    # constructor that initializes car attributes 
    def __init__(self, yearModel, maker):
        self.__yearModel = yearModel
        self.__maker = maker
        self.__speed = 0
    
    # methods
    # method that increases car speed
    def accelerate(self):
        self.__speed += 5
    
    # car brake method
    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    # current speed checker method
    def get_speed(self):
        return self.__speed
    
# HONTIVEROS, JEROME ANDREI O.
# BSCPE 1-5