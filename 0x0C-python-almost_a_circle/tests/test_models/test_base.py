#!/usr/bin/python3
""" Unittest for Base class """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test cases for Base class """

    def test_instance_id(self):
        """ Test if id attribute is assigned correctly """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        """ Test to_json_string method """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')
