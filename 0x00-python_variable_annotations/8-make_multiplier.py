#!/usr/bin/env python3
"""
Basic annotation
"""
from typing import List, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make multiplier
    """
    def multiply(m: float) -> float:
        return m * multiplier
    return multiply
