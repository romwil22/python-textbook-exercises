"""Write a program to read through a mail log, build
a histogram using a dictionary to count how many messages
have come from each email address, and print the dictionary."""

fileread = None

# File input
while True:
    file_input = input('Enter a file name: ')

    try:
        fileread = open(file_input)
        break
    except:
        print(file_input, 'Invalid file name, try again')
        print()

# Looking for mail idex
dict_emails = dict()
for line in fileread:
    line = line.lower()

    if not line.startswith('from'):
        continue

    lst_words = line.split()
    mail = lst_words[1]
    dict_emails[mail] = dict_emails.get(mail, 0) + 1  # Counting the mail

# Output dictionary of emails
print(dict_emails)
