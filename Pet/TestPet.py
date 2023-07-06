from Pet import Pet 
import time
# create pet object
pet = Pet("", "", "")

# input for pet information 
pet.setName(input("What is the pet's name? : "))
pet.setAnimalType(input("What is their type? : "))
pet.setAge(input("What is their age? : "))

# output for pet information
print("\nPet's Information:")
print("Name:", pet.getName())
print("Animal Type:", pet.getAnimalType())
print("Age:", pet.getAge())