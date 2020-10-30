""" 
12. Software Sales
A software company sells a package that retails for $99. 
Quantity discounts are given according to the following table:
Quantity      Discount
10_19          10% 
20_49          20% 
50_99          30%
100 or more    40%
Write a program that asks the user to enter the number of packages purchased.
The program should then display the amount of the discount (if any) and the 
total amount of the purchase after the discount.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
(2) https://youtu.be/0qHWyPWhZO4
"""
# give value
package_price = 99
# Get the User Input(the number of packages purchased) and Convert to int
number_of_packages = int(input("Please Enter the number of packages"+\
                               "purchased : "))

# check All the conditions
if number_of_packages < 10:
    discount = 0
elif number_of_packages < 20:
    discount = 0.1  # 0.1 is 10% 
elif number_of_packages < 50:
    discount = 0.2  # 0.2 is 20% 
elif number_of_packages < 100:
    discount = 0.3  # 0.3 is 30% 
else:
    discount = 0.4  # 0.4 is 20%
# Calculate the discount amount and total amount
total_amount = number_of_packages * package_price
discount_amount = number_of_packages * discount
# Display the Result
print("the amount of the discount is : $" + format(discount, ",.2f"))
print("total amount of the purchase after the discount is : $" + \
       format(total_amount, ",.2f"))