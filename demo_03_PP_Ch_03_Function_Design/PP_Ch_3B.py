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
# January 10, 2021
# 
##################################################
#
# Demo for Chapter 3: Functions
# Part B: Designing Functions
#
##################################################
"""

##################################################
## The Function Design Recipe
##################################################

# The five steps to function design are as follows:

# 1. **Examples** Type a few example calls and determine what it 
#     should return for those values. 
#     The name of your function should indicate what is being 
#     calculated in your examples. 
# 2. **Description** Write a few sentences to describe what 
#     your function does. 
# 3. **Header** Type some documentation relating to your function. 
#     It should be clear to the reader what arguments it takes 
#     as input and what value is returned and the types of each variable. 
# 4. **Body** By now, you should be clear about how your function 
#     will work. 
#     Now type the code to perform the calculations. 
# 5. **Test** Run the examples from step 1 to verify that your 
#     function works as expected. 


##################################################
## Function Design Example
##################################################


# Consider the simple example of the function ```add_two_numbers``` 
# that, well, adds two numbers.

# Define a function without documentation.
def add_two_numbers(first_number, second_number):
    
    total = first_number + second_number
    
    return total


# The function is fine but how does the user know how it works. 
# Guessing is only reasonable if the function is simple. 

add_two_numbers(3,4)
# 7


# That makes sense and it appears to work. 
# If your user wants to know for sure, they can
# search for documentation, as you would for any other function.

help(add_two_numbers)
# Help on function add_two_numbers in module __main__:
# 
# add_two_numbers(first_number, second_number)


# There's not much there yet.


# You could print the entire function object but that
# is not very convenient for long and complex functions.

add_two_numbers
# <function __main__.add_two_numbers(first_number, second_number)>

# Instead, add documentation to the function in a docstring.


def add_two_numbers(first_number, second_number):
    """ Add two numbers together and return the sum.
    
    """
    
    total = first_number + second_number
    
    return total




# Now test the documentation by calling for help:

help(add_two_numbers)
# Help on function add_two_numbers in module __main__:

# add_two_numbers(first_number, second_number)
#     Add two numbers together and return the sum.
    
    
# Notice the content from the description in the docstring.

# We can improve the docstring by including examples, 
# so now let's cover all of these step by following
# the *function design recipe*. 



##################################################
## Function Design Recipe
##################################################

# Now apply the function design recipe to the ```add_two_numbers``` example.

#-------------------------------------------------
### Examples
#-------------------------------------------------

# Try to think of some examples that will test the limit of your function. 
# Note that we can run the tests only because we have already defined the 
# function in the examples above.

add_two_numbers(3,4)
# 7
add_two_numbers(0,4)
# 4
add_two_numbers(-3,3)
# 0


# Now you know that your function will have a form like this.


def add_two_numbers(first_number, second_number):
    
    
    
    return total




#-------------------------------------------------
### Header
#-------------------------------------------------

# Write a header to contain information about the
# the types of variables in your function. 


def add_two_numbers(first_number: float, second_number: float) -> float:
    
    
    
    return total



#-------------------------------------------------
### Description
#-------------------------------------------------

# Add a description of what your function does, in words.
# Include the list of your examples.

def add_two_numbers(first_number: float, second_number: float) -> float:
    """ Add two numbers together and return the sum.
    >>> add_two_numbers(3,4)
    7
    >>> add_two_numbers(0,4)
    4
    >>> add_two_numbers(-3,3)
    0
    """
    
    
    
    return total




#-------------------------------------------------
### Body
#-------------------------------------------------

# In this case, the body is simple but this is often the most work. 

def add_two_numbers(first_number: float, second_number: float) -> float:
    """ Add two numbers together and return the sum.
    >>> add_two_numbers(3,4)
    7
    >>> add_two_numbers(0,4)
    4
    >>> add_two_numbers(-3,3)
    0
    """
    
    total = first_number + second_number
    
    return total



# It seems like a lot of work to do to prepare to write one line of code.
# With more elaborate functions, having clearly stated the 
# examples, header and description, 
# you should be clear about what it is you will compute and the planning will pay off. 



#-------------------------------------------------
### Test
#-------------------------------------------------

# Finally, test your functions to confirm accuracy. 


add_two_numbers(3,4)
# 7
add_two_numbers(0,4)
# 4
add_two_numbers(-3,3)
# 0

# If all goes well, these examples should all return 
# the values you expect. 
# If not, be sure that your examples are correct
# or modify your function definition. 
# Most of the work in coding is correcting your mistakes. 






##################################################
## End
##################################################

