#!/usr/bin/env python3
"""
Test
"""

access_nested_map = __import__('utils').access_nested_map

nested_map = {"a": {"b": {"c": 1}}}

print(access_nested_map(nested_map, ["a", "b", "c"]))
