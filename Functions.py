#!/usr/bin/env python
def change(b):
	a = 90
	print a
a = 9
print "Before the function call ", a
print "inside change function",
change(a)
print "After the function call ", a

#!/usr/bin/env python
def change(b):
	global a
	a = 90
	print a
a = 9
print "Before the function call ", a
print "inside change function",
change(a)
print "After the function call ", a


#!/usr/bin/env python
import math

def longest_side(a,b):
	"""
	Function to find the length of the longest side of a right triangle.
	
	:arg a: Side a of the triangle
	:arg b: Side b of the triangle
	
	:return: Length of the longest side c as float
	"""
	return math.sqrt(a*a + b*b)
	
if __name__ == '__main__':
	print longest_side(4,5)
	