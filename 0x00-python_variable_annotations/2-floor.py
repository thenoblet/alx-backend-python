#!/usr/bin/env python3

"""
This module provides basic mathematical operations.

It includes a function `floor` that converts a floating-point number
to an integer by truncating the decimal part.
"""


def floor(n: float) -> int:
    """
    Convert a floating-point number to an integer by truncating the
    decimal part.

    This function takes a floating-point number as input and returns
    the largest integer less than or equal to the input
    It effectively truncates the decimal portion of the number.

    Parameters:
    n (float): The floating-point number to convert.

    Returns:
    int: The integer value obtained by truncating the decimal part of `n`.
    """
    return int(n)
