"""
8. Hot Dog Cookout Calculator
Assume that hot dogs come in packages of 10, and hot dog buns come 
in packages of 8. 
Write a program that calculates the number of packages of hot dogs 
and the number of packages of hot dog buns needed for a cookout, with the 
minimum amount of leftovers. 
The program should ask the user for the number of people attending 
the cookout and the number of hot dogs each person will be given. 
The program should display the following details:

The minimum number of packages of hot dogs required
The minimum number of packages of hot dog buns required
The number of hot dogs that will be left over 
The number of hot dog buns that will be left over
Reference:
(1) Starting out with Python, Third Edition, Tony Gaddis Chapter 3
 very well explained link blow
(2) https://youtu.be/QCL-EBYG-HA
(3) https://youtu.be/9kZhD42xMn8
"""
# let first store given numbers in variables
# hot dogs come in packages of 10
# hot dog buns come in packages of 8. 
hot_dog_packages = 10
hot_dog_buns_packages = 8  

# Get User Input(the number of people attending the cookout)
# convert usert input to int
number_of_people = int(input("Please Enter the number of people " + \
                         "attending this cookout : ")) 
# Get User Input(tthe number of hot dogs each person will be given)
# the number of hot dogs each person will be given
hot_dogs_foreach = int(input("Please Enter the number of hot dogs " + \
                         "for each person : ")) 

# calculate the number of hot dogs needed
# number of single hot dog we need for this cookcout
hot_dogs_needed = number_of_people * hot_dogs_foreach
# the number of hot dog buns needed 
# number of single hot dog buns we need for this cookcout
hot_dog_buns_needed = hot_dogs_needed

"""
let compute the flowing (the exact dog packages)
and (the exact dog buns packages) we will need 
them latter in calculation process
"""
exact_dog_packages = hot_dogs_needed / hot_dog_packages
exact_dog_buns_packages = hot_dog_buns_needed / hot_dog_buns_packages 

"""
now let compute the flowing
The minimum number of packages of hot dogs required
The minimum number of packages of hot dog buns required
we need used reminder so can test
"""
dog_packages_reminder = hot_dogs_needed % hot_dog_packages
dog_buns_packages_reminder = hot_dog_buns_needed  % hot_dog_buns_packages

"""
if the reminder is bigger than zero we have round up the number to
next integer using only tools we have learn so far and not use any method
"""
if dog_packages_reminder > 0:
    # round it up to next int
    minimum_hot_dogs_required = int(dog_packages_reminder + 1) 
# else mean mean we have exact number of dog 
else:
    minimum_hot_dogs_required = exact_dog_packages
    
"""
we will use same idea with The minimum number of packages of hot dog 
buns required
"""
if dog_buns_packages_reminder > 0:
    # round it up to next int
    minimum_hot_dogs_buns_required = int(dog_buns_packages_reminder + 1)
# else mean mean we have exact number of dog buns 
else:
    minimum_hot_dogs_buns_required = exact_dog_buns_packages
        
"""
now let compute the flowing
The number of hot dogs that will be left over 
The number of hot dog buns that will be left over
"""
hot_dogs_left_over = minimum_hot_dogs_required - exact_dog_packages

hot_dog_buns_left_over = minimum_hot_dogs_buns_required -exact_dog_buns_packages
    
"""
now let display them All :
The minimum number of packages of hot dogs required
The minimum number of packages of hot dog buns required
The number of hot dogs that will be left over 
The number of hot dog buns that will be left over
"""

print("The minimum number of packages of hot dogs required " + \
      str(minimum_hot_dogs_required) + "\n" + \
      "The minimum number of packages of hot dog buns required " + \
       str(minimum_hot_dogs_buns_required) + "\n" + \
       "The number of hot dogs that will be left over " + \
        str(hot_dogs_left_over) + "\n" + \
        "The number of hot dog buns that will be left over " + \
        str(hot_dog_buns_left_over))       

"""
almost 95% is complete but not done yet done i will come
 back continue after Finish chapter 5
 """
