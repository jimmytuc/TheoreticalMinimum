
"""
Even-Odd Vending Machine [1]

This is my solution to the "Even-Odd Vending Machine" problem in which the programmer
will write "an 'even-odd' vending machine which takes a number as input and 

	1) Print whether the number is even or odd
	2) Display the number followed by the next 9 even or odd numbers"

[1] Saha, A. (2015). Doing Math with Python: Use Programming to Explore Algebra, Statistics, 
Calculus, and More! San Francisco: No Starch Press (Ch. 1, Challenge #1).
"""

if __name__ == '__main__':
	x = int(raw_input('Enter Number: '))
	y = [x for x in range(x, x + 19, 2)]
	if ( (x + 1) % 2 == 1):	# <-- "if it's even"
		print "Even ",y
	else:
		print "Odd ",y
