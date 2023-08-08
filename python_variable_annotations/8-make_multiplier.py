#!/usr/bin/env python3
"""Complex types - functions"""


def make_multiplier(multiplier: float) -> float:
    """Returns a function that multiplies a float by multiplier"""
    return lambda x: x * multiplier
