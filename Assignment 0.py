# Khush Agarwala
# ICS 4U
# September 6th, 2018
# program that calculates the area of a triangle

# This tells the user what this program is meant for
print ("\nThis program will find the area of a triangle")

# This collects an input from the user and converts it into a float, and assigns it to the variable "b"
b = float(input("\nPlease input the base length of the triangle greater than 0 in cm \n"))

# This runs if the user inputs the value of "b" as less than or equal to zero, and constantly runs while the user
# changes the value to greater than 0
while b <= 0:
    b = float(input("Invalid input! Please input the base length of the triangle in cm \n"))

# This collects an input from the user and converts it into a float, and assigns it to the variable "h"
h = float(input("Please input the height of the triangle greater than 0 in cm \n"))

# This runs if the user inputs the value of "h" as less than or equal to zero, and constantly runs while the user
# changes the value to greater than 0
while h <= 0:
    h = float(input("Invalid input! Please input the height of the triangle in cm \n"))

# this calculates the area of the triangle by multiplying the values of "b" and "h" and then dividing the product by 2,
# then it assigns it to the variable "a"
a = (b * h)/2

# This prints out a final sentence that prints out the value of a (the area of the triangle)
print ("The area of this triangle is " + str(a) + " cm^2")