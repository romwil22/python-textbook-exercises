"""Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit,
and print out theconverted temperature."""

#User input
cel_temp = input('Enter celsius temperature: ')
cel_temp = float(cel_temp)

#Convert to Fahrenheit
fah_temp = (cel_temp*9/5)+32
print('Fahrenheit temperature:', round(fah_temp, 2))
