""" Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count 
the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits."""

fileread = None

# User input text file
while True:
    file_input = input('Enter a file name: ')

    try:
        fileread = open(file_input)
        print()
        break
    except:
        print(file_input, ' invalid text file, try again')
        print()

# Emails dictionary
emailsender = dict()

# Reading file text
for line in fileread:
    line = line.lower()
    line = line.rstrip()

    if not line.startswith('from'):
        continue

    splitline = line.split()

    # Adding email to emails dictionary
    for email in splitline:
        if '@' in email:
            emailsender[email] = emailsender.get(email, 0) + 1

# List of counts and emails
lst_email = list()

# Adding the emails dictionary to list of counts and emails
for email, count in emailsender.items():
    lst_email.append((count, email))

# Sort the list from decending order
lst_email.sort(reverse=True)

# Most email output
for count, email in lst_email[:1]:
    print(email + ':', count)
