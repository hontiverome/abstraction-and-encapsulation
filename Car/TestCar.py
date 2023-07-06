from Car import Car
import time
# create car object
car = Car(2023, "Porsche")

# acceleration 
print("Acceleration Method")
for i in range(5):
    time.sleep(0.5)
    car.accelerate()
    print("Accelerating... Current Speed:", car.get_speed())

# braking
print("\nBraking Method")
for i in range(5):
    time.sleep(0.5)
    car.brake()
    print("Braking... Current Speed:", car.get_speed())