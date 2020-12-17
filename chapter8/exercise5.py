"""Write a program to read through the mail box data and
when you find line that starts with “From”, you will split the line into
words using the split function. We are interested in who sent the
message, which is the second word on the From line."""

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

count = 0

# Searching for from lines and print-out the sender email
for line in fileread:
    lower_line = line.lower()

    if not lower_line.startswith('from'):
        continue

    line_words = line.split()

    if line_words[0] == 'From':  # Counting "From" index
        count += 1

    sender = line_words[1]
    print(sender)

message = 'There were {} lines in the file with From as the first word'.format(
    count)

print(message)
