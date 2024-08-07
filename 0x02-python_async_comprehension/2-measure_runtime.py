#!/usr/bin/env python3

"""
This module provides a function to measure the runtime of multiple
asynchronous tasks.

It includes the `measure_runtime` function, which measures the total
time taken to execute four instances of the `async_comprehension`
function concurrently.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of executing four asynchronous comprehensions
    concurrently.

    This function runs four instances of `async_comprehension` concurrently
    using `asyncio.gather` and measures the total time taken to execute all
    four tasks. It returns the elapsed time in seconds.

    Returns:
    float: The total runtime in seconds for executing the four asynchronous
    comprehensions.
    """
    start_time = time.perf_counter()

    coroutines = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)

    end_time = time.perf_counter()

    return end_time - start_time
