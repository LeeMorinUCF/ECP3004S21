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
# Demo for Chapter 6: A Modular Approach 
# to Program Organization
# Part B: Designing Modules
#
##################################################
"""



##################################################
# Set Working Directory.
##################################################

import os

# Find out the current directory.
os.getcwd()
# Change to a new directory.
# os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\demo_09_Modules_for_Regression')
os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\demo_10_PP_Ch_06_Testing_Modules')
# Check that the change was successful.
os.getcwd()




##################################################
## Defining Your Own Modules
##################################################

# In Chapter 3, we defined the function convert_to_celsius. 
 

# If you save this function definition into a file named
# temperature.py, you can import it as a module. 

 
import temperature
celsius = temperature.convert_to_celsius(33.3)
print(celsius)

temperature.above_freezing(celsius)

 



#-------------------------------------------------
### What Happens During Import
#-------------------------------------------------

# Let's try an experiment: save the following command in a file 
# called experiment.py. 

 
print("The panda's scientific name is 'Ailuropoda melanoleuca'")

 

# Then import it as a module and see what happens:


 
import experiment

 
# It executed the print statement in the file. 
# This shows that Python *executes the commands in a module*
# when it imports. 

# Now try to import it a second time in the same script.

 
import experiment

 

# The message wasn't printed the second time. 
# Python keeps track of modules that have already been loaded
# and does not execute the scripts twice. 
# This saves time if you import modules that import other modules.
# Sometimes several modules would otherwise import the same module
# multiple times. 

# If you need to edit the commands in a module, the changes would not be updated
# automatically. 
# You can use the imp module to reload the module with your changes. 


# In between the next set of commands, change the print command
# to the following (switching pandas for koalas).

 
print("The koala's scientific name is 'Phascolarctos cinereus'")

 

# Afterward, reload the module with this change.


 
import experiment
# The panda's scientific name is 'Ailuropoda melanoleuca'
# As above.

import experiment
# Nothing printed the second time.


import imp
imp.reload(experiment)
# You should see the updated name.
# The koala's scientific name is 'Phascolarctos cinereus'
# <module 'experiment' from '/Users/.../.../experiment.py'>
 
# Notice the new version is effective after the reload command. 


#-------------------------------------------------
#### Restoring a Module
#-------------------------------------------------

# If you want to reload a module, you could restart Python but the 
# importlib module avoids restarting. 

 
import example
example.x

example.x = 7
example.x

import importlib
example = importlib.reload(example)
example.x

 

# This doesn't work, however, for systems modules, like math. 

 
import math
math.pi

# Take a copy before breaking something.
math_pi_copy = math.pi

# Change the value of math.pi.
math.pi = 3
math.pi

# Try to reload math.
math = importlib.reload(math)
math.pi

 

# It's better to simply avoid overwriting functions or values in modules. 

# Correct the damage.
math.pi = math_pi_copy
math.pi

# But better not to break it in the first place. 


# For the next tests, we will need the following. 

#-------------------------------------------------
### How to run a script within another script
#-------------------------------------------------


# First, we will run a command of the form 
# exec(open("my_script.py").read()) which will
# read the text in the contants of the script
# and execute those commands in __main__. 
# 
# 1.  The open("my_script.py") initializes a connection
#     to interact with the contents of my_script.py. 
# 2.  The my_string.read() method reads the text 
#     from the file my_script.py and returns a string. 
# 3.  Finally the exec() function executes the commands 
#     in the script.



#-------------------------------------------------
### Selecting Which Code Gets Run on Import: __main__
#-------------------------------------------------

# Sometimes you want some commands to run only when the module 
# is run directly but not when it is imported. 
# Python defines a special variable named __name__ to help
# us figure this out. 

# Place this command in the file echo.py:

 
print("__name__ is", __name__)

# Run it with this command (or at the command line, such as GitBash) 
exec(open("echo.py").read())

# If we run this file it outputs this: 

# __name__ is __main__

 

# When we import the script as a module, the following output is produced. 

 
import echo
# It prints
# __name__ is echo

 
# Now follow this with an additional command:
 
import echo

print("After import, __name__ is", __name__, 
	"and echo.__name__ is", echo.__name__)

 


# When Python imports this module, the __name__ variable
# stores the special string __main__ but the variable within the module, 
# echo.__name__ stores the name of the module.



# This means that a module can tell whether it is being run by the main program. 

# Now create another file called main_example.py with the following code. 

 
if __name__ == "__main__":
    print("I am the main program.")
else:
    print("Another module is importing me.")

 

# Try running this script by running the script and by importing the module. 


exec(open("main_example.py").read())

import main_example


# Some modules contain only function modules but others contain programs. 
# The file temperature_program.py contains a set of programs. 

 
exec(open("temperature_program.py").read())

 
# When this module is run, it runs the block of code at the bottom and
# asks the user for input. 

# Now create another module, baking.py that imports the 
# above temperature_program module. 


 
exec(open("baking.py").read())
 

# When baking.py is run, it imports the code at the bottom of
# the temperature_program.py script. 
# If we don't care about running that block of code, then we can place it 
# within an if statement of the form 
# if __name__ == '__main__':.


# Let's make this modification in better_baking.py.

# # <function definitions copied from above>

# if __name__ == '__main__':
#   fahrenheit = float(input('Enter the temperature in degrees Fahrenheit: '))
#   celsius = convert_to_celsius(fahrenheit)
#   if above_freezing(celsius):
#       print('It is above freezing.')
#   else:
#       print('It is below freezing.')

 
# This is what happens when you run the script for this module:
exec(open("better_baking.py").read())



# Compare what happens when these modules are imported.
import better_baking

import baking




##################################################
## Testing Your Code Semiautomatically
##################################################

# The last step after designing the functions in your module is to test them. 



# The doctest module allows us to run the tests that are included 
# in the function docstrings. 


 
import doctest
doctest.testmod()
 

# As an experiment, suppose that we had made an error in our calculation.
# Suppose that instead of (fahrenheit - 32.0) * 5.0 / 9.0 we 
# calculate fahrenheit - 32.0 * 5.0 / 9.0. 
# That is, we forgot to include the parentheses.

# To test this, replace the definition of the convert_to_celsius
# function with this:

 
# def convert_to_celsius(fahrenheit):
#     """ (number) -> float

#     Return the number of Celsius degrees equivalent to fahrenheit degrees.

#     convert_to_celsius(75)
#     23.88888888888889
#     """
                        
#     return fahrenheit - 32.0 * 5.0 / 9.0



# Then, when we run doctest on that module.
# Do this by entering the following commands in the bottom of 
# the script. 

 
# import testmod
# doctest.testmod()




# Run the script with the failure to see what happens.
exec(open("temperature_doctest_fail.py").read())
doctest.testmod()




# **********************************************************************
# File "__main__", line 6, in __main__.convert_to_celsius
# Failed example:
#     convert_to_celsius(75)
# Expected:
#     23.88888888888889
# Got:
#     57.22222222222222
# **********************************************************************
# 1 items had failures:
#    1 of   1 in __main__.convert_to_celsius
# ***Test Failed*** 1 failures.
# TestResults(failed=1, attempted=3)
 

# This test failed. That is finds that the calculation returned an error.
# When calculating convert_to_celsius(75), 
# the expected answer is 23.88888888888889 
# but instead the calculation returns 57.22222222222222. 



# Then run the fixed script to see the result.
exec(open("temperature_doctest_pass.py").read())
doctest.testmod()

# It say that three tests were run but none failed. 
# TestResults(failed=0, attempted=3)



##################################################
# Exercise
##################################################



##################################################
# End
##################################################

