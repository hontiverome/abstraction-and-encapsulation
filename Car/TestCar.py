from Car import Car

# create car object
car = Car(2023, "Porsche")

# acceleration 
print("Acceleration Method")
for i in range(5):
    car.accelerate()
    print("Current Speed:", car.get_speed())

# braking
print("\nBraking Method")
for i in range(5):
    car.brake()
    print("Current Speed:", car.get_speed())