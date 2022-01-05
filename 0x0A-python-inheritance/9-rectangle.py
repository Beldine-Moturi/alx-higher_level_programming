#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Description for the class Rectangle"""

    def __init__(self, width, height):
        """Initializes instances of the class

        Args:
            width (int): the width of the Rectangle
            height (int): the height of the rectangle
        """

        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""

        return (self.__width * self.__height)

    def __str__(self):
        """Returns a description for the current Rectangle instance"""

        return (f"[{self.__class__.__name__}] {self.__width}/{self.__height}")
