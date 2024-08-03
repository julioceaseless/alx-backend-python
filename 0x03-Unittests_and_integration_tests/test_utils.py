#!/usr/bin/env python3
"""
Unit tests
"""
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from unittest.mock import patch, Mock

from utils import (
    get_json,
    access_nested_map,
    memoize
)


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
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int]
            ) -> None:
        """test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
       ({}, ("a",), KeyError),
       ({"a": 1}, ("a", "b"), KeyError)
       ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception
            ) -> None:
        """Check if KeyError is raised"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests the `get_json` function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Tests `get_json`'s output."""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""
    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()


'''
class TestGetJson(unittest.TestCase):
    """
    Mock http calls
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests.get')
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            mock_get):
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


class TestMemoize(unittest.TestCase):
    """Use memoize"""
    def test_memoize(self):
        """Test the memoize decorator"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass,
                          'a_method',
                          return_value=42) as mock_method:
            # create an instance of TestClass
            obj = TestClass()

            # Call a_property twice
            result1 = obj.a_property
            result2 = obj.a_property

            # Check that a_property returns the correct result
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Check that a_method is called only once
            mock_method.assert_called_once()
'''

if __name__ == "__main__":
    unittest.main()
