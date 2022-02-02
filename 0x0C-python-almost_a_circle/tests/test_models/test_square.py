#!/usr/bin/python3
"""Contains test cased for the Square class"""
from models.square import Square
import json
import os
import unittest


class TestSquareInstantiation(unittest.TestCase):
    """ Tests that objects of the class Square are properly instantiated"""

    def test_correct_input(self):
        """Tests instantiation when objects are created with proper
        attribute values"""

        s1 = Square(5, 1, 2)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)

    def test_required_positional_attribute(self):
        """Tests that TypeError exception is raised if the size
        attribute is not provided during object instantiation"""

        with self.assertRaises(TypeError):
            Square()

    def test_optional_positional_atributes(self):
        """Tests that instances of the Square can be created without the x
        and y attributes; 0 is assigned"""

        s1 = Square(4)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_upto_4_arguments(self):
        """Tests Square objects instantiation with varying number
        of arguments"""

        s1 = Square(4, 1)
        s2 = Square(5, 2, 3, 12)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s2.id, 12)

    def test_setter_methods(self):
        """Tests that the setter methods from Base class properly assign
        attribute values"""
        s1 = Square(5, 1, 2)
        s1.width = 6
        s1.height = 7
        s1.x = 3
        s1.y = 4
        s1.id = 43
        self.assertEqual(s1.width, 6)
        self.assertEqual(s1.height, 7)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 43)

class TestSquareAttributes(unittest.TestCase):
    """Tests that the attributtes of Square insatnces are assigned
    proper values and appropriate exceptions are raised otherwise"""

    def test_size_attribute(self):
        """Tests that the appropriate exceptions are raised if the size
        attribute is not an integer and is not greater than 0"""

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square("5")
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(-5)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(0)

    def test_width_attribute(self):
        """Tests that the appropriate exceptions are raised if the width
        attribute is not an integer or is not greater than 0"""

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square("10", 3, 4)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(-5, 1, 2)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(0, 3, 4)

    def test_x_attribute(self):
        """Tests whether appropriate exceptions are raised if the x value
        is not an integer or is less than 0"""

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(10, "3", 4)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Square(10, -3, 4)

    def test_y_attribute(self):
        """Tests whether the appropriate exceptions are raised if the y value
        is not an integer or is less than 0"""

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(10, 3, "4")
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Square(12, 3, -4)

class TestSquareMethods(unittest.TestCase):
    """Tests that the methods of the Square class work as they are
    expected to"""

    def test_str_method(self):
        """Tests that the __str__ method returns the expected string
        representation of objects of this class"""

        s1 = Square(5)
        s2 = Square(4, 1)
        s3 = Square(6, 2, 3)
        s4 = Square(7, 3, 4, 12)

        self.assertEqual(s1.__str__(), f"[Square] ({s1.id}) 0/0 - 5")
        self.assertEqual(s2.__str__(), f"[Square] ({s2.id}) 1/0 - 4")
        self.assertEqual(s3.__str__(), f"[Square] ({s3.id}) 2/3 - 6")
        self.assertEqual(s4.__str__(), "[Square] (12) 3/4 - 7")

    def test_update_args_method(self):
        """Tests that the update method properly assigns arguments to
        each attribute of the Rectangle class, when called using *args"""

        s1 = Square(5, 1, 2)
        s1.update(24)
        self.assertEqual(s1.id, 24)
        s1.update(24, 8)
        self.assertListEqual([s1.id, s1.size], [24, 8])
        s1.update(24, 8, 9)
        self.assertListEqual([s1.id, s1.size, s1.x], [24, 8, 9])
        s1.update(24, 8, 9, 10)
        self.assertListEqual([s1.id, s1.size, s1.x, s1.y], [24, 8, 9, 10])

    def test_update_kwargs_method(self):
        """Tests that the update method properly assgins arguments to each
        attribute of the Rectangle class when called using *kwargs"""

        s1 = Square(10, 10, 10, 10)
        s1.update(size=15)
        self.assertEqual(s1.size, 15)
        s1.update(x=2, y=3)
        self.assertListEqual([s1.x, s1.y], [2, 3])
        s1.update(size=4, y=1, x=1)
        self.assertListEqual([s1.size, s1.x, s1.y], [4, 1, 1])
        s1.update(x=0, id=12, size=23, y=0)
        self.assertListEqual([s1.id, s1.size, s1.x, s1.y],
                             [12, 23, 0, 0])

    def test_to_dictionary_method(self):
        """Tests that the to_dictionary method returns the expected
        representation of a Square instance"""
        s1 = Square(5)
        s2 = Square(5, 2)
        s3 = Square(5, 2, 3)
        s4 = Square(5, 2, 3, 12)
        self.assertTrue(type(s1.to_dictionary()), dict)
        self.assertDictEqual(s1.to_dictionary(), {
            'size': 5,
            'x': 0,
            'y': 0,
            'id': s1.id
        })
        self.assertDictEqual(s2.to_dictionary(), {
            'size': 5,
            'x': 2,
            'y': 0,
            'id': s2.id
        })
        self.assertDictEqual(s3.to_dictionary(), {
            'size': 5,
            'x': 2,
            'y': 3,
            'id': s3.id
        })
        self.assertDictEqual(s4.to_dictionary(), {
            'size': 5,
            'x': 2,
            'y': 3,
            'id': 12
        })

    def tearDown(self):
        """Deletes resources(files) created when tests are run"""

        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_method(self):
        """Tests that the save_to_file method writes the JSON string
           representation of list_objs to a file"""

        s1 = None
        s2 = []
        s3 = Square(5, 1, 2, 12)

        Square.save_to_file(s1)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file(s2)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file([s3])
        with open("Square.json") as f:
            self.assertEqual(f.read(), json.dumps([s3.to_dictionary()]))


if __name__ == "__main__":
    unittest.main()
