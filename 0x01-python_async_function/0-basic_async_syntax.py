#!/usr/bin/env python3

"""
This module provides an asynchronous function for generating a random delay.

It includes the `wait_random` function, which asynchronously waits for a
random delay within a specified maximum duration.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay between 0 and `max_delay` seconds.

    This function generates a random float number between 0 and `max_delay`
    (inclusive) and returns it.
    Although it doesn't actually include an `await` statement to simulate
    waiting, it can be used in an asynchronous context.

    Parameters:
    max_delay (int, optional): The maximum delay duration in seconds.
    Defaults to 10.

    Returns:
    float: The random delay duration generated.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
