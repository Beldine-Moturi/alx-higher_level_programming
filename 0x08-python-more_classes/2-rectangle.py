#!/usr/bin/python3
"""
This module defines a class Rectangle
"""


class Rectangle:
    """Description for the class Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes instances of the class Rectangle

        Args:
            width (int): the width the the rectangle
            height (int): the height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value


    @property
    def height(self):
        """returns the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value


    def area(self):
        """returns the area of the rectangle"""

        return (self.width * self.height)


    def perimeter(self):
        """returns the perimeter of the rectangle"""

        if (self.__width == 0 or self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))
