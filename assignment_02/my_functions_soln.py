# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: 
#
# Date:
# 
##################################################
#
# Sample Script for Assignment 2: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module
import math


##################################################
# Function Definitions
##################################################

# Exercise 1

def average(num1: float, num2: float) -> float:
    """Return the average of num1 and num2.

    >>> average(10,20)
    15.0
    >>> average(2.5, 3.0)
    2.75
    >>> average(0.0, 0.0)
    0.0
    """
    avg = (num1 + num2) / 2

    return avg



# Define the rest of your functions for Exercises 2-6.
 

# Exercise 2

def area_of_circle(radius: float) -> float:
    """Return the area of a circle with given radius.

    >>> area_of_circle(0.0)
    0.0
    >>> area_of_circle(1.0)
    math.pi
    >>> area_of_circle(1.0/math.sqrt(math.pi))
    1.0
    """
    area = math.pi*radius**2

    return area
    


# Exercise 3

def volume_of_cylinder(radius: float, height: float) -> float:
    """Return the volume of a cylinder with a given height and
    base a given radius.

    >>> volume_of_cylinder(0.0, 9.9)
    0.0
    >>> volume_of_cylinder(1.0, 1.0)
    math.pi
    >>> volume_of_cylinder(1.0/math.pi, math.pi)
    1.0
    """
    volume = math.pi*radius**2*height

    return volume


# Exercise 4

def utility(x: float, y: float, alpha: float) -> float:
    """Calculates the value of the Cobb-Douglass utility
    function for consumption goods x and y with exponent alpha.

    >>> utility(0.0, 4.7, 0.5)
    0.0
    >>> utility(1.0, 1.0, 0.75)
    1.0
    >>> utility(4, 16, 0.5)
    8.0
    """
    utils = x**(alpha)*y**(1 - alpha)

    return utils


# Exercise 5

def logit(x: float, beta_0: float, beta_1: float) -> float:
    """Calculates the value of the Cobb-Douglass utility
    function for consumption goods x and y with exponent alpha.

    >>> logit(13.7, 0.0, 0.0)
    0.5
    >>> logit(0.0, math.log(2), 2.0)
    2.0/3.0
    >>> logit(1.0, 0.0, math.log(5))
    5.0/6.0
    """
    link = math.exp(beta_0 + x*beta_1)/(1 + math.exp(beta_0 + x*beta_1))

    return link





##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results. 

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating average(10,20)")
print("Expected: " + str(15.0))
print("Got: " + str(average(10,20)))


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating average(2.5, 3.0)")
print("Expected: " + str(2.75))
print("Got: " + str(average(2.5, 3.0)))


print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating average(2.5, 3.0)")
print("Expected: " + str(0.0))
print("Got: " + str(average(0.0, 0.0)))

#--------------------------------------------------


# ...

# Continue with the rest of your examples.
# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating area_of_circle(0.0)")
print("Expected: " + str(0.0))
print("Got: " + str(area_of_circle(0.0)))


print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating area_of_circle(1.0)")
print("Expected: " + str(math.pi))
print("Got: " + str(area_of_circle(1.0)))


print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating area_of_circle(1.0/math.sqrt(math.pi))")
print("Expected: " + str(1.0))
print("Got: " + str(area_of_circle(1.0/math.sqrt(math.pi))))

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating volume_of_cylinder(0.0, 9.9)")
print("Expected: " + str(0.0))
print("Got: " + str(volume_of_cylinder(0.0, 9.9)))


print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating volume_of_cylinder(1.0, 1.0)")
print("Expected: " + str(math.pi))
print("Got: " + str(volume_of_cylinder(1.0, 1.0)))


print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating volume_of_cylinder(1.0/math.pi, math.pi)")
print("Expected: " + str(1.0))
print("Got: " + str(volume_of_cylinder(1.0/math.pi, math.pi)))

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating utility(0.0, 4.7, 0.5)")
print("Expected: " + str(0.0))
print("Got: " + str(utility(0.0, 4.7, 0.5)))


print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating utility(1.0, 1.0, 0.75)")
print("Expected: " + str(1.0))
print("Got: " + str(utility(1.0, 1.0, 0.75)))


print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating utility(4, 16, 0.5)")
print("Expected: " + str(8.0))
print("Got: " + str(utility(4, 16, 0.5)))

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 5.")

print("#" + 50*"-")
print("Exercise 5, Example 1:")
print("Evaluating logit(13.7, 0.0, 0.0)")
print("Expected: " + str(0.5))
print("Got: " + str(logit(13.7, 0.0, 0.0)))


print("#" + 50*"-")
print("Exercise 5, Example 2:")
print("Evaluating logit(0.0, math.log(2), 2.0)")
print("Expected: " + str(2.0/3.0))
print("Got: " + str(logit(0.0, math.log(2), 2.0)))


print("#" + 50*"-")
print("Exercise 5, Example 3:")
print("Evaluating logit(1.0, 0.0, math.log(5))")
print("Expected: " + str(5.0/6.0))
print("Got: " + str(logit(1.0, 0.0, math.log(5))))

#--------------------------------------------------




##################################################
# End
##################################################