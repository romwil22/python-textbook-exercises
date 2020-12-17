"""Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
90 CHAPTER 7. FILES
values from these lines. When you reach the end of the file, print out
the average spam confidence.
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.
"""

# User text file input condition
while True:
    textfile_input = input('enter text file: ')

    try:
        fileread = open(textfile_input)
        print()
        break
    except:
        print(textfile_input, 'invalid text file try again')
        print()
        continue

total_float = 0
count = 0

# Search line for “X-DSPAM-Confidence:”
for line in fileread:
    line = line.strip()

    if not line.startswith('X-DSPAM-Confidence:'):
        continue

    search_number = line.find(':')
    float_number = float(line[search_number+1:])
    total_float += float_number
    count += 1

# result for average
print('Average spam confidence:', round(total_float/count, 12))
