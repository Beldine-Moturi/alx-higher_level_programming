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

    def update(self, *args, **kwargs):
        """Assigns an argumetn in args to each attrinute of the
        Rectangle instance"""

        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def display(self):
        """Prints a Rectangle instance to stdout with the character #"""

        [print() for i in range(self.__y)]
        for i in range(self.__height):
            [print(' ', end='') for n in range(self.__x)]
            [print('#', end='') for j in range(self.__width)]
            print()

    def __str__(self):
        """returns a description for the Rectangle instances"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}"

    def to_dictionary(self):
        """Return a dictionary representation of objects of the class"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
