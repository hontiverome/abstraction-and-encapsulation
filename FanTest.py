from Fan import Fan
import time
class Test:
    def __init__(self):
        fan1 = Fan(Fan.fast, 10, "yellow", True)
        fan2 = Fan(Fan.medium, 5, "blue", False)

        time.sleep(0.5)
        print("Fan 1:")
        time.sleep(0.3)
        print("Speed of the fan:", fan1.get_speed())
        time.sleep(0.3)
        print("Radius:", fan1.get_radius())
        time.sleep(0.3)
        print("Color:", fan1.get_color())
        time.sleep(0.3)
        print("Is On:", fan1.is_on())

        time.sleep(1)
        print("\nFan 2:")
        time.sleep(0.3)
        print("Speed:", fan2.get_speed())
        time.sleep(0.3)
        print("Radius:", fan2.get_radius())
        time.sleep(0.3)
        print("Color:", fan2.get_color())
        time.sleep(0.3)
        print("Is On:", fan2.is_on())

# executes program by creating an instance
if __name__ == '__main__':
    test = Test()