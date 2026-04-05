#!/usr/bin/python3
class Rectangle:
    """Rectangle class with full features."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.width for _ in range(self.height))

    def __repr__(self):
        """Recreate object"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Destructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
