#!/usr/bin/env python3

"""
This module provides a utility function for calculating the
length of elements in an iterable.

It includes the `element_length` function, which takes an iterable of
sequences and returns a list of tuples, where each tuple contains a sequence
and its corresponding length.
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each sequence in an iterable.

    This function takes an iterable containing sequences
    (e.g., strings, lists, tuples) and returns a list of tuples.
    Each tuple contains a sequence from the iterable and the length of
    that sequence.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequences whose lengths
    are to be calculated.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple consists of a
    sequence and its length.
    """
    return [(i, len(i)) for i in lst]
