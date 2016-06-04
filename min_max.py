
'''
Implement the method iter_sample below to make the Unit test pass. iter_sample
is supposed to peek at the first n elements of an iterator, and determine the
minimum and maximum values (using their comparison operators) found in that
sample. To make it more interesting, the method is supposed to return an
iterator which will return the same exact elements that the original one would
have yielded, i.e. the first n elements can't be missing.'''

import unittest
import itertools
from itertools import count



def iter_sample(it, n):
    # change the input to iterables
    iterable = iter(it)

    # Fetch 2 variables initially for comparison
    lowest = next(iterable)
    highest = next(iterable)

    # create an empty list to store the iterables previous state  and store the first two variables
    saved = []
    saved.append(lowest)
    saved.append(highest)

    # Peek N-2 Elements from the iterables
    for _ in range(n - 2 ):
        try:
            el = next(iterable)
            if el < lowest:
                lowest = el
            if el > highest:
                highest = el
            saved.append(el)
        except StopIteration:
            return lowest, highest, itertools.chain(saved, iterable)

    # Return the lowest, highest and the iterable containing the full input set
    return lowest, highest, itertools.chain(saved, iterable)



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
