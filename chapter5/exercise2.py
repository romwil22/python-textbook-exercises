"""Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average."""

# Variable holder for minimum and maximum
max_number = None
min_number = None

while True:
    user_number = input('Enter a number: ')  # user input

    if user_number == 'done':  # end of condition
        break

    # holding an error input
    try:
        user_number = int(user_number)
    except:
        print("Invalid input")
        continue

    # place the max no.
    if max_number is None or user_number > max_number:
        max_number = user_number

    # place the min no.
    if min_number is None or user_number < min_number:
        min_number = user_number

# result
print('Minimum number entered:', min_number)
print('Maximum number entered:', max_number)
