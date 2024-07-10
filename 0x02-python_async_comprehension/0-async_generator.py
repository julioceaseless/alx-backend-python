#!/usr/bin/env python3
"""
Async generator
"""
import asyncio
import random


async def async_generator():
    """
    Generate 0 - 10
    """
    for num in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
