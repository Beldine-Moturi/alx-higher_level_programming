#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Description for instances of the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instances of the Square

        Args:
            size (int): the size of the square instance
            x (int): x coordinate used to print out the square
            y (int): y coordinate used to print out the square
            id (int): identifier for a square instance
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value for the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation for Square instances"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}\
 - {self.width}"
