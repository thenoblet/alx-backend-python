#!/usr/bin/env python3

"""
This module provides basic string manipulation operations.

It includes a function `concat` that concatenates two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings.

    This function takes two strings as input and returns a new string that
    is the concatenation of the two input strings.

    Parameters:
    str1 (str): The first string to concatenate.
    str2 (str): The second string to concatenate.

    Returns:
    str: A new string formed by combining `str1` and `str2`.
    """
    return str1 + str2
