# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Linear Algebra in Python
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
"""



##################################################
# Import Modules.
##################################################

import os

import numpy as np

from scipy import linalg

import matplotlib.pyplot as plt


##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\demo_08_PP_Ch_06_Using_Modules')
# Check that the change was successful.
os.getcwd()



##################################################
# Examples Using Numpy.
##################################################



A = np.array([[1., 2.], [3., 4.]])
b = np.array([1., 1.])
soln = np.linalg.solve(A, b)
soln

# Check the solution
A.dot(soln)
# equals b, so it's the solution. 




# Create some data to output.
x_out = (np.array(range(7)) + 1)*0.1
y_out = np.full(7, 0.1)
z_out = np.sqrt(x_out*x_out + y_out*y_out)
dataOut = np.column_stack((x_out, y_out, z_out))
np.savetxt('PythagExample.dat', dataOut, fmt = ('%10.4f %10.4f %10.4f'), header = 'x, y, z')



# Load the matrix from a file. 
x, y, z = np.loadtxt('PythagExample.dat', unpack = True)
d = np.sqrt(x*x + y*y)
dataOut = np.column_stack((d, z))
np.savetxt('PythagOutput.dat', dataOut, fmt = ('%15.10f %10.4f'), header = 'd, z\n')


# There are a number of convenient functions 
# for generating matrices of a specific form. 

a = np.zeros((2,2))   # Create an array of all zeros
print(a)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"

b = np.ones((1,2))    # Create an array of all ones
print(b)              # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7)  # Create a constant array
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)         # Create a 2x2 identity matrix
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

e = np.random.random((2,2))  # Create an array filled with random values
print(e)                     # Might

# These are often useful for solving algebra problems, 
# since they match the symbols often used on the blackboard. .


##################################################
# Examples Using Scipy.
##################################################


# import numpy as np
# from scipy import linalg
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
A

# Calculate the inverse.
linalg.inv(A)

A.dot(linalg.inv(A)) #double check
# Note that the off-diagonals are very small numbers.


# Solve the above problem with the inverse.
A = np.array([[1., 2.], [3., 4.]])
b = np.array([1., 1.])

A_inv = linalg.inv(A)

soln = A_inv.dot(b)

soln




#--------------------------------------------------
# Solve the parameters in a nonlinear model.
#--------------------------------------------------

# This example uses the following modules, imported above.
# import numpy as np
# from scipy import linalg
# import matplotlib.pyplot as plt

# Set parameters and generate data
c1, c2 = 5.0, 2.0
i = np.r_[1:11]
xi = 0.1*i
yi = c1*np.exp(-xi) + c2*xi
zi = yi + 0.05 * np.max(yi) * np.random.randn(len(yi))

# Arrange into matrix form
A = np.c_[np.exp(-xi)[:, np.newaxis], xi[:, np.newaxis]]
# The newaxis argument increases the dimension of the array by one dimension
# Useful for creating objects one dimension higher

# Solve the system by least squares
c, resid, rank, sigma = linalg.lstsq(A, zi)

# Calculate the fitted values
xi2 = np.r_[0.1:1.0:100j]
yi2 = c[0]*np.exp(-xi2) + c[1]*xi2

# Plot the data and the fitted model
plt.plot(xi,zi,'x',xi2,yi2)
plt.axis([0,1.1,3.0,5.5])
plt.xlabel('$x_i$')
plt.title('Data fitting with linalg.lstsq')
plt.show()





##################################################
# End.
##################################################
