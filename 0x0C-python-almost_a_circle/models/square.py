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

    def update(self, *args, **kwargs):
        """Assigns an argument in args or kwargs to each attribute of the
        Square instance"""

        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
