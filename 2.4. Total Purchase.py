"""
4. Total Purchase
A customer in a store is purchasing five items.
Write a program that asks for the price of each item,
and then displays the subtotal of the sale, the amount
of sales tax, and the total. Assume the sales tax is 7 percent.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis
(2) https://youtu.be/2tHZw1-xVDs
"""
# the sales tax is 7 percent
SALESTAX = 0.07

# (1) Get the User Input (price of all the five items)
# (2) convert All the item to float
item1 = float(input("Please Enter the Price of the first item  : "))
item2 = float(input("Please Enter the Price of the second item : "))
item3 = float(input("Please Enter the Price of the third item  : "))
item4 = float(input("Please Enter the Price of the fourth item : "))
item5 = float(input("Please Enter the Price of the fifth item  : "))

# Calculate the subtotal of the sale
subtotal = (item1 + item2 + item3 + item4 + item5)
# Calculate the amount of sales tax
tax = subtotal * SALESTAX
# Calculate the total
total = subtotal + tax

# printing the final Result in Formated
print("the subtotal of the sale : $"+ format(subtotal,",.2f"))
print("the amount of sales tax :  $"+ format(tax,",.2f"))
print("the total :  $"+ format(total,",.2f"))
