#!/usr/bin/env python3
"""
Unit tests
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json, access_nested_map

# access_nested_map = __import__('utils').access_nested_map
# get_json = __import__('utils').get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test access for nested map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
       ({}, ("a",)),
       ({"a": 1}, ("a", "b"))
       ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Check if KeyError is raised"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Mock http calls
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Mock test"""
        # define mock response data
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # call the function under the test
        result = get_json(test_url)

        # check that the requests.get method is called once
        mock_get.assert_called_once_with(test_url)

        # check that the result is as expected
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
