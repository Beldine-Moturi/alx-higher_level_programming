#!/usr/bin/python3
"""Defines a class Square that inherits from class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Description for the class Square"""

    def __init__(self, size):
        """Initializes instances of the class"""

        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""

        return (self.__size ** 2)

    def __str__(self):
        """Returns a string representation of the Square"""

        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
