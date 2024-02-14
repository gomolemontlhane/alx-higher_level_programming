#!/usr/bin/python3
""" Unittest for Square class """

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test cases for Square class """

    def test_attributes(self):
        """ Test if attributes are set correctly """
        s = Square(5, 1, 2, 7)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 7)

    def test_size_type_error(self):
        """ Test for size type error """
        with self.assertRaises(TypeError):
            s = Square("invalid", 1, 2, 7)

    # Add similar test cases for x, y, and id

    def test_size_value_error(self):
        """ Test for size value error """
        with self.assertRaises(ValueError):
            s = Square(-5, 1, 2, 7)

    # Add similar test cases for x, y, and id

    def test_update_args(self):
        """ Test the update method with *args """
        s = Square(10, 10, 10)
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 10")

    def test_update_kwargs(self):
        """ Test the update method with **kwargs """
        s = Square(10, 10, 10)
        s.update(size=1, id=2)
        self.assertEqual(str(s), "[Square] (2) 10/10 - 1")

    def test_to_dictionary(self):
        """ Test the to_dictionary method """
        s = Square(10, 1, 9)
        d = s.to_dictionary()
        self.assertEqual(d, {'id': 1, 'size': 10, 'x': 1, 'y': 9})
