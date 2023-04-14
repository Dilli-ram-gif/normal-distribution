# Using default parameter in Python
class Rectangle:

    def __init__(self, breadth, height, length=6):
        self.length = length
        self.breadth = breadth
        self.height = height
        self.area = self.breadth * self.length
        self.volume = self.breadth * self.length * self.height


area1 = Rectangle(5,6)
volume1 = Rectangle(2,3,4)
print(f"The area of the rectangle is {area1.area}")
print(f"The volume of the rectangle is {volume1.volume}")
