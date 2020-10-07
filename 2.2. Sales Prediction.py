"""
2. Sales Prediction
A company has determined that its annual profit is typically 23 percent
of total sales. Write a program that asks the user to enter the projected
amount of total sales, and then displays the profit that will be made from that amount.
Hint: Use the value 0.23 to represent 23 percent.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis
(2) https://youtu.be/qTKJuVTgv2Q """

# (1) Get User Input as string (projected amount of total sales)
# (2) convert uset input to float
projectedSales = float(input("Please Enter the projected amount of total sales : "))

# Calculate the annual profit
annualProfit = projectedSales * 0.23

# printing the  final Result in Formated
print("the annual profit is : $" + format(annualProfit, ",.2f"))

 
 
 
