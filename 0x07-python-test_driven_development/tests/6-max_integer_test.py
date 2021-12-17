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
    def test_max_end(self):
        """
        Tests max at the end
        """
        self.assertAlmostEqual(max_integer([1, 3, 2, 4]), 4)
    def test_max_beginning(self):
        """
        tests max at the beginning
        """
        self.assertAlmostEqual(max_integer([10, 8, 6, 4]), 10)
    def test_max_middle(self):
        """
        tests max in the middle
        """
        self.assertAlmostEqual(max_integer([34, 32, 39, 38]), 39)
    def test_none(self):
        """
        tests none argument
        """
        self.assertAlmostEqual(max_integer([]), None)
    def test_one_arg(self):
        """
        tests one argument in list
        """
        self.assertAlmostEqual(max_integer([32]), 32)
    def test_one_neg(self):
        """
        tests when one negative integer in list
        """
        self.assertAlmostEqual(max_integer([10, 5, -80, 4]), 10)
    def test_all_neg(self):
        """
        Tests when list has all negative numbers
        """
        self.assertAlmostEqual(max_integer([-8, -4, -3, -10]), -3)
