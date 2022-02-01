#!/usr/bin/python3
"""Defines a base class ``Base()``"""
import json


class Base:
    """Base - the base class for all classes in this project
            - manages the id attribute in all future classes
    Attributes:
        __nb_objects (int): the number of Instantiated objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instances of the class

        Args:
            id (int): the id of the object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError
        for item in list_dictionaries:
            if type(item) != dict:
                raise TypeError
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:"""

        new_list = []
        if list_objs is not None:
            for item in list_objs:
                new_list.append(item.to_dictionary())
        my_json_string = Base.to_json_string(new_list)
        with open(f"{cls.__name__}.json", mode='w') as f:
            f.write(my_json_string)
