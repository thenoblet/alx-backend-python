#!/usr/bin/env python3

"""
This module provides a utility function for measuring the average execution
time of asynchronous tasks.

It includes the `measure_time` function, which measures the total execution
time of running `n` asynchronous tasks with `wait_n`, and
returns the average time per task.
"""

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int):
    """
    Measure the average execution time for running `n` asynchronous tasks
    with `wait_n`.

    This function calculates the total execution time of running `n` tasks
    using the `wait_n` function, which waits for `n` random delays.
    It then returns the average time per task.

    Parameters:
    n (int): The number of asynchronous tasks to run.
    max_delay (int): The maximum delay duration in seconds for each task.

    Returns:
    float: The average execution time per task
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    execution_time = end_time - start_time
    return execution_time / n
