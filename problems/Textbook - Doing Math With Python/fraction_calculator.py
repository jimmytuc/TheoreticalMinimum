
"""
Fraction Calculator

This is my solution to the "Fraction Calculator" problem. [1] Here, we are tasked to develop 
a calculator programme that can "preform basic mathematical operations on two fractions". 


[1] Saha, A. (2015). Doing Math with Python: Use Programming to Explore Algebra, Statistics, 
Calculus, and More! San Francisco: No Starch Press (Ch. 1, Challenge #4).
"""

import sys
from decimal import Decimal, getcontext
from fractions import Fraction

def processor(expression):
	# first split the operator
	operator_p = None
	operators = ["plus", "minus", "times", "divide by"]
	for n, i in enumerate(operators):
		if i not in expression:
			continue
		else:
			operator_p = n
	# then format the fraction
	f = expression.split(operators[operator_p])
	f_1, f_2 = f[0].split('/'), f[1].split('/')
	ff_1n, ff_1d, ff_2n, ff_2d = int(f_1[0]), int(f_1[1]), int(f_2[0]), int(f_2[1])
	fraction_x, fraction_y = Fraction(ff_1n, ff_1d), Fraction(ff_2n, ff_2d)
	# finally preform the binary action
	if operator_p == 0:
		print "\n\n\t",fraction_x,"plus",fraction_y,"gives us:",fraction_x + fraction_y,"\n\n"
	elif operator_p == 1:
		print "\n\n\t",fraction_x,"minus",fraction_y,"gives us:",fraction_x - fraction_y,"\n\n"
	elif operator_p == 2:
		print "\n\n\t",fraction_x,"times",fraction_y,"gives us:",fraction_x * fraction_y,"\n\n"
	elif operator_p == 3:
		print "\n\n\t",fraction_x,"divided by",fraction_y,"gives us:",fraction_x / fraction_y,"\n\n"
	else:
		print "Unable to parse expression..."
	print "Unable to parse expression..."

if __name__ == '__main__':
	try:
		done = False
		print "========================================================================="
		print "= Simple Fraction Calculator"
		print "= \tBy: Alexander Ahmann [https://keybase.io/hackermaneia]"
		print "========================================================================="
		print "\n"
		while not done:
			print "Directions:"
			print "\tSyntax (a/b) operator (c/b)"
			print "\tExample: 1/2 plus 1/2........."
			print "\t........should give us 1, etc.\n"
			print "Operators:"
			print "\tAddition -> plus"
			print "\tSubtraction -> minus"
			print "\tMultiplication -> times"
			print "\tDivision -> divide by"
			print "Type 'quit' to quit"

			expression2process = raw_input('Expression to compute: ')
			if expression2process == 'quit':
				done = True
			else:
				processor(expression2process)
				raw_input( "Press [ENTER] to continue..." )
	except:
		print sys.exc_info()[0]
