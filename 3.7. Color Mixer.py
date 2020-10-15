"""
7. Color Mixer
The colors red, blue, and yellow are known as the primary colors because 
they cannot be made by mixing other colors. When you mix two primary colors 
you get a secondary color, as shown here:
When you mix red and blue, you get purple. 
When you mix red and yellow, you get orange.
When you mix blue and yellow, you get green.
Design a program that prompts the user to enter the names of two primary colors
to mix. If the user enters anything other than "red" ' "blue" or "yellow" 
the program should display an error message. Otherwise, the program should 
display the name of the secondary color that results.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
(2) https://youtu.be/YncksNMx3qU
"""
#  Get User Input(names of two primary colors to mix)
print("Please Enter names of two primary colors to mix") 
first_color = input("Enter the first primary color : ") 
second_color = input("Enter the second primary color : ")
# Convert both color to lower case
first_color = first_color.lower()
second_color = second_color.lower()
# TEST condition and Display the Result
# Case When we mix red and blue
if (first_color == "red" and second_color == "blue") or \
   (first_color == "blue" and second_color == "red"):
    print(f"{first_color} Mix with {second_color} you get purple color")
# Case When we mix red and yellow
elif (first_color == "red" and second_color == "yellow") or \
     (first_color == "yellow" and second_color == "red"):
    print(f"{first_color} Mix with {second_color} you get orange color")
# Case When we mix blue and yellow 
elif (first_color == "blue" and second_color == "yellow") or \
     (first_color == "yellow" and second_color == "blue"):
    print(f"{first_color} Mix with {second_color} you get green color")
# case when the user enters anything other than "red" "blue: or "yellow"  
else:
    print("Error message Please Enter only from {red, blue and yellow }")

 
