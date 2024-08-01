#!/usr/bin/env python3

"""
This module provides a utility function for summing elements in a list.

It includes the function `sum_list` which computes the sum of
floating-point numbers in a list.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Compute the sum of a list of floating-point numbers.

    This function takes a list of floating-point numbers and returns
    the sum of all the numbers in the list.

    Parameters:
    input_list (List[float]): A list containing floating-point
    numbers to sum.

    Returns:
    float: The sum of the floating-point numbers in the list.
    """
    return sum(input_list)
