#!/usr/bin/env python3
''' Chaining multiple coroutines '''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' Chain multiple coroutines '''

    res = []
    aws = [wait_random(max_delay) for i in range(n)]
    for t in asyncio.as_completed(aws):
        res.append(await t)
    return res
