#!/usr/bin/env python3
"""a test for utils module's access_nested_map"""
import unittest
from utils import access_nested_map as anm
from typing import Any


class TesAccessNestedMap(unittest.TestCase):
    """test the nested function with three level depth"""

    def test_nested_number(self) -> None:
        """test 0 level of nesting"""
        self.assertEqual(anm({"a": {"b": {"c": 1}}}, ["a", "b", "c"]), 1)

    def test_one_nest(self) -> None:
        """test one level of nesting"""
        self.assertEqual(anm({"a": 1}, "a"), 1)

    def test_two_nest(self) -> None:
        """test one level of nesting with a dict as result"""
        self.assertEqual(anm({"a": {"b": 2}}, "a"), {"b": 2})

    def test_three_nest(self) -> None:
        """test three level of nesting"""
        self.assertEqual(anm({"a": {"b": 2}}, ["a", "b"]), 2)


if __name__ == '__main__':
    unittest.main()
