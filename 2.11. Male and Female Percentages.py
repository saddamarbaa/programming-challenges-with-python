""" 
11. Male and Female Percentages
Write a program that asks the user for the number of males and the number of 
females registered in a class. 
The program should display the percentage of males and females in the class.
Hint: Suppose there are 8 males and 12 females in a class. 
There are 20 students in the class.
The percentage of males can be calculated as 8 / 20 = 0.4, or 40%. 
The percentage of females can be calculated as 12 / 20 = 0.6, or 60%.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 2
(2) https://youtu.be/2M1HVL6nbAY
"""
#  Get User Input(the number of males and females registered int Class)
#  Convert User input to int
females = int(input("Please Enter the number of females int Class : "))
males = int(input("Please Enter the number of males int  Class : "))
# Calculate the percentage of males and females 
total_student = males + females 
# first method
#males_percentage = (males / total_student) * 100
#females_percentage = (females / total_student) * 100
# second method
males_percentage = males / total_student
females_percentage = females / total_student
# display the percentage 
# first method method
#print("The females percentage is "+ str(females_percentage) + " %")
#print("The males percentage  is "+ str(males_percentage) + " %")
# second method
print("There are " + str(total_student) + " students in the Class " + \
      format(males_percentage, ".0%") + " of them are males and " + \
     format(females_percentage, ".0%") + " of them are females")
