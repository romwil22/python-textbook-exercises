# Write a program to look for lines of the form:


""" Write a program to look for lines of the form:

    New Revision: 39772
    
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer. """

import re

fhandle = None

# user file text input
while True:
    user_input = input('Enter file: ')
    try:
        fhandle = open(user_input)
        print()
        break
    except:
        print(user_input, 'invalid text file, try again')
        print()

count = 0
total = 0

# searching for new revision line and sum the numbers
for line in fhandle:
    line = line.strip()
    line = line.lower()
    number = re.findall('^n\S+ r\S+: ([0-9]+)', line)

    if not len(number) > 0:
        continue

    total += int(number[0])
    count += 1

# Output of program
print('average:', int(total/count))
print()
