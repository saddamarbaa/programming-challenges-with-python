""" 
9. Celsius to Fahrenheit Temperature Converter
Write a program that converts Celsius temperatures to Fahrenheit temperatures.
The formula is as follows: F = (9/5)C + 32
The program should ask the user to enter a temperature in Celsius,
and then display the temperature converted to Fahrenheit.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 2
(2) https://youtu.be/xcaniCRhh4I
"""
# (1) Get the User Input (the temperature in Celsius )
# (2) Convert User input to float
CelsiusTemperature = float(input("Please Enter the temperature in Celsius : "))

# Converts Celsius temperatures to Fahrenheit temperatures
# Using formula is as follows: F = (9/5)C + 32.
FahrenheitTemperature = ((9 / 5) * CelsiusTemperature) + 32

# Display display the temperature converted to Fahrenheit
print(str(CelsiusTemperature) + " Degree in Fahrenheit is : "+\
      format(FahrenheitTemperature,".1f"))
