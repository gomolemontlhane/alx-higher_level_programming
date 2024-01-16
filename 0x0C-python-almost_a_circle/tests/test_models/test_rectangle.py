#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class.

    Methods:
        test_init(self): Test the initialization of Rectangle.
        test_area(self): Test the area method.
        test_display(self): Test the display method.
        test_str(self): Test the __str__ method.
        test_update(self): Test the update method.
        test_to_dictionary(self): Test the to_dictionary method.
    """

    def test_init(self):
        """Test the initialization of Rectangle."""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)
        self.assertEqual(r2.id, 6)

    def test_area(self):
        """Test the area method."""
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)

        r2 = Rectangle(5, 7, 2, 8)
        self.assertEqual(r2.area(), 35)

    def test_display(self):
        """Test the display method."""
        r1 = Rectangle(2, 3)
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r1.display()
            output = mock_stdout.getvalue()
            self.assertEqual(output, '##\n##\n##\n')

        r2 = Rectangle(3, 2, 1, 1)
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r2.display()
            output = mock_stdout.getvalue()
            self.assertEqual(output, '\n ###\n ###\n')

    def test_str(self):
        """Test the __str__ method."""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), '[Rectangle] (2) 1/0 - 5/5')

    def test_update(self):
        """Test the update method."""
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')

        r1.update(89, 2)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/10')

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/3')

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/10 - 2/3')

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/5 - 2/3')

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        r1 = Rectangle(10, 2, 1, 9)
        r_dict = r1.to_dictionary()
        self.assertIsInstance(r_dict, dict)
        self.assertIn('id', r_dict)
        self.assertIn('width', r_dict)
        self.assertIn('height', r_dict)
        self.assertIn('x', r_dict)
        self.assertIn('y', r_dict)
        self.assertEqual(r_dict['id'], 1)
        self.assertEqual(r_dict['width'], 10)
        self.assertEqual(r_dict['height'], 2)
        self.assertEqual(r_dict['x'], 1)
        self.assertEqual(r_dict['y'], 9)


if __name__ == '__main__':
    unittest.main()
