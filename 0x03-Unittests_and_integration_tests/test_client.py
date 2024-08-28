#!/usr/bin/env python3

"""
Unit Testing for GithubOrgClient Class

This module provides a set of unit tests for the `GithubOrgClient` class
from the `client` module. The tests are designed to verify the correct
functionality of the methods in `GithubOrgClient` that interact with
the GitHub API to fetch organization data.

The `parameterized` library is used to run the same test function with
different sets of input data, ensuring a wide range of scenarios are covered.
The `unittest.mock.patch` function is utilized to mock external dependencies
like network calls to the GitHub API, allowing tests to run without actual
network access.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the `GithubOrgClient` class.

    This test class covers various scenarios for the `org` method,
    which fetches organization details from GitHub. The tests ensure
    that the method correctly calls the external API, handles different
    inputs, and manages exceptions appropriately.
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, mock_get_json):
        """
        Test the `org` method of `GithubOrgClient`.

        This test verifies that the `org` property of the `GithubOrgClient`
        correctly returns the expected organization data. It uses the
        `parameterized` decorator to run the test multiple times with
        different inputs.

        Args:
            org (str): The name of the organization to retrieve.
            expected (Dict[str, Any]): The expected dictionary returned by
            `get_json`.
            mock_get_json (Any): The mocked `get_json` function.

        Asserts:
            - The returned organization matches the expected dictionary.
            - `get_json` is called with the correct URL.
        """
        mock_get_json.return_value = expected

        client = GithubOrgClient(org)
        organisation = client.org

        url = client.ORG_URL.format(org=org)

        self.assertEqual(organisation, expected)
        mock_get_json.assert_called_once_with(url)
