"""Read the documentation of the string methods at
https://docs.python.org/library/stdtypes.html#string-methods You
might want to experiment with some of them to make sure you
understand how they work. strip and replace are particularly useful.
The documentation uses a syntax that might be confusing. For example,
in find(sub[, start[, end]]), the brackets indicate optional arguments.
So sub is required, but start is optional, and if you include start, then
end is optional."""

# Remove left whitespace
string = '          X-DSPAM-Confidence:0.8475           '
lstrip_string = string.lstrip()
print(lstrip_string)

# Remove Right whitespace
rstrip_string = string.rstrip()
print(rstrip_string)

# Remove both whitespace
strip_string = string.strip()
print(strip_string)

# Replace character or word in the string
replace_string = string.replace('X', 'Z')
print(replace_string)
replace_string = string.replace('DSPAM', 'MDRAFT')
print(replace_string)
