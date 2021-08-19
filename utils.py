# Note: In order to import from utils with ‘from utils import *’, the utils.py file needs to be in the same folder as the notebook (at least as its defined now). 
# If the utils.py file is not in the same folder, you can use sys to append a path for the file.

def add(x, y):
	"""A function that adds two numbers and prints the output.

	Arguments:
	x -- a number
	y -- another number
	"""
	
	summed = float(x) + float(y)
	print("the sum of " + str(x) + " and " + str(y) + " is : " + str(summed))
