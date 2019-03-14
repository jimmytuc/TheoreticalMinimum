
"""
The "Exploring Quadratic Functions Visually" Problem [1]

Here, we are given a programme that "calculates a f(x) where f(x) = x^2 + 2x + 1 (quadratic
function) for six different values of an independent variable 'x'. The task at hand is to
create a graph of the function that takes at least 10 inputs [2] and put it through the func-
tion.

[1] Saha, A. (2015). Doing Math with Python: Use Programming to Explore Algebra, Statistics, 
Calculus, and More! San Francisco: No Starch Press (Ch. 2, Challenge #2).
[2] It said 10, but I wanted to extend the domain/range for a more accurate picture.
"""

import matplotlib.pyplot as plt

f = lambda x: x**2 + 2*x + 1
if __name__ == '__main__':

	x = range(-10, 11) # 11, not 10 cos' off-by-one
	y = [f(k) for n, k in enumerate(x)]

	plt.figure()
	plt.plot(x, y)
	plt.title('Matplotlib Example')
	plt.xlabel('Range', fontsize=16)
	plt.ylabel('$y = x^2 + 2x + 1$', fontsize=20)
	plt.show()
