#!/usr/bin/python3
"""
Contains unittests for the Base class methods
"""
import json
from models.base import Base
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


    def tearDown(self):
        """Deletes resources(files) created when running tests"""

        try:
            os.remove("Base.json")
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


if __name__ == "__main__":
    unittest.main()
