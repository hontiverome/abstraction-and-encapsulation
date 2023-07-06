from Car import Car
import time, pyfiglet
from termcolor import cprint, colored

# create object
car = Car(2023, "Porsche")

# acceleration 
accelerateTitle = pyfiglet.figlet_format("Acceleration", font="lcd")
cprint("\n" +  "="*50 + "\n" + colored(accelerateTitle), "red", attrs=["bold"])
for i in range(5):
    time.sleep(0.5)
    car.accelerate()
    print("Accelerating... Current Speed:", car.get_speed())

# braking
brakingTitle = pyfiglet.figlet_format("Braking", font="lcd")
cprint("\n" +  "="*50 + "\n" + colored(brakingTitle), "red", attrs=["bold"])
print("\nBraking Method")
for i in range(5):
    time.sleep(0.5)
    car.brake()
    print("Braking... Current Speed:", car.get_speed())
    
# HONTIVEROS, JEROME ANDREI O.
# BSCPE 1-5