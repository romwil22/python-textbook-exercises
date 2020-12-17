"""Download a copy of the file www.py4e.com/code3/words.txt
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary."""
import random

# Read text file
fileread = open('words.txt')
words_dict = dict()

#  traverse the read file
for line in fileread:
    words = line.split()

    # put  split list words into dictionaries variable
    for word in words:
        if word in words_dict:
            continue
        words_dict[word] = random.randint(1, 100)  # Generate random numbers

# Output dictionaries
print(words_dict)
