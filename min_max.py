
'''
Implement the method iter_sample below to make the Unit test pass. iter_sample
is supposed to peek at the first n elements of an iterator, and determine the
minimum and maximum values (using their comparison operators) found in that
sample. To make it more interesting, the method is supposed to return an
iterator which will return the same exact elements that the original one would
have yielded, i.e. the first n elements can't be missing.'''

from itertools import count
import unittest
import itertools

def iter_sample(ti, n):

    it = itertools.islice(iter(ti),n)

    saved = []

    for i in it:
        saved.append(i)

    min_max = iter(saved)

    try:
        lo = hi = next(min_max)
    except StopIteration:
        raise ValueError('minmax() arg is an empty sequence')

    for x, y in (itertools.zip_longest(min_max, min_max, fillvalue=lo)):
        if x > y:
            x, y = y, x
        if x < lo:
            lo = x
        if y > hi:
            hi = y


    return (lo,hi,itertools.chain(iter(saved), iter(ti)))


class StreamSampleTestCase(unittest.TestCase):

	def test_smoke(self):

		# sample only the first 10 elements of a range of length 100

		it = iter(range(100))
		min_val, max_val, new_it = iter_sample(it, 10)

		self.assertEqual(0, min_val)
		self.assertEqual(9, max_val)
		# all elements are still there:
		self.assertEqual(list(range(100)), list(new_it))

	def test_sample_all(self):

		# sample more elements than there are - no error raised
		# now we now the global maximum!

		it = iter(range(100))
		min_val, max_val, new_it = iter_sample(it, 1000)

		self.assertEqual(0, min_val)
		self.assertEqual(99, max_val)
		self.assertEqual(list(range(100)), list(new_it))

	def test_infinite_stream(self):

		# and guess what - it also works with infinite iterators

		it = count(0)
		min_val, max_val, _ = iter_sample(it, 10)

		self.assertEqual(0, min_val)
		self.assertEqual(9, max_val)

if __name__ == "__main__":
	unittest.main()
