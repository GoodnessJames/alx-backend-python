#!/usr/bin/env python3
"""Nearly identical to wait_n except task_wait_random is being called."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Take the code from wait_n and alter it into a new function.

    Args:
        n (int)
        max_delay (int)

    Returns:
        List
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]


if __name__ == "__main__":
    print(asyncio.run(task_wait_n(5, 5)))
    print(asyncio.run(task_wait_n(10, 7)))
    print(asyncio.run(task_wait_n(15, 0)))
