#!/usr/bin/env python
i = 1
print "-" * 50
while i < 11:
	n = 1
	while n <= 10:
	  print "%4d" % (i * n),
	  n += 1
	print ""
	i += 1
print "-" * 50 

#!/usr/bin/env python
row = int(raw_input("Enter the number of rows: " ))
n = row
while n >= 0:
	x = "*" * n
	print x
	n -= 1
	
#!/usr/bin/env python
n = int(raw_input("Enter the number of rows: "))
i = 1 
while i <= n:
	print "*" * i
	i += 1 

#!/usr/bin/env python
row = int(raw_input("Enter the number of rows: "))
n = row
while n >= 0:
	x = "*" * n
	y = " " * (row - n)
	print y + x
	n -= 1
	
#!/usr/bin/env python
while True:
    n = int(raw_input("Please enter an Integer"))
    if n < 0:
        continue #this will take the execution back to the starting of the loop
    elif n == 0:
        break
    print "Square is ", n ** 2
print "Goodbye" 

#!/usr/bin/env python
sticks = 21

print "There are 21 sticks, you can take 1-4 number of sticks at a time."
print "Whoever will take the last stick will loose"

while True:
    print "Sticks left: " , sticks
    sticks_taken = int(raw_input("Take sticks(1-4):"))
    if sticks == 1:
        print "You took the last stick, you loose"
        break
    if sticks_taken >= 5 or sticks_taken <= 0:
        print "Wrong choice"
        continue
    print "Computer took: " , (5 - sticks_taken) , "n/n"
    sticks -= 5
    