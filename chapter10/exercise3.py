"""Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies."""

import string
fileread = open('mbox-short.txt')

for line in fileread:
    line = line.rstrip()
    line = line.lower()
    line = line = line.translate(str.maketrans('', '', string.punctuation))
    splitline = line.split()
    if not len(splitline) >= 1:
        continue
    print(splitline)
    print(len(splitline))
