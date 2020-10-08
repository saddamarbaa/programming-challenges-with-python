""" 
8. Tip, Tax, and Total
Write a program that calculates the total amount of a meal purchased at a restaurant.
The program should ask the user to enter the charge for the food, and then calculate
the amount of a 18 percent tip and 7 percent sales tax.
Display each of these amounts and the total.

Reference:
(1)Starting out with Python, Third Edition, Tony Gaddis Chapter 2
(2) https://youtu.be/xcaniCRhh4I
"""
tipPercent = 0.18
taxPercent = 0.07
# (1) Get the User Input (the charge for the food)
# (2) convert user input to float
foodCharge = float(input("Please Enter the charge for the food : "))

# Calculate the amount of a 18 percent tip
Tip = foodCharge * tipPercent
# Calculate the amount of 7 percent sales tax
salesTax = foodCharge * taxPercent
# Calculate the total amount of a meal purchased at a restaurant
Total = (foodCharge + Tip + salesTax)

# Display each of these amounts and the total
print("food charge : "+ format(foodCharge, ",.2f") +" $ ")
print("Tip : "+ format(Tip, ",.2f") +" $ ")
print("sales Tax : "+ format(salesTax, ",.2f") +" $ ")
print("Total : "+ format(Total, ',.2f') +' $ ')
