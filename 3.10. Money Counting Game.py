""" 
3.10. Money Counting Game
Create a change-counting game that gets the user to enter the number 
of coins required to make exactly one dollar. 
The program should prompt the user to enter the number of pennies, nickels,
dimes, and quarters. 
If the total value of the coins entered is equal to one dollar, the program
should congratulate the user for winning the game. Otherwise, the program
should display a message indicating whether the amount entered was more 
than or less than one dollar.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
(2) https://youtu.be/nWFkYVinwPo
"""

# let first store the flowing  values in variable 
one_pennies = 0.01
one_nickels = 0.05 
one_dimes =  0.10
one_quarters = 0.25
one_dollar = 1.00
# Get all User Input and Convert to int
number_of_pennies = int(input("Please number of Pennies : ")) 
number_of_nickels = int(input("Please number of nickels  : "))
number_of_dimes = int(input("Please number of dimes  : "))
number_of_quarters = int(input("Please number of quarters : "))

# now we have the number of coins let get the value of each ones
# value of each pennies =  userInput * 0.01
pennies_value = number_of_pennies * one_pennies
# value of each nickels =  userInput * 0.05
nickels_value = number_of_nickels * one_nickels
# value of each dimes = userInput * 0.10
dimes_value = number_of_dimes * one_quarters
# value of each quarters = userInput * 0.25
dimes_quarters = number_of_quarters * one_dimes

# now let calculate the total of one dollar
total = pennies_value + nickels_value +  dimes_value + dimes_quarters

# check all the condition and print the result
if total == one_dollar:
    print("Congratlation You Won the Game Because Your Money Value of $" + \
          format(total, ",.2") +" is Equal to one dollar")
elif total < one_dollar:
    print("You Didint Won the Game Because Your Money Value of $"+ \
          format(total, ",.2") + " is less than to one dollar")
else:
    print("You Didint Won the Game Because Your Money Value of $" + \
           format(total, ",.2") + " is More than to one dollar")    
