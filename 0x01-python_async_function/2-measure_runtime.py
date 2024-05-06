#!/usr/bin/env python3
""" Measure the runtime """

from asyncio import run
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime of wait_n """
    start = time()

    run(wait_n(n, max_delay))

    stop = time()
    total_time = stop - start

    return total_time / n
