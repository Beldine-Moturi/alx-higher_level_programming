#!/usr/bin/python3
"""Defines a base class ``Base()``"""


class Base:
    """Description for objects of the class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instances of the class

        Args:
            id (int): the id of the object
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
