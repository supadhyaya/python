from itertools import count
import unittest
import itertools

def iter_sample(ti, n):

    #chunk = list(ti)[:n]
    ps = iter(ti)
    #chunk = list(ti)[:n]
    #it = iter(ti)

    'Computes the minimum and maximum values in one-pass using only 1.5*len(data) comparisons'
    to = iter(ti)

    it = itertools.islice(to, n)

    dumb = itertools.chain(itertools.islice(to, n), ps)
    


    try:
        lo = hi = next(it)
    except StopIteration:
        raise ValueError('minmax() arg is an empty sequence')

    for x, y in (itertools.zip_longest(it, it, fillvalue=lo)):

        #saved.append = itertools.chain(itertools.islice(to, n), it)

        if x > y:
            x, y = y, x
        if x < lo:
            lo = x
        if y > hi:
            hi = y


    return (lo,hi,dumb)


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
		min_val, max_val, new_it = iter_sample(it, 100)

		self.assertEqual(0, min_val)
		self.assertEqual(99, max_val)
		#self.assertEqual(list(range(100)), list(new_it))

	def test_infinite_stream(self):

		# and guess what - it also works with infinite iterators

		it = count(0)
		min_val, max_val, _ = iter_sample(it, 10)

		self.assertEqual(0, min_val)
		self.assertEqual(9, max_val)

if __name__ == "__main__":
	unittest.main()
