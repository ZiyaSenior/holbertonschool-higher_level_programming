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
        self.radius = radius

    def area(self):
        return math.pi * abs(self.radius) * abs(self.radius)

    def perimeter(self):
        return math.pi * 2 * abs(self.radius)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


if __name__ == "__main__":

    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=6)

    shape_info(circle)
    shape_info(rectangle)
