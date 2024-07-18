#!/usr/bin/env python3
"""
Annotate
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    make a list of tuples
    """
    return [(i, len(i)) for i in lst]
