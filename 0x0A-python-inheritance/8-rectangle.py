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
