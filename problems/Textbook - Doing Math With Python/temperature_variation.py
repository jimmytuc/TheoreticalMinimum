
"""
Temperature Variation

This is my solution to the "Temperature Variation" problem. [1] Here, we are tasked to "find the
temperature at different points of the day" and "create a graph with the time on the x-axis and
the corresponding temperature on the y-axis." of two cities of our choice.


[1] Saha, A. (2015). Doing Math with Python: Use Programming to Explore Algebra, Statistics, 
Calculus, and More! San Francisco: No Starch Press (Ch. 2, Challenge #1).
"""

import sys, datetime
import numpy as np
import matplotlib.pyplot as plt


new_york_temp_sample = [65, 66, 65, 65, 66, 65, 65, 65, 65, 64, 65, 65, 65, 65, 67, 69, 71, 74, 76, 78, 79, 79, 78, 79, 79, 78, 76]
las_vegas_temp_sample = [78, 77, 76, 75, 74, 72, 71, 71, 70, 69, 68, 67, 67, 69, 71, 72, 74, 75, 76, 77, 77, 77, 77, 75, 71, 68, 70]

if __name__ == '__main__':
	plt.figure()

	years = range(2001, 2028) # cos' we don't want to be off-by-one
	plt.plot(years, new_york_temp_sample, color='blue')
	plt.plot(years, las_vegas_temp_sample, color='green')
	plt.xlabel('Time Series')
	plt.ylabel('Temperature')
	plt.xlim(2000, 2027)
	plt.title('Matplotlib Time Series Example')
	plt.show()
