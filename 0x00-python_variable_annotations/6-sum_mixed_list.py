#!/usr/bin/env python3
"""
Basic annotation
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate sum of mixed numbers in a list
    """
    return sum(mxd_lst)
