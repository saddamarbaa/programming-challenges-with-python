"""
7. Miles-per-Gallon
A car’s miles-per-gallon (MPG) can be calculated with the following formula:
MPG = Miles driven / Gallons of gas used
Write a program that asks the user for the number of miles driven and the gallons of gas used.
It should calculate the car’s MPG and display the result.
Reference:
(1)Starting out with Python, Third Edition, Tony Gaddis Chapter 2
(2) https://youtu.be/EjUhUQ_px7o
"""

# (1) Get the User Input (Miles driven and Gallons of gas used  )
# (2) convert  both user input to float
MilesDriven = float(input("Please Enter the number of miles driven : "))
GallonsOfGasUsed = float(input("Please Enter the number of gallons of gas used : "))

# Calculate the car’s miles-per-gallon
# MPG = Miles driven / Gallons of gas used
MilesPerGallon = MilesDriven / GallonsOfGasUsed

# display the result
print("A car’s miles per gallon is : "+ str(MilesPerGallon) +' miles-per-gallon ')
