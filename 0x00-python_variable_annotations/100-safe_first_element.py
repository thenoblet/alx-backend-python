#!/usr/bin/env python3

"""
This module provides a utility function for safely retrieving
the first element of a sequence.

It includes the `safe_first_element` function, which returns the first
element of a sequence if it exists, or `None` if the sequence is empty.
"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieve the first element of a sequence.

    This function returns the first element of the provided sequence
    if it exists.
    If the sequence is empty, the function returns `None`.

    Parameters:
    lst (Sequence): A sequence (such as a list, tuple, or string) from
    which to retrieve the first element.

    Returns:
    Union[Any, None]: The first element of the sequence if available;
    otherwise, `None`.
    """
    if lst:
        return lst[0]
    else:
        return None
