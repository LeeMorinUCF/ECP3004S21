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
# Suggested Solutions for Assignment 4: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module
import numpy as np
import math
import doctest


##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

# Here is a sketch of the solutions.
# I will fix it later to show how edits are displayed on GitHub.
# Stay tuned for the next update. 

def matrix_multiply(mat_1, mat_2):
    """Multiplies two matrices together using loops.
    mat_1 has dimension n_1 and m_1
    mat_2 has dimension n_2 and m_2
    To be conformable, n_1 == m_2.
    It returns a matrix mat_out with n_1 rows and m_2 columns.
    
    This version works sometimes but it is a good start.
    It needs more examples, too.
    
    >>> matrix_multiply(np.full((2,2), 7), np.array([[1.], [2.]]))
    array([[21.], 
           [21.]])

    
    """
    
    # Docstring has to go above the body of the function. 
    
    # First check if the matrices are conformable.
    m_1 = len(mat_2)
    n_1 = len(mat_1[0]) # Won't work for all kinds of arrays. 
    m_2 = len(mat_2)
    n_2 = len(mat_2[0])
    
    if (n_1 != m_2):
        print('Error: Matrices are not conformable.')
        print('Make sure (# columns of mat_1) = (# rows of mat_2).')
        return None
    else:
        # Initialize the output matrix.
        mat_out = np.zeros((m_1, n_2))   
        # Then loop down the rows.
        for i in range(m_1):
            ## For each row, loop through the columns.
            for j in range(n_2):
                # For each element, loop through the
                # row and column combinations.
                sum_element = 0
                for k in range(n_1):
                    sum_i = mat_1[i][k]*mat_2[k][j]
                    sum_element = sum_element + sum_i
                    
                mat_out[i][j] = sum_element
            
    return mat_out

# Indenting returns to margin after body of function.
# Also notice the specific indenting pattern in 
# each block of the loops above. 


# Exercise 2

def ssr_loops(y, x, beta_0, beta_1):
    """Calculates the sum of squared residuals for 
    the bivariate linear regression model.
    y and x are lists of equal length
    and beta_0 and eta_1 are scalar coefficients. 
    
    >>> ssr_loops(y = [2, 2, 2], x = [1, 1, 1], beta_0 = 0.5, beta_1 = 0.5)
    3.0
    >>> ssr_loops(y = [3, 0, 3], x = [0, 2, 2], beta_0 = 1.0, beta_1 = 0.5)
    9.0

    """
    
    ssr = 0
    for i in range(len(y)):
        ssr_i = (y[i] - beta_0 - beta_1*x[i])**2
        ssr = ssr + ssr_i
        
    return ssr


# Exercise 3

def ssr_vec(y, x, beta_0, beta_1):
    """Calculates the sum of squared residuals for 
    the bivariate linear regression model.
    y and x are lists or arrays of equal length
    and beta_0 and eta_1 are scalar coefficients. 
    
    Note that this works for lists or arrays the same shape
    because the call to np.array transforms them to matrix form. 
    
    >>> ssr_loops(y = [2, 2, 2], x = [1, 1, 1], beta_0 = 0.5, beta_1 = 0.5)
    3.0
    >>> ssr_loops(y = [3, 0, 3], x = [0, 2, 2], beta_0 = 1.0, beta_1 = 0.5)
    9.0

    """
    
    ssr = sum((np.array(y) - beta_0 - beta_1*np.array(x))**2)
    
    return ssr


# Exercise 4

# First, review the example from Assignment 3:

def logit_like(y: int, x: float, beta_0: float, beta_1: float) -> float:
    """Calculates the value of the likelihood function
    for the bivariate logistic regression model
    for one observation of x and y 
    and coefficients beta_0 and beta_1.

    >>> logit_like(1, 13.7, 0.0, 0.0)
    -0.6931471805599453
    >>> logit_like(0, 0.0, math.log(2), 2.0)
    -1.0986122886681096
    >>> logit_like(1, 1.0, 0.0, math.log(5))
    -0.1823215567939547
    """
    link = math.exp(beta_0 + x*beta_1)/(1 + math.exp(beta_0 + x*beta_1))
    if y == 0:
        like = math.log(1 - link)
    elif y == 1:
        like = math.log(link)
    else:
        print("Warning: y is not binary. y should be either 1 or 0.")
        like = None

    return like


# Using the function from Assignment 3, 
# the sum is taken over a simple loop:

def logit_like_sum(y: list, x: list, beta_0: float, beta_1: float) -> float:
    """Calculates the value of the likelihood function
    for the bivariate logistic regression model
    for sevaral pairs of observations in the lists x and y
    and coefficients beta_0 and beta_1.
    
    Notice if you are missing the space after the >>>, 
    it causes an error.
    Also, the example without the >>> does not get run.
    
    >>> logit_like_sum([1, 1, 1], [13.7, 12, 437], 0.0, 0.0)
    -2.0794415416798357 # = math.log(8)
    >>> logit_like_sum([1, 0], [1, 1], 0.0, math.log(2))
    -1.504077396776274 # = math.log(2) - math.log(9)
    logit_like_sum([1, 0], [2, 3], math.log(5), math.log(2))
    -3.762362230873739 # = math.log(20) - math.log(21) - math.log(41)
    # Notice it didn't run the third example.
    # doctest confused it with the second example.
    """
    
    like_sum = 0
    for i in range(len(y)):
        like_sum_i = logit_like(y[i], x[i], beta_0, beta_1)
        like_sum = like_sum + like_sum_i
        
    return like_sum

# Indenting should return to the margin after the last return statement 
# in each function definition. 


# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstring
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 




print("#" + 50*"-")
print("# Testing with doctest module")
print("#" + 50*"-")

# Test the examples with doctest.
doctest.testmod()

print("#" + 50*"-")




##################################################
# End
##################################################
