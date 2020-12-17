"""Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:"""

#User input
hours = input('Enter hours: ')
rate = input('Enter rate: ')

#Condition
try:
    #convert
    hours = float(hours)
    rate = float(rate)
    if hours > 40:
        pay = (((hours - 40)*1.5)+40)*rate
    else:
        pay = hours*rate
    print('Pay:', pay)
except:
    #input error acure
    try:
        if type(hours) == type(str(hours)) and type(float(rate)) == type(float(rate)):
            print('Inavalid hours input')
        else:
            print('Inavalid rate input')
    except:
        print('Hours and rate invalid input')
