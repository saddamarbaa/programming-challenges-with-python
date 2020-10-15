""" 
1. Day of the Week
Write a program that asks the user for a number in the range of 1 through 7. 
The program should display the corresponding day of the week, where 1 = Monday,
2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, 
and 7 = Sunday. 
The program should display an error message if the user enters a number 
that is outside the range of 1 through 7.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
(2) https://youtu.be/jx8y647CMsI
"""
#  Get User Input(a number in the range of 1 through 7)
#  Convert User input to int
user_number = int(input("Enter a number in the range of 1 through 7 : "))
# check all the conditions
if user_number == 1:
    print("Monday")
elif user_number == 2:
    print("Tuesday")
elif user_number == 3:
    print("Wednesday")
elif user_number == 2:
    print("Tuesday")
elif user_number == 4:
    print("Thursday")
elif user_number == 5:
    print("Friday")
elif user_number == 6:
    print("Saturday")
elif user_number == 7:
    print("Sunday")
# for all the else cases
else: 
    print("Error a number is outside the range of 1 through 7")
    
