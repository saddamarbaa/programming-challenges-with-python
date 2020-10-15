"""
6. Magic Dates
The date June 10, 1960, is special because when it is written in the 
following format, the month times the day equals the year: 6/10/60
Design a program that asks the user to enter a month (in numeric form), 
a day, and a two- digit year. 
The program should then determine whether the month times the day equals 
the year. 
If so, it should display a message saying the date is magic. 
Otherwise, it should display a message saying the date is not magic.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
(2) https://youtu.be/sp0sP640MgA
"""
#  Get User Input(a month (in numeric form), a day, and a two- digit year.)
#  Convert User input to int
month = int(input("Please Enter a month (in numeric form) : "))
day = int(input("Please Enter the day : "))
year = int(input("Please Enter a two- digit year : "))
# Display the Result
if month * day == year:
    print(f"the {day}/{month}/{year} is magic date")
else:
    print(f"the {day}/{month}/{year} is not magic date")
    
