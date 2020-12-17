"""This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below."""

fileread = None

# User input file text in directory
while True:
    file_input = input('Enter file name: ')

    try:
        fileread = open(file_input)
        break
    except:
        print(file_input, 'Invalid input, try again')
        print()

# Hours dictionary
hours_dict = dict()

# Reading user file text
for line in fileread:
    line = line.lower()

    if not line.startswith('from'):
        continue

    splitline = line.split()

    if len(splitline) - 1 <= 1:
        continue

    # Find for hour and add to hours dictionary
    for hour in splitline:
        if not ':' in hour:
            continue

        split_time = hour.split(':')

        hours_dict[split_time[0]] = hours_dict.get(split_time[0], 0) + 1

# List of hours and counts
hourslst = list()

# Adding to list of hours and count from hours dictionary
for hour, count in hours_dict.items():
    hourslst.append((hour, count))

# Sort to ascending order
hourslst.sort()

# Ascending order output
for h, c in hourslst:
    print(h, c)
