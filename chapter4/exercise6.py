"""Rewrite your pay computation with time-and-a-half for overtime and
create a function called computepay which takes two parameters
(hours and rate)."""

hours = input('Enter hours: ')
rate = input('Enter rate: ')


def computepay(h, r):
    try:
        # Convert
        h = float(h)
        r = float(r)
        if h > 40:
            pay = (((h - 40)*1.5)+40)*r
            return pay
        else:
            pay = h*r
            return pay
    except:
        # Input error condition
        try:
            if type(h) == type(str(h)) and type(float(r)) == type(float(r)):
                return 'Inavalid hours input'
            else:
                return 'Inavalid rate input'
        except:
            return 'Hours and rate invalid input'


# Output
payment = computepay(hours, rate)
print(payment)
