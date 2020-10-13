""" 
10. Ingredient Adjuster
A cookie recipe calls for the following ingredients:
1.5 cups of sugar
1 cup of butter
2.75 cups of flour
The recipe produces 48 cookies with this amount of the ingredients.
Write a program that asks the user how many cookies he or she wants
to make, and then displays the number of cups of each ingredient 
needed for the specified number of cookies.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 2
(2) https://youtu.be/hXfsYLsI-Ic
"""
# store all the given values in variable
constAmountOfCookies = 48
cupsOfSugarPer48Cookies = 1.5 
cupsOfButterPer48Cookies = 1 
cupsOfFlourPer48Cookies = 2.75 

# (1) Get the User Input (number of cookies he or she wants to make)
# (2) Convert User input to float
numberofcookies = float(input("Please Enter the number of cookies You wants\
to make : "))

# Calculate  each of ingredients
cupsOfSugar = (numberofcookies / constAmountOfCookies) * cupsOfSugarPer48Cookies 
cupOfButter = (numberofcookies / constAmountOfCookies) * cupsOfButterPer48Cookies 
cupsOfFlour = (numberofcookies / constAmountOfCookies) * cupsOfFlourPer48Cookies 

# displays the number of cups of each ingredient 
# needed for the specified number of cookies
print("For "+ str(numberofcookies) + " You will need : "+\
      format(cupsOfSugar,".3f") + "cups of sugar") 

print("For "+ str(numberofcookies) + " You will need : "+\
      format(cupOfButter,".3f") + "cups of butter") 

print("For "+ str(numberofcookies) + " You will need : "+\
      format(cupsOfFlour,".3f") + " cups of Flour") 
