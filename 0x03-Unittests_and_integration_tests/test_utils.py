#!/usr/bin/env python3

"""
Unit Testing for access_nested_map Function

This module provides a set of unit tests for the `access_nested_map` function
from the `utils` module. The tests are parameterized to cover different cases
of nested dictionary access. The `parameterized` library is used to run the
same test function with different sets of input data.
"""

import unittest
import requests
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """
    Unit tests for the `get_json` function.

    The `test_get_json` method is parameterized to test different scenarios
    of making HTTP GET requests and receiving JSON responses.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """
        Tests the `get_json` function with different URLs and expected
        JSON payloads.

        Args:
            url (str): The URL to send the HTTP GET request to.
            payload (Dict[str, Any]): The expected JSON payload returned
            by the URL.

        Asserts:
            The result of `get_json(url)` equals the expected payload.
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = payload

            result = get_json(url)
            self.assertEqual(result, payload)
            mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the `memoize` decorator.

    The `test_memoize` method tests that a method decorated with `memoize`
    is only called once for subsequent accesses to the decorated property.
    """

    def test_memoize(self):
        """
        Tests the `memoize` decorator functionality.

        Ensures that a method wrapped with `memoize` is only called once
        even if accessed multiple times.

        Asserts:
            The result of accessing the memoized property twice equals the
            expected value and the underlying method is called only once.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        instance = TestClass()

        with patch.object(
            instance, 'a_method', wraps=instance.a_method
        ) as mock_method:
            result1 = instance.a_property
            result2 = instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()
