#!/usr/bin/env python3
"""
Python Async
"""
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """
    executes multiple coroutines at the same time with async
    """
    delays = await asyncio.gather(*(wait_random(max_delay)
                                  for _ in range(n)))
    return sorted(delays)
