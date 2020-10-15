""" 
2. Areas of Rectangles
The area of a rectangle is the rectangles length times its width. 
Write a program that asks for the length and width of two rectangles. 
The program should tell the user which rectangle has the greater area, 
or if the areas are the same.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
(2) https://youtu.be/7be9HlHRB-E
"""
#  Get User Input(the length and width of two rectangles.)
#  Convert User input to float
rectangle1_length = float(input("Please Enter the length of Rectangle 1 : "))
rectangle1_width = float(input("Please Enter the Width of Rectangle 1 : "))
rectangle2_length = float(input("Please Enter the length of Rectangle 2 : "))
rectangle2_width = float(input("Please Enter the Width of Rectangle 2 : "))
# Compute Area of Rectangle for both
rectangle1_area = rectangle1_length * rectangle1_width
rectangle2_area = rectangle2_length * rectangle2_width
# check all the conditions
if rectangle1_area > rectangle2_area:
    print("Rectangle 1 is Bigger than Rectangle 2")
elif rectangle2_area > rectangle1_area:
    print("Rectangle 2 is Bigger than Rectangle 1")
else:
    print("the areas are the same")
