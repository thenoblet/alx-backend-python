#!/usr/bin/env python3

"""
This module provides an asynchronous generator function.

It includes the `async_generator` function, which generates a sequence of
10 random float numbers between 0 and 10, with a 1-second delay between each.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generate 10 random float numbers between 0 and 10.

    This generator function produces a sequence of 10 random floats.
    It waits for 1 second between each number generation using
    `await asyncio.sleep(1)`.
    The function yields each float as it is generated.

    Returns:
    AsyncGenerator[float, None]: An asynchronous generator of random floats
    between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
