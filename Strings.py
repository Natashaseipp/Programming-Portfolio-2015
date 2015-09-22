#!/usr/bin/env python
s = raw_input("Please enter a string: ")
z = s[::-1]
if s == z:
	print "The strong is a palindrome"
else:
	print "The string is not palindrome"
	
#!/usr/bin/env python
s = raw_input("Enter a line: ")
print "The number of words in the lines are %d" % (len(s.split(" ")))

