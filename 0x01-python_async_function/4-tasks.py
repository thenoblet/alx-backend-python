#!/usr/bin/env python3

"""
Task details:

Take the code from wait_n and alter it into a new function task_wait_n. The
code is nearly identical to wait_n except task_wait_random is being called.
"""

from typing import List
import asyncio


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously wait for `n` tasks and return the list of
    delays in the order they complete.
    """

    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
