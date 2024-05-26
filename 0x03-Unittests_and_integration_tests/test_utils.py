#!/usr/bin/env python3
"""a test for utils module's access_nested_map"""
import unittest
from utils import access_nested_map as anm, get_json, memoize
from typing import Dict, Tuple, Union
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """test the nested function with three level depth"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nst: Dict, path: Tuple[str], exp: Union[Dict, int]) -> None:
        """test access of nesting by three level of nesting"""
        self.assertEqual(anm(nst, path), exp)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self, nst: Dict, path: Tuple[str], exp: Exception) -> None:
        """test a key error input"""
        with self.assertRaises(exp):
            anm(nst, path)


class TestGetJson(unittest.TestCase):
    """ mock http calls"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: dict) -> None:
        """ test get_json """
        args = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**args)) as g_rqst:
            self.assertEqual(get_json(test_url), test_payload)
            g_rqst.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """memoization test """
    def test_memoize(self) -> None:
        """test memoize and check that it's clled once"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mocked:
            test = TestClass()
            test.a_property()
            test.a_property()
            mocked.assert_called_once()


if __name__ == '__main__':
    unittest.main()
