#!/usr/bin/python3
"""This module defines a Square class with getter and setter for size"""


class Square:
    """Square class with private size attribute and area method"""

    def __init__(self, size=0):
        """Initialize square with optional size"""
        self.size = size  # istifadə edirik setter-ə, validation burada gedir

    @property
    def size(self):
        """Retrieve the current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size * self.__size
