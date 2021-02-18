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

import os
import doctest


##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
os.chdir('C:\\Users\\user_name\\path\\to\\your\\repo\\assignment_04')
# Check that the change was successful.
os.getcwd()



##################################################
# Read script and test.
##################################################


# Read the script my_A4_functions.py to run the tests. 
exec(open("my_A5_module.py").read())


doctest.testmod()



##################################################
# Import your module and use it on some examples
##################################################

# Optional (not graded): 
# Use this as a scratchpad to test your functions
# and print out results.

# Get your testing it out of your system here and 
# keep the printing and testing out of the 
# my_A4_functions module. 


import my_A5_module

# Insert examples like this for any tests you want to try.
my_A5_module.ssr([2, 2, 2], [1, 1, 1], 0, 2)


# ...


##################################################
# End
##################################################

