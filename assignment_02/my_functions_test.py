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
# Testing Script for Assignment 2: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# Import the function definitions from my_functions.py

print("#" + 50*"-")
print("# Importing function definitions")
print("# Examples within script my_functions.py:")
print("#" + 50*"-")


# Run the script to load those definitions.
exec(open("my_functions.py").read())
# This puts the function definitions in memory.


# Import doctest to test functions from docstring.
import doctest



##################################################
# Testing with doctest module
##################################################

# Use the doctest module to test the examples in the docstring

print("#" + 50*"-")
print("# Testing with doctest module")
print("#" + 50*"-")

# Run the examples to test examples in the docstrings 
# of the functions in this module. 
doctest.testmod()


##################################################
# Run the solution examples to test these functions
##################################################


# Test the examples and print the results. 



print("#" + 50*"-")
print("# Testing with examples in solutions")
print("#" + 50*"-")

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



print("#" + 50*"-")


##################################################
# End
##################################################