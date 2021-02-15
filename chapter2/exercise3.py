"""Write a program to prompt the user for hours and rate per
hour to compute gross pay."""

# Asking user input for hours and rate
hours = input('Enter hours: ')
hours = float(hours)
rate = input('Enter rate: ')
rate = float(rate)
# Computation for payment
gross_pay = hours * rate
print('Pay:', round(gross_pay, 2))
