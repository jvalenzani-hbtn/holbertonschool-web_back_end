#!/usr/bin/env python3

import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random
s = time.perf_counter()
print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
elapsed = time.perf_counter() - s
print(f"executed in {elapsed:0.2f} seconds.")
