#!/usr/bin/env python3
"""a test for utils module's access_nested_map"""
import unittest
from utils import access_nested_map as anm
from typing import Dict, Tuple, Union
from parameterized import parameterized


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


if __name__ == '__main__':
    unittest.main()
