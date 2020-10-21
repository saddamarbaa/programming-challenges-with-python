""" 
11. Book Club Points
Serendipity Booksellers has a book club that awards points to its customers
based on the number of books purchased each month. 
The points are awarded as follows:
- If a customer purchases 0 books, he or she earns 0 points
- If a customer purchases 2 books, he or she earns 5 points
- If a customer purchases 4 books, he or she earns 15 points
- If a customer purchases 6 books, he or she earns 30 points
- If a customer purchases 8 or more books, he or she earns 60 points
Write a program that asks the user to enter the number of books that he 
or she has purchased this month and displays the number of points awarded.
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
(2) https://youtu.be/1n8T4JOd9s4
"""
# Get the User Input and Convert to int
number_of_books = int(input("Please Enter number of books Purchased " + \
                       "this month : ")) 
# now let check all the condition and print the result
if number_of_books < 2:
    print("You have earn 0 Point")
elif number_of_books < 4:
    print("You have earn 5 Points")
elif number_of_books < 6:
    print("You have earn 15 Points")
elif number_of_books < 8:
    print("You have earn 30 Points")
else:
    print("You have earn 60 Points")
