"""
5. Mass and Weight
Scientists measure an object's mass in kilograms and its weight in newtons. 
If you know the amount of mass of an object in kilograms, you can calculate 
its weight in newtons with the following formula: weight = mass x 9.8
Write a program that asks the user to enter an object's mass' and then 
calculates its weight. 
If the object weighs more than 500 newtons display a message indicating that 
it is too heavy. 
If the object weighs less than 100 newtons  display a message indicating that 
it is too light.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
(2) https://youtu.be/O6lqF8WxUwk
"""
#  Get User Input(the object mass)
#  Convert User input to float
mass = float(input("Please Enter an object  mass : "))
# calculates its weight with the formula: weight = mass x 9.8
weight = mass * 9.8
# Display the Result
if weight > 500:
    print("the object weighs : " + str(format(weight,",.2f")) + \
          " newtons is too heavy ")
elif weight < 100:
    print("the object weighs : " + str(format(weight,",.2f")) + \
          " newtons is too light ")
else:
    print("the object weighs : " + str(format(weight,",.2f")) + \
          " newtons is neither heavy or light ")    
    

