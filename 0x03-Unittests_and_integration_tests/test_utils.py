#!/usr/bin/env python3

"""
Unit Testing for access_nested_map Function

This module provides a set of unit tests for the `access_nested_map` function
from the `utils` module. The tests are parameterized to cover different cases
of nested dictionary access. The `parameterized` library is used to run the
same test function with different sets of input data.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the `access_nested_map` function.

    The `test_access_nested_map` method is parameterized to test different
    scenarios of accessing nested dictionaries.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Tests the `access_nested_map` function with different parameter sets.

        Args:
            nested_map: The nested dictionary to be accessed.
            path: The path (tuple of keys) to access the value in the nested
                  dictionary.
            expected: The expected value returned by `access_nested_map`.

        Asserts:
            The result of `access_nested_map(nested_map, path)` equals the
            expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Tests that `access_nested_map` raises a KeyError for invalid paths.

        Args:
            nested_map: The nested dictionary to be accessed.
            path: The path (tuple of keys) to access the value in the nested
                  dictionary.

        Asserts:
            A KeyError is raised when attempting to access a non-existent
            path in the nested dictionary.
        """
        # self.assertRaises(KeyError, access_nested_map, nested_map, path)
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
