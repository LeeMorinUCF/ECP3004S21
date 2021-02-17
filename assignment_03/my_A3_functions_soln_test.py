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
# Testing Script for Assignment 3:
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
print("# Examples within script my_A3_functions_soln.py:")
print("#" + 50*"-")


# Run the script to load those definitions.
exec(open("assignment_03/my_A3_functions_soln.py").read())
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
print("Evaluating quad_roots_1(1, -2, 1)")
print("Expected: " + str([1.0, 1.0]))
print("Got: " + str(quad_roots_1(1, -2, 1)))


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating quad_roots_1(1, 0, -1)")
print("Expected: " + str([1.0, -1.0]))
print("Got: " + str(quad_roots_1(1, 0, -1)))


print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating quad_roots_1(2, 2, -12)")
print("Expected: " + str([2.0, -3.0]))
print("Got: " + str(quad_roots_1(2, 2, -12)))


# Continue with the rest of your examples.
# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating quad_roots_real(1, -2, 1)")
print("Expected: " + str([1.0, 1.0]))
print("Got: " + str(quad_roots_real(1, -2, 1)))


print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating quad_roots_real(1, 0, -1)")
print("Expected: " + str([1.0, -1.0]))
print("Got: " + str(quad_roots_real(1, 0, -1)))


print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating quad_roots_real(2, 2, -12)")
print("Expected: " + str([2.0, -3.0]))
print("Got: " + str(quad_roots_real(2, 2, -12)))

#--------------------------------------------------

# Additional examples to test out-of-bounds.

print("#" + 50*"-")
print("Exercise 2, Example 4:")
print("Evaluating quad_roots_real(0, 0, 0)")
print("Expected: " + str([247, math.sqrt(math.pi)/11]))
print("Got: " + str(quad_roots_real(0, 0, 0)))

print("#" + 50*"-")
print("Exercise 2, Example 5:")
print("Evaluating quad_roots_real(0, 0, 7.0)")
print("Expected: " + str(None))
print("Got: " + str(quad_roots_real(0, 0, 7.0)))

print("#" + 50*"-")
print("Exercise 2, Example 6:")
print("Evaluating quad_roots_real(0, 4.0, 2.0)")
print("Expected: " + str([-0.5, -0.5]))
print("Got: " + str(quad_roots_real(0, 4.0, 2.0)))

print("#" + 50*"-")
print("Exercise 2, Example 7:")
print("Evaluating quad_roots_real(1.0, 0, 1.0)")
print("Expected: " + str(None))
print("Got: " + str(quad_roots_real(1.0, 0, 1.0)))


#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating utility_positive(0.0, 4.7, 0.5)")
print("Expected: " + str(0.0))
print("Got: " + str(utility_positive(0.0, 4.7, 0.5)))


print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating utility_positive(1.0, 1.0, 0.75)")
print("Expected: " + str(1.0))
print("Got: " + str(utility_positive(1.0, 1.0, 0.75)))


print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating utility_positive(4, 16, 0.5)")
print("Expected: " + str(8.0))
print("Got: " + str(utility_positive(4, 16, 0.5)))

#--------------------------------------------------

# Additional examples to test out-of-bounds.


print("#" + 50*"-")
print("Exercise 3, Example 4:")
print("Evaluating utility_positive(-1.0, 1.0, 0.5)")
print("Expected: " + str(None))
print("Got: " + str(utility_positive(-1.0, 1.0, 0.5)))


print("#" + 50*"-")
print("Exercise 3, Example 5:")
print("Evaluating utility_positive(1.0, -1.0, 0.5)")
print("Expected: " + str(None))
print("Got: " + str(utility_positive(1.0, -1.0, 0.5)))


print("#" + 50*"-")
print("Exercise 3, Example 6:")
print("Evaluating utility_positive(1.0, 1.0, -0.5)")
print("Expected: " + str(None))
print("Got: " + str(utility_positive(1.0, 1.0, -0.5)))


print("#" + 50*"-")
print("Exercise 3, Example 7:")
print("Evaluating utility_positive(1.0, 1.0, 1.5)")
print("Expected: " + str(None))
print("Got: " + str(utility_positive(1.0, 1.0, 1.5)))


#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating logit_like(1, 13.7, 0.0, 0.0)")
print("Expected: " + str(math.log(0.5)))
print("Got: " + str(logit_like(1, 13.7, 0.0, 0.0)))


print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating logit_like(0, 0.0, math.log(2), 2.0)")
print("Expected: " + str(math.log(1.0/3.0)))
print("Got: " + str(logit_like(0, 0.0, math.log(2), 2.0)))


print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating logit_like(1, 1.0, 0.0, math.log(5))")
print("Expected: " + str(math.log(5.0/6.0)))
print("Got: " + str(logit_like(1, 1.0, 0.0, math.log(5))))


#--------------------------------------------------

# Additional example to test out-of-bounds.


print("#" + 50*"-")
print("Exercise 4, Example 4:")
print("Evaluating logit_like(7, 1.0, 0.0, math.log(5))")
print("Expected: " + str(None))
print("Got: " + str(logit_like(7, 1.0, 0.0, math.log(5))))

#--------------------------------------------------



print("#" + 50*"-")


##################################################
# End
##################################################
