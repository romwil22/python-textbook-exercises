"""Download a copy of the file www.py4e.com/code3/romeo.txt.
Write a program to open the file romeo.txt and read it line by line. For
each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word
is not in the list, add it to the list. When the program completes, sort
and print the resulting words in alphabetical order."""

# User file input checking
openfile = None
while True:
    openfile = input('enter a text file: ')

    try:
        fileread = open(openfile)
        print()
        break

    except:
        print(openfile, 'is not in the directory')
        print()

listwords = list()

# Getting the words in text file
for line in fileread:
    linewords = line.split()

    for word in linewords:
        if word in listwords:
            continue

        listwords.append(word)


# File output with sorted list
listwords.sort()
print(listwords)
