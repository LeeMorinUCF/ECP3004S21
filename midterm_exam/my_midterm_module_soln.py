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
# Sample Script for Midterm Exam: 
# Suggested Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for a script that you might call
# my_midterm_tests.py.
##################################################
##################################################
"""






##################################################
# Import Required Modules
##################################################

# import name_of_module
# import math
import numpy as np


##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

# Sample function for sample script.
# def function_name(x: type) -> type:
#     """
#     Calculates something.
    
#     >>> function_name(arguments)
#     answer_you_expect
    
#     """
    
#     return None


def in_budget(x: float, y: float, p_x: float, p_y: float, w: float) -> bool:
    """
    Preconditions: x, y, w >= 0 and p_x, p_y > 0
    
    Calculates returns a boolean indicator 
    of whether the consumer's expenditure 
    is less than or equal to wealth.
    
    >>> in_budget(3, 1, 10, 25, 100)
    True
    >>> in_budget(5, 5, 10, 20, 120)
    False
    >>> in_budget(5.0, 7.5, 5, 10, 100)
    True
    
    """
    
    if x < 0 or y < 0 or p_x <= 0 or p_y <= 0 or w < 0:
        print("Error: all arguments must be non-negative")
        print("and prices must be positive.")
        return None
    
    else:
        return x*p_x + y*p_y <= w


# Exercise 2

def calc_bundle(p_x: float, p_y: float, w: float, alpha: float) -> float:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    
    >>> calc_bundle(10, 25, 100, 0.5)
    [5.0, 2.0]
    >>> calc_bundle(10, 20, 120, 1.0/3.0)
    [4.0, 4.0]
    >>> calc_bundle(5, 10, 100, 0.25)
    [5.0, 7.5]
    
    """
    if p_x <= 0 or p_y <= 0 or w < 0 or alpha < 0 or alpha > 1:
        print("Error: all arguments must be non-negative")
        print("and prices must be positive")
        print("and alpha must be between zero and one.")
        return None
    
    else:
        x_star = alpha*w/p_x
        y_star = (1 - alpha)*w/p_y
        return [x_star, y_star]



# Exercise 3

def y_solve(x_star: type, p_x: float, p_y: float, w: float) -> float:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= x_star <= w/p_x
    
    Calculates the remaining expenditure on good y, 
    given an expenditure x_star in good x.
    
    >>> y_solve(5, 10, 25, 100)
    2.0
    >>> y_solve(4, 10, 20, 120)
    4.0
    >>> y_solve(5, 5, 10, 100)
    7.5
    
    """
    if p_x <= 0 or p_y <= 0 or w < 0 or x_star < 0 or x_star > w/p_x:
        print("Error: all arguments must be non-negative")
        print("and prices must be positive")
        print("and x_star must be less than w/p_x.")
        return None
    
    else:
        y_star = (w - x_star*p_x)/p_y
        return y_star


# Exercise 4


def one_loop_bundle(p_x: float, p_y: float, w: float, alpha: float, 
                    step: float) -> float:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    It searches over a loop on x_star and assigns the remaining
    wealth to y using y_solve.
    
    >>> one_loop_bundle(10, 25, 100, 0.5, 0.01)
    [5.0, 2.0]
    >>> one_loop_bundle(10, 20, 120, 1.0/3.0, 0.01)
    [4.0, 4.0]
    >>> one_loop_bundle(5, 10, 100, 0.25, 0.01)
    [5.0, 7.5]
    
    """
    if p_x <= 0 or p_y <= 0 or w < 0 or alpha < 0 or alpha > 1:
        print("Error: all arguments must be non-negative")
        print("and prices must be positive")
        print("and alpha must be between zero and one.")
        return None
    
    else:
        max_util = -1
        x_star = None
        y_star = None
        
        x_star_list = np.arange(0, w/p_x, step)
        
        for i in range(len(x_star_list)):
            x_i = x_star_list[i]
            y_i = y_solve(x_i, p_x, p_y, w)
            util_i = x_i**alpha * y_i**(1 - alpha)
            
            if util_i > max_util:
                x_star = x_i
                y_star = y_i
                max_util = util_i
                
        return [x_star, y_star]



# Exercise 5

def util_in_budget(x: float, y: float, p_x: float, p_y: float, 
                   w: float, alpha: float) -> float:
    """Calculates the value of the Cobb-Douglass utility
    function for consumption goods x and y with exponent alpha.
    It restricts x and y to non-negative values and 
    alpha to the unit interval.
    It also restricts the calculation to bundles [x, y] within budget w.
    
    The following examples evaluate to:
    math.sqrt(5)*math.sqrt(2)
    4**(1.0/3.0)*4**(2.0/3.0)
    5**0.25 * 7.5**0.75

    >>> util_in_budget(5, 2, 10, 25, 100, 0.5)
    3.1622776601683795
    >>> util_in_budget(4, 4, 10, 20, 120, 1.0/3.0)
    4.0
    >>> util_in_budget(5.0, 7.5, 5, 10, 100, 0.25)
    6.777015027073836
    """
    # Several independent conditions for warning messages.
    if x < 0:
        print("Warning: x < 0. x should be non-negative.")
    if y < 0:
        print("Warning: y < 0. y should be non-negative.")
    if alpha < 0:
        print("Warning: alpha < 0. alpha should be non-negative.")
    if alpha > 1:
        print("Warning: alpha > 1. alpha should be less than or equal to one.")
    
    # New conditions for prices and wealth.
    if p_x <= 0 or p_y <= 0 or w < 0:
        print("Error: all arguments must be non-negative")
        print("and prices must be positive")
        print("and alpha must be between zero and one.")
    
    # One more condition to check whether the bundle is within budget.
    x_y_in_budget = in_budget(x, y, p_x, p_y, w)
    # Warning is noisy if running in a loop.
    # if not x_y_in_budget:
        # print("Warning: Bundle of goods [x, y] not within budget w.")
        
    
    # Calculate the output when all cases are well-defined. 
    if x < 0 or y < 0 or alpha < 0 or alpha > 1 or \
        p_x <= 0 or p_y <= 0 or w < 0 or not x_y_in_budget:
        utils = 0
    else:
        utils = x**(alpha)*y**(1 - alpha)

    return utils





# Exercise 6

def two_loop_bundle(p_x: float, p_y: float, w: float, alpha: float, 
                    step: float) -> float:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    It searches over two loops on x_star and y_star.
    
    Note that there is no error handling
    because that is taken care of in util_in_budget() and np.arange(). 
    
    >>> two_loop_bundle(10, 25, 100, 0.5, 0.01)
    [5.0, 2.0]
    >>> two_loop_bundle(10, 20, 120, 1.0/3.0, 0.01)
    [4.0, 4.0]
    >>> two_loop_bundle(5, 10, 100, 0.25, 0.01)
    [5.0, 7.5]
    
    """
    
    # Define grid of parameters for search.
    x_star_list = np.arange(0, w/p_x, step)
    y_star_list = np.arange(0, w/p_y, step)
    
    # Initialize util and indices.
    max_util = -1
    i_max = None
    j_max = None
    
    # Loop over candidate values to find a minimum SSR.
    for i in range(len(x_star_list)):
        for j in range(len(y_star_list)):
            # print("i = ", i)
            # print("j = ", j)
            
            # Extract candidate values of parameters.
            x_i = x_star_list[i]
            y_j = y_star_list[j]
            
            # Calculate candidate value of utility function.
            util_ij = util_in_budget(x_i, y_j, p_x, p_y, w, alpha)
            
            # Replace values if SSR_ij is a new high.
            if util_ij > max_util:
                # Keep this as the new highest value.
                max_util = util_ij
                # Record the location of the parameter values.
                i_max = i
                j_max = j
                
    # At the end, if a higest value was found, 
    # output those values.
    if (i_max is not None and j_max is not None):
        return [x_star_list[i_max], y_star_list[j_max]]
    else:
        print("No value of utility was higher than the initial value.")
        print("Choose different values of the parameters, if necessary.")
        return None



# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstrings above
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# Add code so that the tests are implemented below 
# -- but only when the script is run,
# not when it is imported. 


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    






##################################################
# End
##################################################
