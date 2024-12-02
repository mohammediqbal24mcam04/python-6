from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# User input
choice = input("Calculate area of Rectangle or Triangle? (R/T): ").upper()

if choice == "R":
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    rect = Rectangle(length, breadth)
    print(f"Area of Rectangle: {rect.calculate_area()}")
elif choice == "T":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    tri = Triangle(base, height)
    print(f"Area of Triangle: {tri.calculate_area()}")
