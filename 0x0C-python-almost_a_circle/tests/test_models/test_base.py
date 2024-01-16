#!/usr/bin/python3
"""Unittests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class.

    Methods:
        test_init(self): Test the initialization of Base.
        test_nb_objects(self): Test the __nb_objects attribute.
        test_custom_id(self): Test creating Base instance with a custom id.
        test_to_dict(self): Test the to_dict method.
        test_to_json_string(self): Test the to_json_string method.
        test_from_json_string(self): Test the from_json_string method.
        test_create(self): Test the create method.
    """

    def test_init(self):
        """Test the initialization of Base."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_nb_objects(self):
        """Test the __nb_objects attribute."""
        b1 = Base()
        self.assertTrue(hasattr(b1, '_Base__nb_objects'))
        self.assertEqual(type(b1)._Base__nb_objects, 1)

        b2 = Base()
        self.assertEqual(type(b1)._Base__nb_objects, type(b2)._Base__nb_objects)

        b3 = Base()
        self.assertEqual(type(b2)._Base__nb_objects, type(b3)._Base__nb_objects)

    def test_custom_id(self):
        """Test creating Base instance with a custom id."""
        b1 = Base(42)
        self.assertEqual(b1.id, 42)

    def test_to_dict(self):
        """Test the to_dict method."""
        b1 = Base(1)
        b_dict = b1.to_dict()
        self.assertIsInstance(b_dict, dict)
        self.assertIn('id', b_dict)
        self.assertEqual(b_dict['id'], 1)

    def test_to_json_string(self):
        """Test the to_json_string method."""
        b1 = Base(1)
        json_str = b1.to_json_string([{'id': 1}])
        self.assertIsInstance(json_str, str)
        self.assertEqual(json_str, '[{"id": 1}]')

    def test_from_json_string(self):
        """Test the from_json_string method."""
        b1 = Base(1)
        json_str = b1.to_json_string([{'id': 1}])
        obj_list = b1.from_json_string(json_str)
        self.assertIsInstance(obj_list, list)
        self.assertEqual(obj_list, [{'id': 1}])

    def test_create(self):
        """Test the create method."""
        b1 = Base(1)
        b_dict = {'id': 1}
        b2 = b1.create(**b_dict)
        self.assertIsInstance(b2, Base)
        self.assertEqual(b1, b2)
        self.assertIsNot(b1, b2)

if __name__ == '__main__':
    unittest.main()
