""" 
13. Shipping Charges
The Fast Freight Shipping Company charges the following rates:

Weight of Package                             Rate per Pound
2 pounds or less                                  $1.50
Over 2 pounds but not more than 6 pounds          $3.00
Over 6 pounds but not more than 10 pounds         $4.00
Over 10 pounds                                    $4.75
Write a program that asks the user to enter the weight of a package 
and then displays the shipping charges.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
(2) https://youtu.be/eZwTPscc4Yc
"""
# Get the User Input(the weight of a package) and Convert to int
weight_of_package = int(input("Please Enter the weight of a package : "))
                               
# check All the conditions
if weight_of_package <= 2:
    shipping_charges = 1.50
elif weight_of_package <= 6:
    shipping_charges = 3.00 
elif weight_of_package <= 10:
    shipping_charges = 4.00  
else:
    shipping_charges = 4.75
# Display the shipping charges
print("the shipping charges is : $" + format(shipping_charges,",.2f"))
