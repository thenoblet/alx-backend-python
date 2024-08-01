#!/usr/bin/env python3

"""
This module provides a utility function for converting a key-value pair.

It includes the function `to_kv` which takes a key and a value,
and returns a tuple containing the key and the square of the value.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a key-value pair into a tuple with the key and the
    square of the value.

    This function takes a string `k` as the key and a number `v`
    (either integer or floating-point) as the value.
    It returns a tuple where the first element is the key and the second
    element is the square of the value.

    Parameters:
    k (str): The key as a string.
    v (Union[int, float]): The value to be squared, which can be either an
    integer or a floating-point number.

    Returns:
    Tuple[str, float]: A tuple where the first element is the key and the
    second element is the square of the value.
    """
    return k, v**2
