#!/usr/bin/env python3
"""
Basic annotation
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    make tuple
    """
    return (k, v*v)
