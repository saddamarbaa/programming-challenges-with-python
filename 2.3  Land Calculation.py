"""
3. Land Calculation
One acre of land is equivalent to 43,560 square feet.
Write a program that asks the user to enter the total square feet
in a tract of land and calculates the number of acres in the tract.

Hint: Divide the amount entered by 43,560 to get the number of acres.

Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis
(2) https://youtu.be/KiD7LEkDEfY
"""
#  One acre of land
ONE_ACRE_OF_LAND = 43560

# (1) Get User Input as string (totals quare feet)
# (2) convert uset input to int
totalsquarefeet = int(input("Please Enter the total square feet : "))

# Calculates the number of acres in the tract
numberofAcres = (totalsquarefeet / ONE_ACRE_OF_LAND )* 1

# printing the final Result in Formated
print("the number of acres in the tract : "+ format(numberofAcres, ",.2f"))
