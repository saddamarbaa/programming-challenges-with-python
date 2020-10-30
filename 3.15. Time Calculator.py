""" 
15. Time Calculator
Write a program that asks the user to enter a number of seconds 
and works as follows:
- There are 60 seconds in a minute. If the number of seconds entered by 
the user is greater than or equal to 60, the program should display 
the number of minutes in that many seconds.
- There are 3600 seconds in an hour. If the number of seconds entered by 
the user is greater than or equal to 3600, the program should display 
the number of hours in that many seconds.
- There are 86400 seconds in a day. If the number of seconds entered by 
the user is greater than or equal to 86400, the program should display 
the number of days in that many seconds.
Starting out with Python. Third Edition. Tony Gaddis.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
(2) https://youtu.be/o_0PvX0s0zQ
"""
# Get the User Input(the number of seconds) and Convert to int
number_of_seconds = int(input("Please Enter The number of seconds : "))
# Let save the flowing values in variable first 
one_minute = 60
an_hour = 3600 
seconds_in_day = 86400 
# Calculate All the Results
number_of_minutes = number_of_seconds // one_minute
number_of_hours = number_of_seconds // an_hour
number_of_days = number_of_seconds // seconds_in_day
# check All the conditions and display the Result
if number_of_seconds >= 0  and number_of_seconds  < one_minute:
    print(f"is only {number_of_seconds} seconds")
elif number_of_seconds >= one_minute  and number_of_seconds  < an_hour:
    print("there is : " + str(number_of_minutes) + " minutes in " + \
          str(number_of_seconds) + " seconds ")
elif number_of_seconds >= an_hour and number_of_seconds  < seconds_in_day:
    print("there is : " + str(number_of_hours) + " hours in " + \
          str(number_of_seconds) + " seconds ")
elif number_of_seconds >= seconds_in_day :
    print("there is : " + str(number_of_days) + " days in " + \
          str(number_of_seconds) + " seconds ")
