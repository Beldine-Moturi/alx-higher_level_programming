#!/usr/bin/python3
"""Defines a base class ``Base()``"""
import csv
import json
import turtle


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

    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string:
        json_string is a string representing a list of dictionaries"""

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                if ("width" not in dictionary.keys()) or\
                   ("height" not in dictionary.keys()):
                    raise TypeError
                else:
                    new_instance = cls(1, 2)
            elif cls.__name__ == "Square":
                if (
                        "size" not in dictionary.keys() and
                        ('width' not in dictionary.keys()) and
                        ('height' not in dictionary.keys())):
                    raise TypeError
                else:
                    new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        try:
            with open(f"{cls.__name__}.json", 'r') as f:
                my_list = Base.from_json_string(f.read())
                return [cls.create(**item) for item in my_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv"""

        with open(f"{cls.__name__}.csv", mode='w', newline='') as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    keys = ['id', 'width', 'height', 'x', 'y']
                else:
                    keys = ['id', 'size', 'x', 'y']
                my_file = csv.DictWriter(csvfile, fieldnames=keys)
                for item in list_objs:
                    my_file.writerow(item.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in csv"""

        try:
            with open(f"{cls.__name__}.csv", mode='r', newline='') as csvfile:
                if cls.__name__ == "Rectangle":
                    keys = ['id', 'width', 'height', 'x', 'y']
                else:
                    keys = ['id', 'size', 'x', 'y']
                my_file = csv.DictReader(csvfile, fieldnames=keys)
                my_file = [dict([k, int(v)] for k, v in d.items())
                           for d in my_file]
                return [cls.create(**row) for row in my_file]

        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ that opens a window and draws all the Rectangles and Squares
        (Subclasses of the Base class)

        Args:
            list_rectangles: a list of Rectangle instances to draw
            list_squares: a list of Square instances to draw
        """

        t = turtle.Turtle()
        t.pensize(5)
        t.shape('turtle')

        sc = turtle.Screen()
        sc.setup(1000, 1000)
        sc.bgcolor("white")

        t.color("red")
        for rect in list_rectangles:
            t.showturtle()
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for n in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.hideturtle()

        t.color("green")
        for sq in list_squares:
            t.showturtle()
            t.penup()
            t.goto(sq.x, sq.y)
            t.pendown()
            for i in range(2):
                t.forward(sq.size)
                t.left(90)
                t.forward(sq.size)
                t.left(90)
            t.hideturtle()

        turtle.exitonclick()
