#!/usr/bin/env python3

"""
This module provides a utility function for summing elements in
a mixed-type list.

It includes the function `sum_mixed_list` which computes the sum of both
integer and floating-point numbers in a list.
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Compute the sum of a list containing both integer and
    floating-point numbers.

    This function takes a list of numbers (both integers and floating-point)
    and returns the sum of all numbers in the list.
    The result is returned as a floating-point number.

    Parameters:
    mxd_list (List[Union[float, int]]): A list containing integers and/or
    floating-point numbers to sum.

    Returns:
    float: The sum of the numbers in the list, represented as a
    floating-point number.
    """
    return sum(mxd_list)
