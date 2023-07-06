from Pet import Pet 
import time, pyfiglet
from termcolor import colored, cprint
# create pet object
pet = Pet("", "", "")

# input for pet information 
pet.setName(input("What is the pet's name? : "))
pet.setAnimalType(input("What is their type? : "))
pet.setAge(input("What is their age? : "))

# output for pet information
petTitle = pyfiglet.figlet_format("Pet Info:", font="lcd", width = 500)
cprint(colored("="*160),"red")
cprint(colored(petTitle), "red", attrs=["bold"])
print("\nPet's Information:")
print("Name:", pet.getName())
print("Animal Type:", pet.getAnimalType())
print("Age:", pet.getAge())

# HONTIVEROS, JEROME ANDREI O.
# BSCPE 1-5