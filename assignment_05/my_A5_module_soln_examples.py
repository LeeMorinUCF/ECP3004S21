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
# Sample Script for Assignment 5: 
# Importing Function Definitions and Testing
#
##################################################
"""



##################################################
# Import Required Modules
##################################################

# import os
# import doctest


# Import functions for handling exceptions.
import traceback
import logging
import sys
# This redirects errors to the output file (or stdout). 
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


##################################################
# Set Working Directory.
##################################################

# No need to do this because I am running it in the
# same directory as where the module is located.

# # Find out the current directory.
# os.getcwd()
# # Change to a new directory.
# os.chdir('C:\\Users\\user_name\\path\\to\\your\\repo\\assignment_04')
# # Check that the change was successful.
# os.getcwd()



##################################################
# Read script and test.
##################################################


# Read the script my_A4_functions.py to run the tests. 
exec(open("my_A5_module_soln.py").read())


# doctest.testmod()



##################################################
# Import your module and use it on some examples
##################################################

# Optional (not graded): 
# Use this as a scratchpad to test your functions
# and print out results.

# Get your testing it out of your system here and 
# keep the printing and testing out of the 
# my_A4_functions module. 


import my_A5_module_soln as A5


# Test the examples and print the results.

print("#" + 50*"-")
print("# Testing with examples in solutions")
print("#" + 50*"-")

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

#--------------------------------------------------

print("#" + 50*"-")
print("Exercise 1, Example 1:")
eval_str = "A5.variance([-1, -1, 1, 1])"
ans_str = str("1.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.variance([-1, -1, 1, 1])
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 1, Example 2:")
eval_str = "A5.variance([101, 103, 94, 102, 100])"
ans_str = str("10.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.variance([101, 103, 94, 102, 100])
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 1, Example 3:")
eval_str = "A5.variance([99,101,99,101,99,101])"
ans_str = str("1.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.variance([99,101,99,101,99,101])
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

#--------------------------------------------------

print("#" + 50*"-")
print("Exercise 2, Example 1:")
eval_str = "A5.covariance([2, 2, -2, -2], [-1, -1, 1, 1])"
ans_str = str("-2.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.covariance([2, 2, -2, -2], [-1, -1, 1, 1])
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 2, Example 2:")
eval_str = "A5.covariance([102, 106, 88, 104, 100], \
                   [101, 103, 94, 102, 100])"
ans_str = str("20.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.covariance([102, 106, 88, 104, 100], \
                   [101, 103, 94, 102, 100])
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 2, Example 3:")
eval_str = "A5.covariance([99,101,99,101,99,101], \
                   [99,101,99,101,99,101])"
ans_str = str("1.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.covariance([99,101,99,101,99,101], \
                   [99,101,99,101,99,101])
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

#--------------------------------------------------

print("#" + 50*"-")
print("Exercise 3, Example 1:")
eval_str = "A5.ols_slope([2, 2, -2, -2], [-1, -1, 1, 1])"
ans_str = str("-2.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.ols_slope([2, 2, -2, -2], [-1, -1, 1, 1])
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 3, Example 2:")
eval_str = "A5.ols_slope([102, 106, 88, 104, 100], \
                  [101, 103, 94, 102, 100])"
ans_str = str("2.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.ols_slope([102, 106, 88, 104, 100], \
                  [101, 103, 94, 102, 100])
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 3, Example 3:")
eval_str = "A5.ols_slope([99,101,99,101,99,101], \
                  [99,101,99,101,99,101])"
ans_str = str("1.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.ols_slope([99,101,99,101,99,101], \
                  [99,101,99,101,99,101])
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

#--------------------------------------------------

print("#" + 50*"-")
print("Exercise 4, Example 1:")
eval_str = "A5.ols_intercept([2, 2, -2, -2], [-1, -1, 1, 1], -2.0)"
ans_str = str("0.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.ols_intercept([2, 2, -2, -2], [-1, -1, 1, 1], -2.0)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 4, Example 2:")
eval_str = "A5.ols_intercept([102, 106, 88, 104, 100], \
                  [101, 103, 94, 102, 100], 2.0)"
ans_str = str("-100.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.ols_intercept([102, 106, 88, 104, 100], \
                  [101, 103, 94, 102, 100], 2.0)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 4, Example 3:")
eval_str = "A5.ols_intercept([99,101,99,101,99,101], \
                  [99,101,99,101,99,101], 1.0)"
ans_str = str("0.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.ols_intercept([99,101,99,101,99,101], \
                  [99,101,99,101,99,101], 1.0)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 5.")

#--------------------------------------------------

print("#" + 50*"-")
print("Exercise 5, Example 1:")
eval_str = "A5.ssr([2, 2, 2], [1, 1, 1], 0.5, 0.5)"
ans_str = str("3.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.ssr([2, 2, 2], [1, 1, 1], 0.5, 0.5)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 5, Example 2:")
eval_str = "A5.ssr([3, 0, 3], [0, 2, 2], 1.0, 0.5)"
ans_str = str("9.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.ssr([3, 0, 3], [0, 2, 2], 1.0, 0.5)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 5, Example 3:")
eval_str = "A5.ssr([2, 3, 4], [1, 2, 3], 1.0, 1.0)"
ans_str = str("0.0")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.ssr([2, 3, 4], [1, 2, 3], 1.0, 1.0)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 6.")

#--------------------------------------------------

print("#" + 50*"-")
print("Exercise 6, Example 1:")
eval_str = "A5.min_ssr([2, 2, -2, -2], [-1, -1, 1, 1], \
                -1.0, 1.0, -3.0, -1.0, 0.1)"
ans_str = str("[0.0, -2.0]")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.min_ssr([2, 2, -2, -2], [-1, -1, 1, 1], \
                -1.0, 1.0, -3.0, -1.0, 0.1)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 6, Example 2:")
eval_str = "A5.min_ssr([102, 106, 88, 104, 100], \
                [101, 103, 94, 102, 100], \
                -105.0, -95.0, 0.0, 5.0, 0.1)"
ans_str = str("[-100.0, 2.0]")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.min_ssr([102, 106, 88, 104, 100], \
                [101, 103, 94, 102, 100], \
                -105.0, -95.0, 0.0, 5.0, 0.1)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())

print("#" + 50*"-")
print("Exercise 6, Example 3:")
eval_str = "A5.min_ssr([99,101,99,101,99,101], \
                [99,101,99,101,99,101], \
                 -5.0, 5.0, -1.0, 3.0, 0.1)"
ans_str = str("[0.0, 1.0]")
print("Evaluating " + eval_str)
print("Expected: " + ans_str)
try:
    print("Got: \n")
    print(str(
        A5.min_ssr([99,101,99,101,99,101], \
                [99,101,99,101,99,101], \
                 -5.0, 5.0, -1.0, 3.0, 0.1)
        ))
except:
    print("Error in" + eval_str)
    logging.error(traceback.format_exc())






##################################################
# End
##################################################

