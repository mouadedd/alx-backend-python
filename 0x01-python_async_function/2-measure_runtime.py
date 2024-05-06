#!/usr/bin/python3
"""Measure the runtime"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """count the runtime of wait_n"""
    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    stop = time.time()
    total_time = stop - start
    return total_time/n
