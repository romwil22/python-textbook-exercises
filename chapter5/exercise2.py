"""Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average."""

max_number = None
min_number = None

while True:
    user_number = input('Enter a number: ')

    if user_number == 'done':
        break

    try:
        user_number = int(user_number)
    except:
        print("Invalid input")
        continue

    if max_number is None or user_number > max_number:
        max_number = user_number

    if min_number is None or user_number < min_number:
        min_number = user_number

print(type(user_number))
print('Minimum number entered:', min_number)
print('Maximum number entered:', max_number)
