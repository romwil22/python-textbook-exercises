"""Encapsulate this code in a function named count, and
generalize it so that it accepts the string and the letter as arguments."""

fruit = 'banana'

# Count how many letter "a" in a strings


def count(f):
    count = 0
    for letter in f:
        if letter == 'a':
            count += 1

    return count


# Print output
a_count = count(fruit)
print(a_count)
