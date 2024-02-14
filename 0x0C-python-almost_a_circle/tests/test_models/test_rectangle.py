#!/usr/bin/python3
""" Unittest for Rectangle class """

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test cases for Rectangle class """

    def test_attributes(self):
        """ Test if attributes are set correctly """
        r = Rectangle(5, 10, 1, 2, 7)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 7)

    def test_width_type_error(self):
        """ Test for width type error """
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 10, 1, 2, 7)

    # Add similar test cases for height, x, y, and id

    def test_width_value_error(self):
        """ Test for width value error """
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10, 1, 2, 7)

    # Add similar test cases for height, x, y, and id

    def test_area(self):
        """ Test the area method """
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """ Test the display method """
        r = Rectangle(3, 2, 1, 0)
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), "\n ###\n ###\n")

    def test_str(self):
        """ Test the __str__ method """
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """ Test the update method with *args """
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_kwargs(self):
        """ Test the update method with **kwargs """
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1, id=2)
        self.assertEqual(str(r), "[Rectangle] (2) 10/10 - 10/1")

    def test_to_dictionary(self):
        """ Test the to_dictionary method """
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})
