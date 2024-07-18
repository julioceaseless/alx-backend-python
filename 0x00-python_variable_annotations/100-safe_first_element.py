#!/usr/bin/python3
"""
Advanced task 100
"""
from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Add type annotations to the function
    """
    if lst:
        return lst[0]
    else:
        return None
