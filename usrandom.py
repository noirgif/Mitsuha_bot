"""
    usrandom.py: user defined random functions
"""
import random

def choice(iterable):
    return iterable[random.randint(0, len(iterable) - 1)]
