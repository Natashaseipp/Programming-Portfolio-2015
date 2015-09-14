#!/usr/bin/env python
days = int(raw_input("Enter days: "))
months = days / 30
days = days % 30
print "Months = %d Days = %d" % (months, days)

#!/usr/bin/env python
a = 9
b = 12
c = 3
x = a - b / 3 + c * 2 - 1
y = a - b / (3 + c) * (2 - 1)
z = a - (b / (3 + c) * 2) - 1
print "X = ", x
print "Y = ", y
print "Z = ", z

#!/usr/bin/env python
sum = 0.0
for i in range(1, 11):
  sum += 1.0 / i
print "%2d %6.4f" % (i , sum)

#!/usr/bin/env python
basic_salary = 1500
bonus_rate = 200
commision_rate = 0.02
numberofcamera = int(raw_input("Enter the number of inputs sold: "))
price = float(raw_input("Enter the total prices: "))
bonus = (bonus_rate * numberofcamera)
commision = (commision_rate * numberofcamera * price)
print "Bonus		= %6.2f" % bonus
print "Commision	= %6.2f" % commision
print "Gross salary = %6.2f" % (basic_salary + bonus + commision)
