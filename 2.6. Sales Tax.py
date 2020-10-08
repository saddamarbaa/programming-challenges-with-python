"""
6. Sales Tax
Write a program that will ask the user to enter the amount of a purchase.
The program should then compute the state and county sales tax.
Assume the state sales tax is 5 percent and the county sales tax is 2.5 percent.
The program should display the amount of the purchase, the state sales tax,
the county sales tax, the total sales tax, and the total of the sale
(which is the sum of the amount of purchase plus the total sales tax).

Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.

Reference:
(1)Starting out with Python, Third Edition, Tony Gaddis Chapter 2
(2) https://youtu.be/q2iDYpJP1zk
"""

STATETAX  = 0.05     # state tax percent this from Hind
COUNTYTAX = 0.025    # county tax percent this from Hind

# (1) Get the User Input (the amount of a purchase )
# (2) convert user input to float
userInputPurchase = float(input("Please Enter the amount of purchase  : "))

# Compute the state sales tax
stateSalesTax = userInputPurchase * STATETAX
# Compute the county sales tax
countySalesTax = userInputPurchase * COUNTYTAX
# Compute the total sales tax
totalSalesTax = stateSalesTax + countySalesTax
# Compute the total of the sale
totalOfSale = userInputPurchase + totalSalesTax

# display the final Result in Formated
print()  # print new line first
print("the amount of the purchase : $"+ format(userInputPurchase, ",.2f"))
print("the state sales tax  :  $"+ format(stateSalesTax, ",.2f"))
print("the county sales tax  :  $"+ format(countySalesTax, ",.2f"))
print("the total sales tax :  $"+ format(totalSalesTax, ",.2f"))
print("the total of the sale :  $"+ format(totalOfSale, ",.2f"))
