#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """Description for Instances of the class Rectangle
    that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates objects of the class

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
            x: x coordinate used to print out the rectangle
            y: y coordinate used to print out the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width attribute"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        """sets the value of the height of the rectangle"""
        self.__height = value

    @property
    def x(self):
        """returns the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of the x attribute"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns the area of a Rectangle instance"""

        return (self.__width * self.__height)

    def update(self, *args):
        """Assigns an argumetn in args to each attrinute of the
        Rectangle instance"""

        pass

    def display(self):
        """Prints a Rectangle instance to stdout with the character #"""

        [print() for i in range(self.__y)]
        for i in range(self.__height):
            [print(' ', end='') for n in range(self.__x)]
            [print('#', end='') for j in range(self.__width)]
            print()

    def __str__(self):
        """returns a description for the Rectangle instances"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"
