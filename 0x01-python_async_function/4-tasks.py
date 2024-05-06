#!/usr/bin/env python3
""" tasks """

import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """ Take the code from wait_n and alter it into a new function task_wait_n
    The code is nearly identical to wait_n except task_wait_random
    is being called."""
    delays = [task_wait_random(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
