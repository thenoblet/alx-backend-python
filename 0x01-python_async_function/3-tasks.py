#!/usr/bin/env python3

"""
Import wait_random from 0-basic_async_syntax.
"""

import asyncio
from typing import Task

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    This function returns an asyncio.Task object
    """
    return asyncio.create_task(wait_random(max_delay))
