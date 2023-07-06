# car class
# class creation
class Car:
    # constructor that initializes car attributes 
    def __init__(self, year_model, maker):
        self.__year_model = year_model
        self.__maker = maker
        self.__speed = 0
    
    # methods
    # method that increases car speed
    def accelerate(self):
        self.__speed += 5