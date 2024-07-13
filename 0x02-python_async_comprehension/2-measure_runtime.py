#!/usr/bin/env python3
"""
Task 2: Async comprehension
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times and measures the
    total execution time.
    """
    # start time
    start_time = time.time()

    # create a list of tasks to run concurrently
    tasks = [async_comprehension() for i in range(4)]

    # run the tasks
    results = await asyncio.gather(*tasks)

    # return time lapse
    return time.time() - start_time
