""" 
14. Body Mass Index
Write a program that calculates and displays a person's body mass index (BMI).
The BMI is often used to determine whether a person is overweight or underweight
for his or her height. 
A person's BMI is calculated with the following formula:
BMI = weight * 703/(height * height)
where weight is measured in pounds and height is measured in inches. 
The program should ask the user to enter his or her weight and height 
and then displays the user's BMI. 
The program should also display a message indicating whether the person 
has optimal weight, is underweight, or is overweight. 
A person's weight is considered to be optimal if his or her BMI is 
between 18.5 and 25. 
If the BMI is less than 18.5, the person is considered to be underweight. 
If the BMI value is greater than 25, the person is considered to be overweight
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
(2) https://youtu.be/p2FgB_x94Cg
"""
# Get the User Input(weight and height) and Convert to float
weight = float(input("Please Enter Your weight : "))
height = float(input("Please Enter Your height : "))
"""
Calculate the person's body mass index (BMI) using the given Formula
BMI = weight * 703/(height * height)
"""
BMI = (weight * 703) / (height * height) # height * height = height ** 2
                               
# check All the conditions and display the Result
if BMI < 18.5:
    print("Your BMI is : " + format(BMI,".2f") + \
          " So You Considered to be Underweight")
if BMI >= 18.5 and BMI <= 25:
    print("Your BMI is : " + format(BMI,".2f") + \
          " You have Optimal Weight")
else:
    print("Your BMI is : " + format(BMI,".2f") + \
          " So You Considered to be Overweight")
