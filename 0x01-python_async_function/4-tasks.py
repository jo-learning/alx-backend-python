#!/usr/bin/env python3
''' Chaining multiple async tasks '''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Chain multiple coroutines '''

    res = []
    aws = [task_wait_random(max_delay) for i in range(n)]
    for t in asyncio.as_completed(aws):
        res.append(await t)
    return res
