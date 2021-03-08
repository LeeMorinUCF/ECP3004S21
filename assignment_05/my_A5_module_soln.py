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
# Suggested Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for the script my_A5_tests.py.
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

def variance(x: np.ndarray) -> float:
    """
    Calculates the variance of a list or vector array x.
    
    >>> variance([-1, -1, 1, 1])
    1.0
    >>> variance([101, 103, 94, 102, 100])
    10.0
    >>> variance([99,101,99,101,99,101])
    1.0
    
    """
    x = np.array(x)
    
    n = len(x)
    x_bar = sum(x)/n
    
    var = sum((x - x_bar)**2)/n
    
    return var


# Exercise 2

def covariance(y: np.ndarray, x: np.ndarray) -> float:
    """
    Calculates the covariance of two lists or vector arrays
    y and x.
    
    >>> covariance([2, 2, -2, -2], [-1, -1, 1, 1])
    -2.0
    >>> covariance([102, 106, 88, 104, 100], \
                   [101, 103, 94, 102, 100])
    20.0
    >>> covariance([99,101,99,101,99,101], \
                   [99,101,99,101,99,101])
    1.0
    
    """
    
    if len(y) == len(x):
        x = np.array(x)
        y = np.array(y)
        
        n = len(x)
        x_bar = sum(x)/n
        y_bar = sum(y)/n
        
        covar = sum((x - x_bar)*(y - y_bar))/n
        
        return covar
        
    else:
        print("Error: y and x must be the same length.")
        return None



# Exercise 3

def ols_slope(y: np.ndarray, x: np.ndarray) -> float:
    """
    Calculates the slope coefficient 
    by ordinary least squares
    for the linear regesssion model 
    between two lists or vector arrays
    y and x.
    
    >>> ols_slope([2, 2, -2, -2], [-1, -1, 1, 1])
    -2.0
    >>> ols_slope([102, 106, 88, 104, 100], \
                  [101, 103, 94, 102, 100])
    2.0
    >>> ols_slope([99,101,99,101,99,101], \
                  [99,101,99,101,99,101])
    1.0
    
    """
    if len(y) == len(x):
        covar = covariance(y, x)
        var = variance(x)
        
        if var > 0:
                
            slope = covar/var
            
            return slope
        
        else:
            print("Error: x must have positive variance.")
            return None
        
    else:
        print("Error: y and x must be the same length.")
        return None




# Exercise 4

def ols_intercept(y: np.ndarray, x: np.ndarray, 
                  beta_1_hat: float) -> float:
    """
    Calculates the intercept coefficient 
    by ordinary least squares
    for the linear regesssion model 
    between two lists or vector arrays
    y and x.
    
    >>> ols_intercept([2, 2, -2, -2], [-1, -1, 1, 1], -2.0)
    0.0
    >>> ols_intercept([102, 106, 88, 104, 100], \
                  [101, 103, 94, 102, 100], 2.0)
    -100.0
    >>> ols_intercept([99,101,99,101,99,101], \
                  [99,101,99,101,99,101], 1.0)
    0.0
    
    """
    if len(y) == len(x):
        
        x = np.array(x)
        y = np.array(y)
        
        n = len(x)
        x_bar = sum(x)/n
        y_bar = sum(y)/n
        
        intercept = y_bar - beta_1_hat*x_bar
        return intercept
        
    else:
        print("Error: y and x must be the same length.")
        return None
            
    



# Exercise 5

def ssr(y: np.ndarray, x: np.ndarray, 
        beta_0: float, beta_1: float) -> float:
    """Calculates the sum of squared residuals for 
    the bivariate linear regression model.
    y and x are lists or arrays of equal length
    and beta_0 and eta_1 are scalar coefficients. 
    
    Note that this works for lists or arrays the same shape
    because the call to np.array transforms them to matrix form. 
    
    >>> ssr([2, 2, 2], [1, 1, 1], 0.5, 0.5)
    3.0
    >>> ssr([3, 0, 3], [0, 2, 2], 1.0, 0.5)
    9.0
    >>> ssr([2, 3, 4], [1, 2, 3], 1.0, 1.0)
    0.0

    """
    
    if len(y) == len(x):
        
        ssr = sum((np.array(y) - beta_0 - beta_1*np.array(x))**2)
        
        return ssr
        
    else:
        print("Error: y and x must be the same length.")
        return None


# Exercise 6

def min_ssr(y: np.ndarray, x: np.ndarray, 
        beta_0_min: float, beta_0_max: float, 
        beta_1_min: float, beta_1_max: float, 
        step: float) -> float:
    """
    Calculates the slope intercept coefficient 
    by grid search on the sum of squared residuals
    for the linear regesssion model 
    between two lists or vector arrays
    y and x.
    
    The search is taken over a grid of candidate values
    of beta_0 and beta_1 defined over
    np.arange(beta_0_min, beta_0_max, step) and
    np.arange(beta_1_min, beta_1_max, step), respectively.
    
    Note that there is no error handling
    because that is taken care of in ssr() and np.arange(). 
    
    >>> min_ssr([2, 2, -2, -2], [-1, -1, 1, 1], \
                -1.0, 1.0, -3.0, -1.0, 0.1)
    [0.0, -2.0]
    >>> min_ssr([102, 106, 88, 104, 100], \
                [101, 103, 94, 102, 100], \
                -105.0, -95.0, 0.0, 5.0, 0.1)
    [-100.0, 2.0]
    >>> min_ssr([99,101,99,101,99,101], \
                [99,101,99,101,99,101], \
                 -5.0, 5.0, -1.0, 3.0, 0.1)
    [0.0, 1.0]
    
    """
    
    # Define grid of parameters for search.
    beta_0_list = np.arange(beta_0_min, beta_0_max, step)
    beta_1_list = np.arange(beta_1_min, beta_1_max, step)
    # beta_1_list = np.arange(beta_0_min, beta_1_max, step)
    
    # print("beta_0_list = ", beta_0_list)
    # print("beta_1_list = ", beta_1_list)
    
    # Initialize SSR and 
    min_SSR = 999999
    # min_SSR = -1
    i_min = None
    j_min = None
    
    # Loop over candidate values to find a minimum SSR.
    for i in range(len(beta_0_list)):
        for j in range(len(beta_1_list)):
            # print("i = ", i)
            # print("j = ", j)
            
            # Extract candidate values of parameters.
            beta_0 = beta_0_list[i]
            beta_1 = beta_1_list[j]
            
            # Calculate candidate value of SSR.
            SSR_ij = ssr(y, x, beta_0, beta_1)
            
            # Replace values if SSR_ij is a new low.
            if SSR_ij < min_SSR:
                # print(SSR_ij)
                # Keep this as the new lowest value.
                min_SSR = SSR_ij
                # Record the location of the parameter values.
                i_min = i
                j_min = j
                
    # At the end, if a lowest value was found, 
    # output those values.
    if (i_min is not None and j_min is not None):
        return [beta_0_list[i_min], beta_1_list[j_min]]
    else:
        print("No value of SSR was lower than the initial value.")
        print("Choose different values of the parameters for beta_0 and beta_1.")
        return None



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
