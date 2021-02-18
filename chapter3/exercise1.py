"""Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours"""

# User input of hours and rate
hours = input('Enter hours: ')
rate = input('Enter rate: ')
hours = float(hours)
rate = float(rate)

# payment condition base on user consume
if hours > 40:
    pay = (((hours - 40)*1.5)+40)*rate
else:
    pay = hours*rate

# result
print('Pay:', pay)
