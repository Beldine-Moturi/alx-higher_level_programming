#!/usr/bin/python3
"""
This module provides test cases for the 6-max_integer module
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    This class provides methods to test the max_integer function
    """
    def test_integer_list(self):
        """
        This method tests correct output when a list of integers is provided
        """
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([10, 8, 6, 4]), 10)
        self.assertAlmostEqual(max_integer([34, 32, 33, 38]), 38)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([32]), 32)
        self.assertAlmostEqual(max_integer([10, 5, -80, 4]), 10)
        self.assertAlmostEqual(max_integer([-8, -4, -3, -10]), -3)

    def test_type(self):
        """
        This method tests for correct type(list of integers) given as the
        function argument
        """
        self.assertRaises(TypeError, max_integer, 'string')
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, 3+5j)

    def test_list_values(self):
        """
        This method tests for correct values(integers or floats only) given in
        the list argument
        """
        self.assertRaises(TypeError, max_integer, [1, 2, 'string', 4])
        self.assertRaises(TypeError, max_integer, [3, True, 6, 8])
