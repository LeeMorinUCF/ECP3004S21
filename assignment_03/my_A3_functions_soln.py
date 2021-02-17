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
# Sample Script for Assignment 3: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module
import math
from typing import List
import doctest



##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def quad_roots_1(a: float, b: float, c: float) -> List[float]:
    """Precondition: a != 0 & b**2 - 4ac >= 0
    The real-valued roots of the quadratic equation
    a*x**2 + b*x + c
    with the coefficients listed in the parameters.

    >>> quad_roots_1(1, -2, 1)
    [1.0, 1.0]
    >>> quad_roots_1(1, 0, -1)
    [1.0, -1.0]
    >>> quad_roots_1(2, 2, -12)
    [2.0, -3.0]
    """
    num_1 = - b 
    num_2 = math.sqrt(b**2 - 4*a*c) 
    denom = 2*a 
    root_1 = (num_1 + num_2)/denom
    root_2 = (num_1 - num_2)/denom

    return [root_1, root_2]



# Define the rest of your functions for Exercises 2-4.
 

# Exercise 2

def quad_roots_real(a: float, b: float, c: float) -> List[float]:
    """Real-valued roots of the quadratic equation
    a*x**2 + b*x + c
    with the coefficients listed in the parameters.

    >>> quad_roots_real(1, -2, 1)
    [1.0, 1.0]
    >>> quad_roots_real(1, 0, -1)
    [1.0, -1.0]
    >>> quad_roots_real(2, 2, -12)
    [2.0, -3.0]
    """
    if a == 0 and b == 0 and c == 0:
        return [247, math.sqrt(math.pi)/11]
    elif a == 0 and b == 0:
        return None
    elif a == 0:
        return [-c/b, -c/b]
    elif b**2 - 4*a*c < 0:
        return None
    else:
        
        num_1 = - b 
        num_2 = math.sqrt(b**2 - 4*a*c) 
        denom = 2*a 
        root_1 = (num_1 + num_2)/denom
        root_2 = (num_1 - num_2)/denom
        return [root_1, root_2]




# Exercise 3

def utility_positive(x: float, y: float, alpha: float) -> float:
    """Calculates the value of the Cobb-Douglass utility
    function for consumption goods x and y with exponent alpha.
    It restricts x and y to non-negative values and 
    alpha to the unit interval.

    >>> utility_positive(1.0, 1.0, 0.75)
    1.0
    >>> utility_positive(4, 16, 0.5)
    8.0
    >>> utility_positive(0.0, -4.7, 0.5)
    None
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
    
    # Calculate the output when all cases are well-defined. 
    if x < 0 or y < 0 or alpha < 0 or alpha > 1:
        utils = None
    else:
        utils = x**(alpha)*y**(1 - alpha)

    return utils


# Exercise 4

def logit_like(y: int, x: float, beta_0: float, beta_1: float) -> float:
    """Calculates the value of the Cobb-Douglass utility
    function for consumption goods x and y with exponent alpha.

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



# Only function definitions above this point. 


##################################################
# Run the examples to test these functions
##################################################



print("#" + 50*"-")
print("# Testing with doctest module")
print("#" + 50*"-")

# Test the examples with doctest.
doctest.testmod()


# Test the examples and print the results. 

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating quad_roots_1(1, -2, 1)")
print("Expected: " + str([1.0, 1.0]))
print("Got: " + str(quad_roots_1(1, -2, 1)))


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating quad_roots_1(1, 0, -1)")
print("Expected: " + str([1.0, -1.0]))
print("Got: " + str(quad_roots_1(1, 0, -1)))


print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating quad_roots_1(2, 2, -12)")
print("Expected: " + str([2.0, -3.0]))
print("Got: " + str(quad_roots_1(2, 2, -12)))


# Continue with the rest of your examples.
# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating quad_roots_real(1, -2, 1)")
print("Expected: " + str([1.0, 1.0]))
print("Got: " + str(quad_roots_real(1, -2, 1)))


print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating quad_roots_real(1, 0, -1)")
print("Expected: " + str([1.0, -1.0]))
print("Got: " + str(quad_roots_real(1, 0, -1)))


print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating quad_roots_real(2, 2, -12)")
print("Expected: " + str([2.0, -3.0]))
print("Got: " + str(quad_roots_real(2, 2, -12)))

#--------------------------------------------------

# Additional examples to test out-of-bounds.

print("#" + 50*"-")
print("Exercise 2, Example 4:")
print("Evaluating quad_roots_real(0, 0, 0)")
print("Expected: " + str([247, math.sqrt(math.pi)/11]))
print("Got: " + str(quad_roots_real(0, 0, 0)))

print("#" + 50*"-")
print("Exercise 2, Example 5:")
print("Evaluating quad_roots_real(0, 0, 7.0)")
print("Expected: " + str(None))
print("Got: " + str(quad_roots_real(0, 0, 7.0)))

print("#" + 50*"-")
print("Exercise 2, Example 6:")
print("Evaluating quad_roots_real(0, 4.0, 2.0)")
print("Expected: " + str([-0.5, -0.5]))
print("Got: " + str(quad_roots_real(0, 4.0, 2.0)))

print("#" + 50*"-")
print("Exercise 2, Example 7:")
print("Evaluating quad_roots_real(1.0, 0, 1.0)")
print("Expected: " + str(None))
print("Got: " + str(quad_roots_real(1.0, 0, 1.0)))


#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating utility_positive(0.0, 4.7, 0.5)")
print("Expected: " + str(0.0))
print("Got: " + str(utility_positive(0.0, 4.7, 0.5)))


print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating utility_positive(1.0, 1.0, 0.75)")
print("Expected: " + str(1.0))
print("Got: " + str(utility_positive(1.0, 1.0, 0.75)))


print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating utility_positive(4, 16, 0.5)")
print("Expected: " + str(8.0))
print("Got: " + str(utility_positive(4, 16, 0.5)))

#--------------------------------------------------

# Additional examples to test out-of-bounds.


print("#" + 50*"-")
print("Exercise 3, Example 4:")
print("Evaluating utility_positive(-1.0, 1.0, 0.5)")
print("Expected: " + str(None))
print("Got: " + str(utility_positive(-1.0, 1.0, 0.5)))


print("#" + 50*"-")
print("Exercise 3, Example 5:")
print("Evaluating utility_positive(1.0, -1.0, 0.5)")
print("Expected: " + str(None))
print("Got: " + str(utility_positive(1.0, -1.0, 0.5)))


print("#" + 50*"-")
print("Exercise 3, Example 6:")
print("Evaluating utility_positive(1.0, 1.0, -0.5)")
print("Expected: " + str(None))
print("Got: " + str(utility_positive(1.0, 1.0, -0.5)))


print("#" + 50*"-")
print("Exercise 3, Example 7:")
print("Evaluating utility_positive(1.0, 1.0, 1.5)")
print("Expected: " + str(None))
print("Got: " + str(utility_positive(1.0, 1.0, 1.5)))


#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating logit_like(1, 13.7, 0.0, 0.0)")
print("Expected: " + str(math.log(0.5)))
print("Got: " + str(logit_like(1, 13.7, 0.0, 0.0)))


print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating logit_like(0, 0.0, math.log(2), 2.0)")
print("Expected: " + str(math.log(1.0/3.0)))
print("Got: " + str(logit_like(0, 0.0, math.log(2), 2.0)))


print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating logit_like(1, 1.0, 0.0, math.log(5))")
print("Expected: " + str(math.log(5.0/6.0)))
print("Got: " + str(logit_like(1, 1.0, 0.0, math.log(5))))


#--------------------------------------------------

# Additional example to test out-of-bounds.


print("#" + 50*"-")
print("Exercise 4, Example 4:")
print("Evaluating logit_like(7, 1.0, 0.0, math.log(5))")
print("Expected: " + str(None))
print("Got: " + str(logit_like(7, 1.0, 0.0, math.log(5))))

#--------------------------------------------------



##################################################
# End
##################################################