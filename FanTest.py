from Fan import Fan
class Test:
    def __init__(self):
        fan1 = Fan(Fan.fast, 10, "yellow", True)
        fan2 = Fan(Fan.medium, 5, "blue", False)

        print("Fan 1:")
        print("Speed:", fan1.get_speed())
        print("Radius:", fan1.get_radius())
        print("Color:", fan1.get_color())
        print("Is On:", fan1.is_on())

        print("\nFan 2:")
        print("Speed:", fan2.get_speed())
        print("Radius:", fan2.get_radius())
        print("Color:", fan2.get_color())
        print("Is On:", fan2.is_on())

if __name__ == '__main__':
    test = Test()