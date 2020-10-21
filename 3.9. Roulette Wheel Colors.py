"""
9. Roulette Wheel Colors
On a roulette wheel, the pockets are numbered from 0 to 36. 
The colors of the pockets are as follows:
- Pocket 0 is green.
- For pockets 1 through 10, the odd-numbered pockets are red and the 
  even-numbered pockets are black.
- For pockets 11 through 18, the odd-numbered pockets are black and the
  even-numbered pockets are red.
- For pockets 19 through 28, the odd-numbered pockets are red and the
  even-numbered pockets are black.
- For pockets 29 through 36, the odd-numbered pockets are black and the 
  even-numbered pockets are red.
Write a program that asks the user to enter a pocket number and displays 
whether the pocket is green, red, or black. 
The program should display an error message if the user enters a number 
that is outside the range of 0 through 36.

Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
(2) https://youtu.be/5_33mLlTxMs
"""
# Get User Input(a pocket Number)and Convert to int
pocket_number = int(input("Please Enter a pocket number : ")) 
# Validate the user input first
if pocket_number < 0 or pocket_number > 36:
    print("Please Enter number in the Range (0 to 36)")
# by now we are sure the number is validate so let check all the condition
else:
     # for(0) pocket Numbers are green
    if pocket_number == 0:
        print("the pocket is GREEN")
    # for(1 to 10 )odd Numbers are RED and even numbers are back
    elif pocket_number < 11 :
        if pocket_number % 2 != 0:
            print("the pocket is RED")  
        else:
            print("the pocket is BLACK") 
    # for(11 to 18 )odd Numbers are Black and even numbers are RED
    elif pocket_number < 19 :
        if pocket_number % 2 != 0:
            print("the pocket is BLACK")
        else:
            print("the pocket is RED")
    # for(19 to 28 ) odd Numbers are RED and even numbers are Black
    elif pocket_number < 29 :
        if pocket_number % 2 != 0:
            print("the pocket is RED")
        else:
            print("the pocket is BLACK")
     # else case for(29 to 36) odd Numbers are Black and even numbers are RED 
    else:
        if pocket_number % 2 != 0:
            print("the pocket is BLACK")
        else:
            print("the pocket is RED")
    
    
 
