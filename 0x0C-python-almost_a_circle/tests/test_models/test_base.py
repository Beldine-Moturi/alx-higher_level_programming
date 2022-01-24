#!/usr/bin/python3
"""
Contains unittests for the Base class
"""
import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """Tests that objects of the class are properly Instantiated"""

    def test_no_id(self):
        """Tests whether id is assigned automatically when node is provided
        when creating the object the class"""
        base_1 = Base()

        self.assertEqual(base_1.id, 1)

if __name__ == "__main__":
    unittest.main()
