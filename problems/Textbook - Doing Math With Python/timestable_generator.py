
"""
Enhanced Multiplication Table Generator [1]

This is my solution to the "Enhanced Multiplication Table Generator" problem. We are presented
with a "Multiplication Table Generator" which prints the first 10 multiples of 2. The task at
hand is to extend the functionality of the original generator to an integer k for n multiples.


[1] Saha, A. (2015). Doing Math with Python: Use Programming to Explore Algebra, Statistics, 
Calculus, and More! San Francisco: No Starch Press (Ch. 1, Challenge #2).
"""

import sys

if __name__ == '__main__':
	k, n = None, None
	try:
		k = int(raw_input("Enter an arbitrary integer: "))
		n = int(raw_input("Up to how many multiples?: "))
	except:
		print "Please enter an integer"
		sys.exit()

	print "{0} multiples of {1}...".format(n, k)
	for i in range(n):
		print "{0} X {1} = {2}".format(k, i, k * i)
