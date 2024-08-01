#!/usr/bin/env python3

"""
This module provides a utility function for "zooming" into a tuple
by repeating its elements.

It includes the `zoom_array` function, which takes a tuple and a factor
and returns a list where each element in the tuple is repeated
according to the factor.

"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Repeat each element in a tuple to create a zoomed-in list.

    This function takes a tuple and an integer factor, and returns a
    list where each element in the tuple is repeated `factor` times.

    Parameters:
    lst (Tuple): The tuple containing elements to be repeated.
    factor (int, optional): The number of times each element should be
    repeated. Defaults to 2.

    Returns:
    List: A list with each element of the tuple repeated according
    to the factor.
    """
    zoomed_in: List = [
            item for item in lst
            for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
