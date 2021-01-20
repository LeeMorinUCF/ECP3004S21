#!/usr/bin/python
"""
##################################################
# 
# ECP 3004: Python for Business Analytics
# 
# Solving Equations with Scipy
# 
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business
# University of Central Florida
# 
# January 19, 2021
# 
# This program provides introductory examples of 
# numerical methods for finding roots of single equations
# and solving systems of equations.
# 
##################################################
"""


##################################################
# Import Modules.
##################################################


import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy import optimize
# from scipy.optimize import minimize
# from scipy.optimize import Bounds
# from scipy.optimize import LinearConstraint

################################################################################
# Solving Nonlinear equations
################################################################################

#--------------------------------------------------
# Single variable equations
#--------------------------------------------------

# Goal: Find the root of this function.
def f(x):
    out_value = math.log(x) - math.exp(-x)
    print("(x, f(x)) = (%f, %f)" % (x, out_value))
    return out_value
# That is, find the x at which this function is zero.

# Plot this function to show an approximate root.
x_grid = np.arange(0.1, 2, 0.01)
f_grid = x_grid*0
for i in range(0, len(x_grid)):
    f_grid[i] = f(x_grid[i])


plt.figure()
plt.plot(x_grid, f_grid, label='f(x)' )
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()


# Legacy solution:
soln_fs = fsolve(f, 1)
# The root:
print(soln_fs)
# The objective function:
print(f(soln_fs))


# Other legacy functions:

# soln_b1 = broyden1(f, 1)
# soln_b1 = broyden2(f, 1)
# soln_b1 = anderson(f, 1)



#--------------------------------------------------
# Multiple variable equations
#--------------------------------------------------

# 2 equations, 2 parameters.


def my_eqns_22(x):
    F1 = x[0]**2+ x[1]**2 - 1 
    F2 = x[0]**2- x[1]**2 + 0.5
    return [F1, F2]

# Test it for a few inputs (potential starting values).
my_eqns_22([1, 1])
my_eqns_22([1, 2])
x0 = [1, 1]

soln_m_22 = optimize.root(my_eqns_22, x0)



# The root:
print(soln_m_22.x)
# The objective function:
print(soln_m_22.fun)
print(my_eqns_22(soln_m_22.x))


# 3 equations, 2 parameters.


def my_eqns_32(x):
    F1 = x[0] + x[1] + x[2]**2 - 12
    F2 = x[0]**2 - x[1] + x[2] - 2
    F3 = 2 * x[0] - x[1]**2 + x[2] - 1
    return [F1, F2, F3]



# Test it for a few inputs (potential starting values).
my_eqns_32([1, 1, 1])
my_eqns_32([0, 0, 0])
x0 = [1, 1, 1]

soln_m32_1 = optimize.root(my_eqns_32, x0)


# The root:
print(soln_m32_1.x)
# The objective function:
print(soln_m32_1.fun)
print(my_eqns_32(soln_m32_1.x))


# Try the other starting value, just to compare.
x0 = [0, 0, 0]

soln_m32_2 = optimize.root(my_eqns_32, x0)

# The root:
print(soln_m32_2.x)
# The objective function:
print(soln_m32_2.fun)
print(my_eqns_32(soln_m32_2.x))


# Passing additional parameters. 

def my_eqns_33_p(x, parms):
    F1 = x[0] + x[1] + x[2]**2 - parms[0]
    F2 = x[0]**2 - x[1] + x[2] - parms[1]
    F3 = 2 * x[0] - x[1]**2 + x[2] - parms[2]
    return [F1, F2, F3]


# Set parameters and choose starting values.
parms = [12, 2, 1]
my_eqns_33_p([1, 1, 1], parms)
x0 = [1, 1, 1]


# Solve
soln_m33_p = optimize.root(my_eqns_33_p, x0, parms)

# The root:
print(soln_m33_p.x)
# The objective function:
print(soln_m33_p.fun)
print(my_eqns_33_p(soln_m33_p.x, parms))


# Try other parameters and starting value.
parms = [24, 4, 2]
x0 = [0, 0, 0]
my_eqns_33_p(x0, parms)

# Solve
soln_m33_p = optimize.root(my_eqns_33_p, x0, parms)

# The root:
print(soln_m33_p.x)
# The objective function:
print(soln_m33_p.fun)
print(my_eqns_33_p(soln_m33_p.x, parms))


# Test these values:
x0 = [-0.6406658, 1.2471383, 4.8366856]
my_eqns_33_p(x0, parms)
# Another solution. 

# Solve to higher degree of precision.
soln_m33_p = optimize.root(my_eqns_33_p, x0, parms)

# The root:
print(soln_m33_p.x)
# The objective function:
print(soln_m33_p.fun)
print(my_eqns_33_p(soln_m33_p.x, parms))


##################################################
# End
##################################################
