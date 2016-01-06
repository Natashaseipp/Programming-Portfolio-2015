#!/usr/bin/env python
sticks = 50

print "There are 50 sticks, you can take 1-6 number of sticks at a time."
print "Whoever will take the last stick will loose"

while True:
	print "Sticks left: " , sticks
	sticks_taken = int(raw_input("Take sticks(1-6):"))
	if sticks == 1:
		print "You took the last stick, you suck"
		break
	if sticks_taken >= 7 or sticks_taken <= 0:
		print "Error: you cant choose that number of sticks"
		continue
	print "Computer took: " , (7 - sticks_taken) , "n\n"
	sticks -=5
	