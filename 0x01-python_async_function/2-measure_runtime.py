#!/usr/bin/env python3
''' Measuring total execution time for coroutines '''
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Returns total execution time for a chain of coroutines '''

    start = time.perf_counter()
    res = asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return ((end - start) / n)
