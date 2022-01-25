#!/usr/bin/python3
"""Defines Test cases for the class Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Tests whether objects of the class Rectangle
    are properly instantiated"""

    def test_correct_input(self):
        """Tests the correct output of instance attributes(width,
        height, x, y)when objects are instantiated with proper values"""

        self.Rect1 = Rectangle(10, 15, 4, 5)
        self.assertEqual(self.Rect1.width, 10)
        self.assertEqual(self.Rect1.height, 15)
        self.assertEqual(self.Rect1.x, 4)
        self.assertEqual(self.Rect1.y, 5)

    def test_required_positional_attributes(self):
        """Tests that TypeError exception is raised if the width and height
        attribute are not provided uring object instantiation"""

        with self.assertRaises(TypeError):
            Rectangle()
            Rectangle(20)

    def test_optional_positional_attributes(self):
        """Tests that objects of this class can be instantiated without
        the attributes x and y; will be assigned with 0 if none
        is provided"""

        self.Rect2 = Rectangle(24, 12)
        self.assertEqual(self.Rect2.x, 0)
        self.assertEqual(self.Rect2.y, 0)

    def test_upto_5_args(self):
        """Tests the correct attribute assignment when objects are
        instantiated with up to 5 arguments"""

        self.Rect3 = Rectangle(10, 14, 5)
        self.Rect4 = Rectangle(15, 20, 3, 4, 12)
        self.assertEqual(self.Rect3.width, 10)
        self.assertEqual(self.Rect3.height, 14)
        self.assertEqual(self.Rect3.x, 5)
        self.assertEqual(self.Rect3.y, 0)
        self.assertEqual(self.Rect4.id, 12)

    def test_more_than_5_args(self):
        """Test that an exception is raised when objects of this class are
        instantiated with more than 5 arguments"""

        with self.assertRaises(TypeError):
            Rectangle(10, 15, 3, 4, 12, 7)

    def test_private_attributes(self):
        """Tests that the private attributes of instances can only be
        accessed outside the class using their getter and setter methods"""

        with self.assertRaises(AttributeError):
            print(self.Rect1.__width)
            print(self.Rect1.__height)
            print(self.Rect1.__x)
            print(self.Rect1.__y)

    def test_setter_methods(self):
        """Tests that the setter methods of this class properly assign values
        to the respective private attributes"""

        self.Rect6 = Rectangle(10, 15, 3, 4)
        self.Rect6.width = 58
        self.Rect6.height = 46
        self.Rect6.x = 8
        self.Rect6.y = 9
        self.assertEqual(self.Rect6.width, 58)
        self.assertEqual(self.Rect6.height, 46)
        self.assertEqual(self.Rect6.x, 8)
        self.assertEqual(self.Rect6.y, 9)
