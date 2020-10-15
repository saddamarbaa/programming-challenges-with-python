"""
4. Roman Numerals
Write a program that prompts the user to enter a number within the range of 
1 through 10. 
The program should display the Roman numeral version of that number. 
If the number is outside the range of 1 through 10, the program should display 
an error message. 
The following table shows the Roman numerals for the numbers 1 through 10:
Number - Roman Numeral
1 -------------------- I 
2 -------------------- II 
3 -------------------- III
4 -------------------- IV 
5 -------------------- V 
6 -------------------- VI 
7 -------------------- VII 
8 -------------------- VIII
9 -------------------- IX
10 ------------------ X
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
(2) https://youtu.be/lV-EUUOvKB0
"""
#  Get User Input(a number within the range of 1 through 10. )
#  Convert User input to int
number = int(input("Please Enter a number within the range of 1 through 10 : "))
# check all the conditions
if number == 1:
    print(f"the Roman numeral version of {number} is I")
elif number == 2:
    print(f"the Roman numeral version of {number} is II")
elif number == 3:
    print(f"the Roman numeral version of {number} is III")
elif number == 4:
    print(f"the Roman numeral version of {number} is IV")    
elif number == 5:
    print(f"the Roman numeral version of {number} is V")    
elif number == 6:
    print(f"the Roman numeral version of {number} is VI")
elif number == 7:
    print(f"the Roman numeral version of {number} is VII")
elif number == 8:
    print(f"the Roman numeral version of {number} is VIII")
elif number == 9:
    print(f"the Roman numeral version of {number} is IX")
elif number == 10:
    print(f"the Roman numeral version of {number} is X")
else:
    print("Error ! : Please Enter a number in the range of 1 through 10")
"""
this Question can be solve with loop very easy but am flowing the book 
and in chapter 3  is all about if condition
"""
