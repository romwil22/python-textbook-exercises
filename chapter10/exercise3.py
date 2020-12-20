"""Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies."""

import string
fileread = None

# User input file text
while True:
    user_input = input('Enter file name: ')
    try:
        fileread = open(user_input)
        print()
        break
    except:
        print(user_input, 'invalid file name, try again')
        print()

# dictionary for letters
letters_dict = dict()

# Read the user file text
for line in fileread:
    line = line.rstrip()
    line = line.lower()
    line = line.translate(str.maketrans('', '', string.punctuation))
    splitline = line.split()

    if not len(splitline) >= 1:
        continue

    for index in splitline:
        lst_char = list(index)  # List of character
        for char in lst_char:
            try:
                integer = int(char)
            except:
                letters_dict[char] = letters_dict.get(char, 0) + 1

# List of letters and values
letters_list = list()

# Add the dictionaries items to List of items
for letter, count in letters_dict.items():
    letters_list.append((count, letter))

# Sort variable "letters_list" to decending order
letters_list.sort(reverse=True)

# Print the list of items in decreasing  order
for count, letter in letters_list:
    print(letter + ':', count)
