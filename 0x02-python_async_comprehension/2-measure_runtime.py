#!/usr/bin/env python3
"""a python module to measure the execution time"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the total runtime for four time and return it
    """
    start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    stop = time.perf_counter()
    return (stop - start)
