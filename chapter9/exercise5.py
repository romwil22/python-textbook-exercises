"""This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary."""

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

# Looking for domain idex
dct_domain = dict()
for line in fileread:
    line = line.lower()

    if not line.startswith('from'):
        continue

    words = line.split()

    # Looking for domain
    for email in words:
        if not '@' in email:
            continue

        domain = email.split('@')
        dct_domain[domain[1]] = dct_domain.get(
            domain[1], 0) + 1  # Counting the domain

# Output of domain dictionary
print()
for emaildomain in dct_domain:
    print(emaildomain + ':', dct_domain[emaildomain])
