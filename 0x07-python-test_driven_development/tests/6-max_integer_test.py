#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case for the max_integer_function
    """

    def test_max_int(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_float(self):
        self.assertEqual(max_integer([1, 2, 3.1]), 3.1)

    def test_neg(self):
        self.assertEqual(max_integer([-1, -3, -5, -4,]), -1)

    def test_mixed(self):
        self.assertEqual(max_integer([-1000, 2.5, 50, -50.1 * -2]), 100.2)

    """ TypeError """

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, '2'])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)
