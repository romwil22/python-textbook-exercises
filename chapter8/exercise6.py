"""Rewrite the program that prompts the user for a list of
numbers and prints out the maximum and minimum of the numbers at
the end when the user enters “done”. Write the program to store the
numbers the user enters in a list and use the max() and min() functions to
compute the maximum and minimum numbers after the loop completes."""

numbers_list = list()

# user input for number
while True:
    input_number = input('Enter a number: ')

    if input_number.lower() == 'done':
        print()
        break
    try:
        number = float(input_number)
        numbers_list.append(number)
    except:
        # Error message if user enter an invalid input
        print('Invalid input, try again')

# Output for max and min value
print('Maximum:', max(numbers_list))
print('Minimum:', min(numbers_list))
