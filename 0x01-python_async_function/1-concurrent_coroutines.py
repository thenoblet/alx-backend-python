#!/usr/bin/env python3

"""
This module provides an asynchronous function that waits for multiple
random delays.

It includes the `wait_n` function, which asynchronously waits for `n` random
delays and returns a list of these delays in the order they were completed.
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously wait for `n` random delays and return the list of delays.

    This function creates `n` tasks, each waiting for a random delay generated
    by `wait_random` with a maximum duration of `max_delay`.
    The tasks are executed concurrently, and the function returns a list of
    delays in the order they are completed.

    Parameters:
    n (int): The number of tasks to create.
    max_delay (int): The maximum delay duration in seconds for each task.

    Returns:
    List[float]: A list of delays in the order they were completed.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
