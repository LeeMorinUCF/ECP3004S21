# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business 
# University of Central Florida
#
# January 19, 2021
# 
##################################################
#
# Demo for Chapter 6, Part B: Testing Modules
# Sample Script for Testing Modules
#
##################################################
"""




##################################################
# Import Modules.
##################################################


import os # To set working directory
import doctest # To test modules


##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\demo_10_PP_Ch_06_Testing_Modules')
# Check that the change was successful.
os.getcwd()



##################################################
# Test Versions of birthday.py
##################################################



# First, we will run a command of the form 
# exec(open("birthday_v1.py").read()) which will
# read the text in the contants of the script
# and execute those commands in __main__. 
# 
# 1.  The open("my_script.py") initializes a connection
#     to interact with the contents of my_script.py. 
# 2.  The my_string.read() method reads the text 
#     from the file my_script.py and returns a string. 
# 3.  Finally the exec() function executes the commands 
#     in the script, which may include __main__.


# Next, we will use the testmod module to test the
# examples in the docstrings of the functions in the 
# modules. Note that this will not run the code in
# the block if __name__ == "__main__":



##################################################
# Test of birthday_v1
##################################################

# Run the script to run examples in __main__.
exec(open("birthday_v1.py").read())
# This also puts the function definitions in memory.


# You can use the modules in PP_Ch_06_B.py 
# to reload your module after making changes. 
# import imp
# imp.reload(birthday_v1)


# Run the examples to test examples in the docstrings 
# of the functions in this module. 


doctest.testmod()

# There were some failures.
# Take a look at the functions and determine
# the causes of the failures.
# Make some adjustments and test it again.


##################################################
# Test of birthday_v2
##################################################


# Run the script to run examples in __main__.
exec(open("birthday_v2.py").read())
# This also puts these new function definitions in memory.


# Run the examples to test examples in the docstrings 
# of the functions in this module. 
doctest.testmod()

# Not as many failures this time but this time a different
# failure occurred. Make more adjustments and test it again.


##################################################
# Test of birthday_v3
##################################################


# Run the script to run examples in __main__.
exec(open("birthday_v3.py").read())
# Again, this overwrites the function definitions.


# Run the examples to test examples in the docstrings 
# of the functions in this module. 
doctest.testmod()

# Success! No failures. 

# During code development, you can put the commands
# import doctest
# doctest.testmod()
# inside the block if __name__ == "__main__":
# and it will automatically test your examples.
# This is useful if you make changes to your
# functions because you can monitor your progress
# when debugging but also find out if your "fix"
# actually broke something else. 


##################################################
# End
##################################################

