#!/usr/bin/python3
"""
This module defines a class rectangle
"""


class Rectangle:
    """Description for a class Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialises instances of the class
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """returns the width of the square"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the square"""

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
        """sets the height of the square"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the square"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """prints the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        my_rec = []
        for i in range(self.__height):
            symbol = str(self.print_symbol)
            [my_rec.append(symbol) for n in range(self.__width)]
            if i != (self.__height - 1):
                my_rec.append('\n')
        return ("".join(my_rec))

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """deletes an instance of a Rectangle"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
