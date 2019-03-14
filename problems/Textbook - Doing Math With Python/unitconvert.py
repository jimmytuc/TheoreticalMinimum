
"""
Enhanced Unit Converter

This is my solution to the "Enhanced Unit Converter" problem. [1] Here, we are presented with
a simple script that runs conversions between kilometres and miles. The task at hand is to ex-
tend the script to run conversions between kilograms and pounds and fahrenheit and celsius.


[1] Saha, A. (2015). Doing Math with Python: Use Programming to Explore Algebra, Statistics, 
Calculus, and More! San Francisco: No Starch Press (Ch. 1, Challenge #3).
"""

import sys
from decimal import Decimal, getcontext

getcontext().prec = 5

f_f2c = lambda x: Decimal(.5556) * Decimal(x - 32) # fahrenheit to celsius
f_c2f = lambda x: Decimal(x - 32) * Decimal(.5556) # celsius to fahrenheit
f_k2p = lambda x: Decimal(x) * Decimal(2.204600) # kilograms to pounds
f_p2k = lambda x: Decimal(x) / Decimal(2.204600) # pounds to kilograms
f_k2m = lambda x: Decimal(x) / Decimal(1.609344) # kilometres to miles
f_m2k = lambda x: Decimal(x) * Decimal(1.609344) # miles to kilometres

if __name__ == '__main__':
	try:
		done = False
		print "==============================================="
		print "= Enhanced Unit Converter"
		print "= \tBy Alexander Ahmann"
		print "==============================================="
		while not done:
			print "\nOptions to choose from:"
			print "1) Convert Fahrenheit to Celsius"
			print "2) Convert Celsius to Fahrenheit"
			print "3) Convert Kilograms to Pounds"
			print "4) Convert Pounds to Kilograms"
			print "5) Convert Kilometres to Miles"
			print "6) Convert Miles to Kilometres"
			print "7) Exit"

			operation = int(raw_input("What do you want to do? "))
			if operation == 1:
				x = Decimal(raw_input("Enter fahrenheits to convert: "))
				print "To celsius:",f_f2c(x),raw_input("\n\nPress [ENTER] to continue...")
			elif operation == 2:
				x = Decimal(raw_input("Enter celsius to convert: "))
				print "To fahrenheit:",f_f2c(x),raw_input("\n\nPress [ENTER] to continue...")
			elif operation == 3:
				x = Decimal(raw_input("Enter kilograms to convert: "))
				print "To pounds:",f_f2c(x),raw_input("\n\nPress [ENTER] to continue...")
			elif operation == 4:
				x = Decimal(raw_input("Enter pounds to convert: "))
				print "To kilograms:",f_f2c(x),raw_input("\n\nPress [ENTER] to continue...")
			elif operation == 5:
				x = Decimal(raw_input("Enter kilometres to convert: "))
				print "To miles:",f_f2c(x),raw_input("\n\nPress [ENTER] to continue...")
			elif operation == 6:
				x = Decimal(raw_input("Enter miles to convert: "))
				print "To kilometres:",f_f2c(x),raw_input("\n\nPress [ENTER] to continue...")
			elif operation == 7:
				done = True
			else:
				print "Please select an option between 1-7"
	except:
		print "Exception:",sys.exc_info()[0]
