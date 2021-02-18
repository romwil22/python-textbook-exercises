"""Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
"""
# User input
grade = input('enter your score between 0.0 and 1.0: ')

# Grade condition function


def computegrade(g):
    try:
        g = float(g)
        if g >= 1:
            return g, "is out of range"
        elif g >= 0.9:
            return 'A'
        elif g >= 0.8:
            return 'B'
        elif g >= 0.7:
            return 'C'
        elif g >= 0.6:
            return 'D'
        else:
            return 'F'
    except:
        return 'String input invalid'


# Result
grade_computed = computegrade(grade)
print(grade_computed)
