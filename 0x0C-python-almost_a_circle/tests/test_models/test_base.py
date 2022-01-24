#!/usr/bin/python3
"""
Contains unittests for the Base class methods
"""
import unittest
from models.base import Base


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

if __name__ == "__main__":
    unittest.main()
