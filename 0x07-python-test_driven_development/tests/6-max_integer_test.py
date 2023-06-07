#!/usr/bin/python3
"""
Unittests for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for max_integer function
    """

    def test_regular(self):
        """
        Test max_integer with a regular list of integers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_empty(self):
        """
        Test max_integer with an empty list
        """
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """
        Test max_integer with a list containing a single element
        """
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_duplicate_values(self):
        """
        Test max_integer with a list containing duplicate values
        """
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_mixed_list(self):
        """
        Test max_integer with a mixed list of integers and other types
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4])
            max_integer([1.5, 2.7, 3.2, 4.9])
            max_integer(["apple", "banana", "cherry"])


if __name__ == '__main__':
    unittest.main()
