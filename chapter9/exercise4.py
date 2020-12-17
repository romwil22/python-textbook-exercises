"""Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and
the dictionary has been created, look through the dictionary using
a maximum loop (see Chapter 5: Maximum and minimum loops) to find
who has the most messages and print how many messages the person has.
"""

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
    dict_emails[mail] = dict_emails.get(mail, 0) + 1  # Counting the mails


def mostemail(dct):
    most_count = None
    most_email = None

    # Looking for the most email message
    for key in dct:
        if most_count is None or dct[key] > most_count:
            most_count = dct[key]
            most_email = key
    print(most_email, most_count)


# Output for most email receive
mostemail(dict_emails)
