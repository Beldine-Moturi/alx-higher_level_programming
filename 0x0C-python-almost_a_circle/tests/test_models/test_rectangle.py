#!/usr/bin/python3
"""Defines Test cases for the class Rectangle"""
import io
import sys
from contextlib import redirect_stdout
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
        with self.assertRaises(TypeError):
            Rectangle(20)

    def test_optional_positional_attributes(self):
        """Tests that objects of this class can be instantiated without
        the attributes x and y; will be assigned with 0 if none
        is provided"""

        self.Rect2 = Rectangle(24, 12)
        self.assertEqual(self.Rect2.width, 24)
        self.assertEqual(self.Rect2.height, 12)
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

class TestAttributeValues(unittest.TestCase):
    """Tests that the correct values are provided for Rectangle
    instance attributes, and that appropriate exceptions are
    raised otherwise"""

    def test_width_value(self):
        """Tests that the appropriate exceptions are raised if the width
        attribute is not an integer or is not greater than 0"""

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle("10", 15, 3, 4)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(-5, 6, 1, 2)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(0, 15, 3, 4)

    def test_height_value(self):
        """Tests that the appropriate exceptions are raised if the height
        attribute is not an integer or is not greater than 0"""

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(10, "15", 3, 4)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(12, -10, 1, 2)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(12, 0, 1, 2)

    def test_x_value(self):
        """Tests whether appropriate exceptions are raised if the x value
        is not an integer or is less than 0"""

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(10, 12, "3", 4)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(10, 15, -3, 4)

    def test_y_value(self):
        """Tests whether the appropriate exceptions are raised if the y value
        is not an integer or is less than 0"""

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(10, 12, 3, "4")
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(12, 15, 3, -4)

class TestRectangleMethods(unittest.TestCase):
    """Tests whether all the methods in the Rectangle class produce
    the correct expected output when called"""

    def test_area_method(self):
        """Tests whether the area method properly calculates
        the area of the rectangle"""

        self.assertEqual(Rectangle(10, 15).area(), 10 * 15)
        self.assertEqual(Rectangle(3, 4, 1, 1).area(), 3 * 4)
        self.assertEqual(Rectangle(4, 5, 1, 2, 12).area(), 4 * 5)

    @staticmethod
    def capture_stdout(rect, method):
        """Captures what is printed to the standard output
        by Rectangle methods that print to the standard output"""

        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            if method == "print":
                print(rect)
            elif method == "display":
                rect.display()
        return (captured_output.getvalue())

    def test_display_method(self):
        """Tests that the display method prints the correct Rectangle instance
        representation to the standard output"""

        r1 = Rectangle(3, 2)
        r2 = Rectangle(3, 2, 1, 2)
        r3 = Rectangle(3, 2, 2)
        self.assertEqual(TestRectangleMethods.capture_stdout(r1, "display")
                         , '###\n###\n')
        self.assertEqual(TestRectangleMethods.capture_stdout(r2, "display")
                         , '\n\n ###\n ###\n')
        self.assertEqual(TestRectangleMethods.capture_stdout(r3, "display")
                         , '  ###\n  ###\n')

    def test_str_method(self):
        """Tests that the __str__ methods prints the expected representation
        of the Rectangle instance"""

        r1 = Rectangle(4, 5)
        r2 = Rectangle(3, 4, 1)
        r3 = Rectangle(5, 6, 1, 2)
        r4 = Rectangle(3, 4, 1, 1, 12)

        self.assertEqual(TestRectangleMethods.capture_stdout(r1, "print"),
                         f"[Rectangle] ({r1.id}) 0/0 - 4/5\n")
        self.assertEqual(TestRectangleMethods.capture_stdout(r2, "print"),
                         f"[Rectangle] ({r2.id}) 1/0 - 3/4\n")
        self.assertEqual(TestRectangleMethods.capture_stdout(r3, "print"),
                         f"[Rectangle] ({r3.id}) 1/2 - 5/6\n")
        self.assertEqual(TestRectangleMethods.capture_stdout(r4, "print"),
                         f"[Rectangle] (12) 1/1 - 3/4\n")

    def test_update_args_method(self):
        """Tests that the update method properly assigns arguments to
        each attribute of the Rectangle class, when called using *args"""

        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 5)
        self.assertListEqual([r1.id, r1.width], [89, 5])
        r1.update(89, 5, 6)
        self.assertListEqual([r1.id, r1.width, r1.height], [89, 5, 6])
        r1.update(89, 5, 6, 2)
        self.assertListEqual([r1.id, r1.width, r1.height, r1.x], [89, 5, 6, 2])
        r1.update(89, 5, 6, 2, 3)
        self.assertListEqual([r1.id, r1.width, r1.height, r1.x, r1.y],
                         [89, 5, 6, 2, 3])

    def test_update_kwargs_method(self):
        """Tests that the update method properly assgins arguments to each
        attribute of the Rectangle class when called using *kwargs"""

        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(width=15)
        self.assertEqual(r1.width, 15)
        r1.update(height=20)
        self.assertEqual(r1.height, 20)
        r1.update(x=2, y=3)
        self.assertListEqual([r1.x, r1.y], [2, 3])
        r1.update(width=4, y=1, height=5, x=1)
        self.assertListEqual([r1.width, r1.height, r1.x, r1.y], [4, 5, 1, 1])
        r1.update(x=0, height=8, width=9, id=12, y=0)
        self.assertListEqual([r1.id, r1.width, r1.height, r1.x, r1.y],
                             [12, 9, 8, 0, 0])

    def test_to_dictionary_method(self):
        """Tests that the to_dictionary method return the expected
        dictionary representation of a Rectangle instance"""

        r1 = Rectangle(4, 5, 2, 3, 12)
        r2 = Rectangle(4, 5)
        r3 = Rectangle(4, 5, 2)
        r4 = Rectangle(4, 5, 2, 3)
        self.assertDictEqual(r1.to_dictionary(), {
            'x': 2,
            'y': 3,
            'id': 12,
            'height': 5,
            'width': 4
        })
        self.assertDictEqual(r2.to_dictionary(), {
            'x': 0,
            'y': 0,
            'id': r2.id,
            'height': 5,
            'width': 4
        })
        self.assertDictEqual(r3.to_dictionary(), {
            'width': 4,
            'height': 5,
            'x': 2,
            'y': 0,
            'id': r3.id
        })
        self.assertDictEqual(r4.to_dictionary(), {
            'x': 2,
            'y': 3,
            'id': r4.id,
            'width': 4,
            'height': 5
        })
