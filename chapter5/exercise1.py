""" Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number."""


def user_input():
    total = 0
    count = 0
    while True:
        input_number = input('Enter a number: ')

        if input_number == 'done':
            break

        try:
            input_number = int(input_number)
        except:
            print('Invalid input')
            continue

        total += input_number
        count += 1
    print(total)
    print(count)
    print(round(total/count, 2))


user_input()
