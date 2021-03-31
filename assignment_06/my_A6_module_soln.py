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
# Sample Script for Assignment 6: 
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



##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def z_squared_diff(x: float, z: float) -> float:
    """Calculates the difference from the square root of z.
    
    >>> z_squared_diff(3.0, 9.0)
    0.0
    >>> z_squared_diff(5.0, 24.0)
    1.0
    >>> z_squared_diff(2.0, 0.0)
    4.0
    """
    
    return x**2 - z


# Exercise 2

def sqrt_z_bisect(z: float, a_0: float, b_0: float, num_iter: int) -> float:
    """Solves for the root of the function z_squared_diff 
    using the bisection method.
    
    >>> sqrt_z_bisect(9.0, 2.0, 4.0, 10)
    3.0
    >>> sqrt_z_bisect(25.0, 2.0, 7.0, 20)
    5.0
    >>> sqrt_z_bisect(2.0, 1.0, 2.0, 10)
    1.4142135623730951
    """
    
    # First verify that the interval is nonempty. 
    if a_0 > b_0:
        print('Error: interval must be nonempty (a_0 <= b_0).')
        return None
    
    # Also verify that the interval contains a root.
    if z_squared_diff(a_0, z) > 0:
        print("Error: f(a_0) is not negative.")
        return None
    if z_squared_diff(b_0, z) < 0:
        print("Error: f(b_0) is not positive.")
        return None
        
    # Notice that this function assumes that the function
    # is monotonically increasing (which it is). 
    # Otherwise, the conditions depend on whether
    # a_i or b_i is negative and the other is positive. 
    
    # For generic functions, you might use the following
    # test for a proper interval. 
    if z_squared_diff(a_0, z)*z_squared_diff(b_0, z) > 0:
        print("Error: f(a_0) and f(b_0) must have different sign.")
        return None
    
    
    
    a_i = a_0
    b_i = b_0
    for i in range(num_iter):
        
        # Calculate the midpoint.
        m_i = (a_i + b_i)/2
        # Evaluate the objective function.
        f_m_i = z_squared_diff(m_i, z)
        
        # Based on the sign of f_m_i, 
        # assign the midpoint to replace an endpoint. 
        if f_m_i < 0:
            a_i = m_i
        else:
            b_i = m_i
            
    # Return any value in the interval. 
    return b_i


# Exercise 3



def z_squared_diff_prime(x: float, z: float) -> float:
    """Calculates the derivative, with respect to x, 
    of the function z_squared_diff, which calculates 
    the difference from the square root of z.
    
    >>> z_squared_diff_prime(3.0, 9.0)
    6.0
    >>> z_squared_diff_prime(5.0, 24.0)
    10.0
    >>> z_squared_diff_prime(2.0, 0.0)
    4.0
    """
    
    return 2*x


# Exercise 4

def sqrt_z_newton(z, x0, tol, num_iter):
    """Solves for the root of the function z_squared_diff  
    using Newton's method.
    
    >>> sqrt_z_newton(9.0, 2.0, 10**(-6), 10)
    3.0
    >>> sqrt_z_newton(25.0, 2.0, 10**(-6), 20)
    5.0
    >>> sqrt_z_newton(2.0, 3.0, 10**(-6), 10)
    1.4142135623730951
    """
    # Initialize at the starting values. 
    x_i = x0
    for i in range(num_iter):
        
        # Calculate the function value and the derivative.
        f_i = z_squared_diff(x_i, z)
        f_prime_i = z_squared_diff_prime(x_i, z)
        
        # Determine the new candidate root. 
        x_i = x_i - f_i/f_prime_i
        
        # Terminate if the root is within tolerance.
        if (abs(f_i) < tol):
            return x_i
        
        # You could also calculate f_prime_i 
        # and the new x_i here, after the if statement. 
        
    # If it reaches the end of the loop, it has
    # exceeded the maximum number of iterations.
    print("Exceeded allowed number of iterations")
    return None




# Exercise 5


def z_squared_mid(x: float, z: float) -> float:
    """Calculates the midpoint between two ratios involving 
    the square root of z.
    It has a fixed point at the square root of z that is used 
    to solve for the square root of z using the fixed point method.
    
    >>> z_squared_mid(3.0, 9.0)
    3.0
    >>> z_squared_mid(5.0, 24.0)
    4.9
    >>> z_squared_mid(2.0, 0.0)
    1.0
    """
    
    return (z/x + x)/2



# Exercise 6

def sqrt_z_fixed_pt(z, x0, tol, num_iter):
    """Solves for the root of the function z_squared_diff  
    using the fixed point method.
    
    >>> sqrt_z_fixed_pt(9.0, 2.0, 10**(-6), 10)
    3.0
    >>> sqrt_z_fixed_pt(25.0, 2.0, 10**(-6), 20)
    5.0
    >>> sqrt_z_fixed_pt(2.0, 3.0, 10**(-6), 10)
    1.4142135623730951
    """
    
    # Initialize at the starting value.
    x_i = x0
    for i in range(num_iter):
        
        # Calculate the recurrence relation. 
        f_i = z_squared_mid(x_i, z)
        
        # Terminate if it is within tolerance, 
        # otherwise, update the candidate fixed point. 
        if (abs(f_i - x_i) < tol):
            return f_i
        else:
            x_i = f_i
        
    # If it reaches the end of the loop, it has
    # exceeded the maximum number of iterations.
    print("Exceeded allowed number of iterations")
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
