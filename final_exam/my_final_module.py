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
# Sample Script for Final Exam: 
# Module with Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for a script that you might call
# my_midterm_tests.py (but is not graded).
##################################################
##################################################
"""






##################################################
# Import Required Modules
##################################################

# import name_of_module


##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1


def function_name_1(x: type) -> type:
    """
    
    Calculates calculates the difference between math.log(x) 
	and some candidate value a, which is a guess of the value of math.log(x).
    
    >>> ln_check(math.exp(7), 3)
    4.0
    >>> function_name_1(arguments)
    answer_you_expect
    >>> function_name_1(arguments)
    answer_you_expect
    
    """
    
    return None



# Exercise 2


def function_name_2(x: type) -> type:
    """
    Preconditions: x_0, iter, tol > 0
    
    Calculates the base of the natural logarithm.
    
    >>> calc_e(2, 10, 0.001)
    2.718281064358138
    >>> function_name_2(arguments)
    answer_you_expect
    >>> function_name_2(arguments)
    answer_you_expect
    
    """
    
    return None



# Exercise 3


def function_name_3(x: type) -> type:
    """
    Calculates the sum of squared residuals 
    for the linear regression model,
    as a function of the slope coefficient only, 
    concentrating out the intercept.
    
    
    >>> SSR_conc(1.0, [3, -3, 3], [1, 1, 1])
    24.0
    >>> function_name_3(arguments)
    answer_you_expect
    >>> function_name_3(arguments)
    answer_you_expect
    
    """
    
    return None


# Exercise 4


def function_name_4(x: type) -> type:
    """
    Calculates the estimated slope coefficient 
    for the linear regression model,
    by minimizing the concentrated sum of squared resduals, 
    which concentrates out the intercept.
    
    >>> ols_slope_conc([2, 1, 2], [1, 0, 1])
    1.0
    >>> function_name_4(arguments)
    answer_you_expect
    >>> function_name_4(arguments)
    answer_you_expect
    
    """
    
    return None



# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstrings above
# with the proper formatting. 

# Test all functions with three examples each. 
# One example is already provided. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# Add code so that the tests are implemented below 
# -- but only when the script is run,
# not when it is imported. 












##################################################
# End
##################################################

