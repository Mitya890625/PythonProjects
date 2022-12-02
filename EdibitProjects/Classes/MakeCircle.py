class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.1459265 * self.radius**2

    def get_circumference(self):
        return 2 * 3.1459265 * self.radius

def main():
    c1 = Circle(11)
    print(c1.get_area())
    print(c1.get_circumference())
main()
