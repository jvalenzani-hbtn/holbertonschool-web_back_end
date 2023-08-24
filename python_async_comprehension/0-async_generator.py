#!/usr/bin/env python3
""" Async Generator """

import asyncio
import random


async def async_generator() -> int:
    """ Async Generator """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
