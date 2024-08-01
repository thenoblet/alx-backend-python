#!/usr/bin/env python3

"""
This module provides a utility function for safely retrieving a
value from a dictionary.

It includes the `safely_get_value` function, which retrieves the value
associated with a given key from a dictionary, returning a default value
if the key is not present.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary, with a default value
    if the key is not present.

    This function checks if the specified key exists in the
    provided dictionary.
    If the key is present, it returns the corresponding value.
    If the key is not found, it returns the specified default value.

    Parameters:
    dct (Mapping[Any, Any]): The dictionary from which to retrieve the value.
    key (Any): The key whose associated value is to be retrieved.
    default (Union[T, None], optional): The default value to return if the
    key is not found. Defaults to `None`.

    Returns:
    Union[Any, T]: The value associated with the key if it exists; otherwise,
    the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
