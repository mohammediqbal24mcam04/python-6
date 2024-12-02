class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# User input for rectangles
print("Enter dimensions for Rectangle 1:")
r1 = Rectangle(float(input("Length: ")), float(input("Breadth: ")))

print("Enter dimensions for Rectangle 2:")
r2 = Rectangle(float(input("Length: ")), float(input("Breadth: ")))

if r1.area() > r2.area():
    print("Rectangle 1 has a larger area.")
elif r1.area() < r2.area():
    print("Rectangle 2 has a larger area.")
else:
    print("Both rectangles have the same area.")
