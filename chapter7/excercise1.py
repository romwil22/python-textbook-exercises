"""Write a program to read through a file and print the contents
of the file (line by line) all in upper case. Executing the program will
look as follows:
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500
You can download the file from www.py4"""

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
        print(textfile_input, 'invalid text file try again')
        print()
        continue

# Read whole file and convert to uppercase
for line in fileread:
    line = line.rstrip()
    print(line.upper())
