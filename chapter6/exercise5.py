"""Take the following Python code that stores a string:
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted
string into a floating point number."""

string = 'X-DSPAM-Confidence:0.8475'
colon_index = string.find(':')
float_convert = string[colon_index+1:]
float_convert = float(float_convert)
print(float_convert)
