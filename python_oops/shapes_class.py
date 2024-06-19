from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        return "Area of Circle with Radius {} = {:.2f}".format(self.radius, math.pi * (self.radius ** 2))

    def perimeter(self):
        return "Perimeter of Circle with Radius {} = {:.2f}".format(self.radius, 2 * math.pi * self.radius)


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = float(length)
        self.breadth = float(breadth)

    def area(self):
        return "Area of Rectangle with Length & Breadth {} & {} = {:.2f}".format(self.length, self.breadth, self.length*self.breadth)

    def perimeter(self):
        return "Perimeter of Rectangle with Length & Breadth {} & {} = {:.2f}".format(self.length, self.breadth, 2*(self.length+self.breadth))


class Square(Shape):

    def __init__(self, side):
        self.side = float(side)

    def area(self):
        return "Area of Square with Side {} = {:.2f}".format(self.side, self.side**2)

    def perimeter(self):
        return "Perimeter of Square with Side {} = {:.2f}".format(self.side, 4 * self.side)


print("Circle: Radius = 9")
c1 = Circle(9)
print(c1.perimeter())
print(c1.area())
print("Rectangle: Length = 9, Breadth = 9")
r1 = Rectangle(9, 9)
print(r1.perimeter())
print(r1.area())
print("Square: Side = 9")
s1 = Square(9)
print(s1.perimeter())
print(s1.area())



