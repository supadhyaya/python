

from itertools import count
import unittest
import itertools

def iter_sample(ti,n):

    'Computes the minimum and maximum values in one-pass using only 1.5*len(data) comparisons'
    it = iter(ti)

    try:
        lo = hi = next(it)
    except StopIteration:
        raise ValueError('minmax() arg is an empty sequence')

    for x, y in (itertools.zip_longest(it, it, fillvalue=lo)):
        if x > y:
            x, y = y, x
        if x < lo:
            lo = x
        if y > hi:
            hi = y
    return lo, hi


print(iter_sample(range(100),10))

print(list(iter(range(10))))











