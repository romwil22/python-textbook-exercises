""" Write a simple program to simulate the operation of the
grep command on Unix. Ask the user to enter a regular expression and
count the number of lines that matched the regular expression. """

import re

# Variable container
count = 0
fhandle = None

# User input text file
while True:
    user_input = input('Enter a file name: ')

    try:
        fhandle = open(user_input)
        print()
        break
    except:
        print(user_input, ' invalid text file, try again')
        print()

# User regular exression input search
RE_var = input('Enter a regular expression: ')
print()

# Looking for line the user enter
for line in fhandle:
    line = line.strip()
    line = line.lower()
    RE_var = RE_var.lower()

    if re.search(RE_var, line):
        count += 1

# Output of the program
print(user_input, 'had', count, 'lines that matched', RE_var)
