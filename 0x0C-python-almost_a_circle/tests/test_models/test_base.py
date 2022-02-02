#!/usr/bin/python3
"""
Contains unittests for the Base class methods
"""
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import unittest


class TestBaseInstantiation(unittest.TestCase):
    """Tests that objects of the class are properly Instantiated"""

    def setUp(self):
        """Sets up the resources required to run the tests"""

        self.base_1 = Base()
        self.base_2 = Base()
        self.base_3 = Base(24)
        self.base_4 = Base()

    def tearDown(self):
        """Deletes the resources created after tests have run"""
        del self.base_1
        del self.base_2
        del self.base_3
        del self.base_4

    def test_no_id(self):
        """Test whether id attribute is assigned automatically when
        none is provided during intantiation"""
        self.assertEqual(self.base_1.id, self.base_2.id - 1)

    def test_id_increment(self):
        """Tests whether id attribute is incremented(value of __nb_objects)
        when subsequent objects are created without providing the id attribute
        """

        self.assertEqual(self.base_2.id, self.base_1.id + 1)

    def test_unique_id(self):
        """Tests whether id attribute is assigned with value provided during
        instantiation"""

        self.assertEqual(self.base_3.id, 24)

    def test_id_after_unique_id(self):
        """Tests that __nb_objects is only incremented when objects are
        Instantiated without id attribute"""

        self.assertEqual(self.base_4.id, self.base_2.id + 1)
        self.assertNotEqual(self.base_4.id, self.base_3.id + 1)

    def test_exception(self):
        """Test that an exception is raised when  objects are intantiated with
        more than one argument"""

        with self.assertRaises(TypeError):
            Base(1, 2)

class TestBaseMethods(unittest.TestCase):
    """Tests that all the methods in the Base class work as expected"""

    def test_to_json_string_method(self):
        """Tests that the to_json_string method  returns the JSON string
        representation of list_dictionaries"""

        list1 = None
        list2 = []
        list3 = [{'x': 2, 'y': 3, 'width': 4, 'height': 5, 'id': 12}]
        list4 = [{'x': 1, 'y': 2, 'width': 5, 'height': 6},
                 {'x': 2, 'y': 3, 'width': 7, 'height': 8, 'id': 23}]
        self.assertEqual(Base.to_json_string(list1), "[]")
        self.assertEqual(Base.to_json_string(list2), "[]")
        self.assertEqual(Base.to_json_string(list3), json.dumps(list3))
        self.assertEqual(Base.to_json_string(list4), json.dumps(list4))

    def test_to_json_string_exceptions(self):
        """Tests that the to_json_string method raises the right exceptions
        is the argument passed to it is not a list of dictionaries"""

        with self.assertRaises(TypeError):
            Base.to_json_string("a string")
        with self.assertRaises(TypeError):
            Base.to_json_string(5)
        with self.assertRaises(TypeError):
            Base.to_json_string(["string_a", "string_b"])
        with self.assertRaises(TypeError):
            Base.to_json_string([4, 5])
        with self.assertRaises(TypeError):
            Base.to_json_string([{'width': 4, 'height': 5}, "string", 45])

    def test_from_json_string_method(self):
        """Tests that the from_json_string method returns the list of the JSON
        string representation json_string"""

        list1 = None
        list2 = "[]"
        list3 = [{'x': 2, 'y': 3, 'width': 4, 'height': 5, 'id': 12}]
        list4 = [\
            {'x': 1, 'y': 2, 'width': 5, 'height': 6},\
            {'x': 2, 'y': 3, 'width': 7, 'height': 8, 'id': 23}\
        ]
        json_string3 = Base.to_json_string(list3)
        json_string4 = Base.to_json_string(list4)

        self.assertEqual(Base.from_json_string(list1), [])
        self.assertEqual(Base.from_json_string(list2), [])
        self.assertEqual(Base.from_json_string(json_string3),
                         [{'x': 2, 'y': 3, 'width': 4, 'height': 5, 'id': 12}])
        self.assertEqual(Base.from_json_string(json_string4),[
            {'x': 1, 'y': 2, 'width': 5, 'height': 6},
            {'x': 2, 'y': 3, 'width': 7, 'height': 8, 'id': 23}
        ])

    def tearDown(self):
        """Deletes resources(files) created when running tests"""

        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_method(self):
        """Tests that the save_to_file method writes the JSON string
        representation of list_objs to a file"""

        l1 = None
        l2 = []
        l3 = Rectangle(4, 5, 1, 2)
        l4 = Square(5, 1, 1)
        l5 = [l3, l4]

        Base.save_to_file(l1)
        with open("Base.json")as f:
            self.assertEqual(f.read(), "[]")

        Base.save_to_file(l2)
        with open("Base.json") as f:
            self.assertEqual(f.read(), "[]")

        Base.save_to_file(l5)
        with open("Base.json") as f:
            self.assertEqual(f.read(), json.dumps([
                l3.to_dictionary(),
                l4.to_dictionary()
            ]))

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_Rectangle_create_method(self):
        """Tests that the create method properly creates new Rectangle
    instances from the arguments supplied"""

        r3 = {'id': 23, 'width': 4, 'height': 5}
        r4 = {'id': 34, 'width': 6, 'height': 7, 'x': 1}
        r5 = {'id': 32, 'width': 8, 'height': 9, 'x': 2, 'y': 3}

        new_r3 = Rectangle.create(**r3)
        self.assertEqual(str(new_r3), "[Rectangle] (23) 0/0 - 4/5")

        new_r4 = Rectangle.create(**r4)
        self.assertEqual(str(new_r4), "[Rectangle] (34) 1/0 - 6/7")

        new_r5 = Rectangle.create(**r5)
        self.assertEqual(str(new_r5), "[Rectangle] (32) 2/3 - 8/9")

    def test_rectangle_create_exceptions(self):
        """Tests that the create method raises the appropriate exceptions when
        called with an insufficient dictionary"""

        r1 = {'id': 12}
        r2 = {'id': 24, 'width': 5}
        r3 = {'id': 25, 'height': 6}

        with self.assertRaises(TypeError):
            new_r1 = Rectangle.create(**r1)

        with self.assertRaises(TypeError):
            Rectangle.create(**r2)

        with self.assertRaises(TypeError):
            Rectangle.create(**r3)

    def test_square_create_method(self):
        """Tests that the create method properly creates new Square instances
         from the arguments supplied"""

        s1 = {'id': 10, 'size': 5}
        s2 = {'id': 12, 'size': 6, 'x': 2}
        s3 = {'id': 24, 'size': 8, 'x': 3, 'y': 4}

        new_s1 = Square.create(**s1)
        self.assertEqual(str(new_s1), "[Square] (10) 0/0 - 5")

        new_s2 = Square.create(**s2)
        self.assertEqual(str(new_s2), "[Square] (12) 2/0 - 6")

        new_s3 = Square.create(**s3)
        self.assertEqual(str(new_s3), "[Square] (24) 3/4 - 8")

    def test_square_create_exceptions(self):
        """Tests that appropriate exceptions are raised if the
        create method is called with an insufficient dictionary"""

        s1 = {'id': 5}
        s2 = {'id': 24, 'x': 4, 'y': 5}

        with self.assertRaises(TypeError):
            Square.create(**s1)

        with self.assertRaises(TypeError):
            Square.create(**s2)


if __name__ == "__main__":
    unittest.main()
