"""Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter)."""

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

# Looking for date idex
dict_dates = dict()
for line in fileread:
    line = line.lower()

    if not line.startswith('from'):
        continue

    lst_words = line.split()

    if len(lst_words)-1 <= 1:
        continue

    date = lst_words[2]
    dict_dates[date] = dict_dates.get(date, 0) + 1  # Counting the date

# Output dictionary of dates
print(dict_dates)
