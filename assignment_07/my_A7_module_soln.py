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
# Sample Script for Assignment 7: 
# Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for the script my_A6_tests.py.
##################################################
##################################################
"""






##################################################
# Import Required Modules
##################################################

# import name_of_module
# from scipy.optimize import minimize

# Added to plot the function before attempting to minimize. 
import numpy as np
import matplotlib.pyplot as plt



##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

# The function

def g(x: float) -> float:
    """The function to optimize.

    >>> g(0)
    0
    >>> g(2)
    0
    >>> g(-2)
    0
    """
    
    return (x - 2)*x*(x + 2)**2


def g_prime(x: float) -> float:
    """The first derivative of the function to optimize.

    >>> g_prime(0)
    -8
    >>> g_prime(2)
    32
    >>> g_prime(-2)
    0
    """
    
    return 4*x**3 + 6*x**2 - 8*x - 8


def g_2prime(x: float) -> float:
    """The second derivative of the function to optimize.

    >>> g_2prime(0)
    -8
    >>> g_2prime(2)
    64
    >>> g_2prime(-2)
    16
    """
    
    return 12*x**2 + 12*x - 8



##################################################
# Optimization
# Step 1: Plot the Function
# (not required for assignment)
##################################################

# Although this was not required, it helps 
# to plot a function to give some intuition about
# where to start the search for an optimum. 

# Calculate function values across a grid of values of x.
x_grid = np.arange(-5, 5, 0.01)
g_grid = g(x_grid)


plt.figure()
plt.plot(x_grid, g_grid, label='f(x)' )
plt.plot(x_grid, 0*g_grid)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()


# Zoom in because it is difficult to see the minimum. 
x_grid = np.arange(-2.5, 2, 0.01)
g_grid = g(x_grid)


plt.figure()
plt.plot(x_grid, g_grid, label='f(x)' )
plt.plot(x_grid, 0*g_grid)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()



# Also consider the slope of g(x). 
x_grid = np.arange(-2.5, 2, 0.01)
g_grid = g_prime(x_grid)


plt.figure()
plt.plot(x_grid, g_grid, label='f(x)' )
plt.plot(x_grid, 0*g_grid)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()



##################################################
# Optimization
# Step 2: Design the Algorithm
##################################################


# Exercise 2

def newton_g_opt(x_0: float, maxiter: int, tol: float) -> float:
    """Calculates optimal value of function g(x)
    using Newton's method.

    >>> newton_g_opt(-2, 100, 0.001)
    -2
    >>> newton_g_opt(0, 100, 0.000001)
    -0.7807763785162698
    >>> newton_g_opt(2, 100, 0.001)
    1.2814640376674955
    """
    
    x = x_0
    for i in range(maxiter):
        x_next = x - g_prime(x)/g_2prime(x)
        if abs(x_next - x) < tol:
            print('Optimization terminated successfully.')
            print('Current parameter value: ' + str(x))
            print('Iterations: ' + str(i))
            # return x_next
            break
        x = x_next
        
    if i == maxiter - 1 and x_next - x > tol:
        print('Optimization terminated after maximum number of iterations.')
    
    # Return the minimizing value of function g(x). 
    return x



# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstrings
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# The tests are implemented below -- but only
# when the script is run, not when it is imported. 


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    






##################################################
# End
##################################################
