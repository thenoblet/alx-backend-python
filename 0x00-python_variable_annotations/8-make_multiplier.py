#!/usr/bin/env python3

"""
This module provides a utility function for creating multiplier functions.

It includes the `make_multiplier` function, which takes a multiplier value
and returns a function that multiplies its input by that value.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    This function takes a floating-point number `multiplier` and returns a
    new function that, when called with a floating-point argument `x`,
    will return the product of `x` and `multiplier`.

    Parameters:
    multiplier (float): The value by which the input of the returned
    function will be multiplied.

    Returns:
    Callable[[float], float]: A function that takes a float as input and
    returns the product of that input and the multiplier.
    """
    def func(x: float) -> float:
        return x * multiplier

    return func
