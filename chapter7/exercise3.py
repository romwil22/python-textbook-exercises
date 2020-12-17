"""Sometimes when programmers get bored or want to have a
bit of fun, they add a harmless Easter Egg to their program. Modify
the program that prompts the user for the file name so that it prints a
funny message when the user types in the exact file name “na na boo
boo”. The program should behave normally for all other files which
exist and don’t exist. Here is a sample execution of the program:
python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt
python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
We are not encouraging you to put Easter Eggs in your programs; this
is just an exercise."""

textfile_input = None
fileread = None

# User text file input condition
while True:
    textfile_input = input('enter text file: ')

    try:
        fileread = open(textfile_input)
        print()
        break
    except:
        if textfile_input == "na na boo boo":
            print(textfile_input.upper(), ' - You have been punk\'d!')
            print()
            continue
        print('File cannot be opened:', textfile_input)
        print()
        continue

count = 0

# Count text line
for line in fileread:
    count += 1

# Print output
format_Txt = 'There were {} subject lines in {}'.format(count, textfile_input)
print(format_Txt)
