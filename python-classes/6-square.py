#!/usr/bin/python3
"""Square class with size, position, area, and print methods"""


class Square:
    """Square with private size and position attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize with optional size and position"""
        self.size = size          # setter çağırılır
        self.position = position  # setter çağırılır

    @property
    def size(self):
        """Retrieve current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve current position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with validation"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return square area"""
        return self.__size * self.__size

    def my_print(self):
        """Print square with '#' and consider position"""
        if self.__size == 0:
            print()
            return
        # vertical shift
        for _ in range(self.__position[1]):
            print()
        # print square lines
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
