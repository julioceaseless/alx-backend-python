#!/usr/bin/env python3
"""
Task 101: TypeVar
"""
from typing import TypeVar, Any, Optional, Mapping, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Annotate the function
    """
    if key in dct:
        return dct[key]
    else:
        return default
