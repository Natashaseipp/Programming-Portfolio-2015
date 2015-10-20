# python learning exercises 

# Functions
def echo(thing):
	return thing

def swap(thing1, thing2):
	return thing2, thing1

	
def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up'): ", echo('no, you shut up')
	print "testing swap('fame', 'fortune')", swap('fame', 'fortune')


#Arithmetic Functions
def reverse(x):
	return -x

def plus(a, b):
	return a + b
	
def diff(x, y):
	return x - y
	
def abs_diff(d, b):
	diff = d - b 
	if diff < 0:
		diff *= -1
	return diff

def divide(a, c):
	return a / c
	
def remainder(l, z):
	return l % z

def power(l, t):
	answer = 1
	for i in range(t):
		answer *= l
		
def calculate(a, b, c, d, e):
	return (a + b / d - e) * c
	
def ratio(f1, f2):
	if f1 > f2: 
		return f1 / f2
	else:
		return f2 / f1
		
def pythagoras(a, b):
	return (a**2 + b**2)**(.5)

def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "testing plus(1, 1): ", plus(1, 1)
	print "testin' diff(12, 5): ", diff(12, 5)
	print "test abs_diff(10, 5): ", abs_diff(10, 5)
	print "test abs_diff(5, 10): ", abs_diff(5, 10)
	print "test divide(21, 7): ", divide(21, 7)
	print "test divide(126, 18): ", divide(126, 18)
	print "test remainder(20, 18): ", remainder(20, 18)
	print "test remainder(126, 18): ", remainder(126, 18)
	print "test power(2, 3): ", power(2, 3)
	print "test calculate(1, 2, 3, 4, 5): ", calculate(1, 2, 3, 4, 5)
	print "test ratio(7.7, 2.8): ", ratio(7.7, 2.8)
	print "test ratio(2.8, 7.7): ", ratio(2.8, 7.7)
	print "test pythagoras(3, 4): ", pythagoras(3, 4)
	print "test pythagoras(28, 32): ", pythagoras(28, 32)

def main():
	main_function()
	main_arithmetic()
	
main()