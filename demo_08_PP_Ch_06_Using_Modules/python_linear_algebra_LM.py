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

# Module os to interact with the operating system, 
# e.g. set the working directory. 
import os

# Module numpy for numerical methods in Python, 
# e.g. to use linear algebra.
import numpy as np

# Module scipy for scientific computing in Python, 
# such as linear algebra, in this example, 
# but also optimization and solving nonlinear equations.
from scipy import linalg

# Module matplotlib to plot figures. 
import matplotlib.pyplot as plt


##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
# os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\demo_08_PP_Ch_06_Using_Modules')
os.chdir('C:\\Users\\le279259\\OneDrive - University of Central Florida\\Documents\\GitHub\\ECP3004S21\\demo_08_PP_Ch_06_Using_Modules')
# Check that the change was successful.
os.getcwd()



##################################################
# Examples Using Numpy.
##################################################

# Some languages are designed for matrix algebra. 
# For example, when you use the statistical programming language ```R```,
# the matrix multiplication operator is the symbol ```%*%```. 

# Python operates vectors and matrices differently. 
# It thinks of them as parameters in a function, 
# such as the dot function in the numpy module. 

# Assign numbers to two numpy arrays.
A = np.array([[1., 2., 3.], [4., 5., 6.]])
x = np.array([[10., 11.], [20., 21.], [30., 31.]])

# Multiply these matrices together. 
b = A.dot(x)
print(b)

# These numpy arrays have their own type. 
type(A)

type(x)

type(b)


# To extract values from the array, you can extract elements
# just as you would for a list.

A[1]

A[1][2]

# Since these numpy arrays are 2-dimensional objects,
# you can also extract the elements by passing a 
# list of index numbers. 
A[1, 2]

# Now that we know how to perform matrix multiplication, 
# we can use it to solve for the unknown vector or matrix 
# x that produced the product b.


#--------------------------------------------------
# Solve a linear system with the inverse matrix
#--------------------------------------------------

# The conceptually simple--but computationally expensive--approach 
# is to calculate the inverse of the matrix ```A``` 
# and then multiply ```b``` to achieve the solution ```b```. 


# Assign numbers to two numpy arrays.
A = np.array([[1., 2.], [3., 4.]])
b = np.array([1., 1.])


# Use the np.linalg.inv method to find the inverse.
A_inv = np.linalg.inv(A)
A_inv

# Verify that A_inv is the inverse of A.
A.dot(A_inv)

A_inv.dot(A)

# Since both of these products equal the identity matrix, 
# A_inv is the inverse of A. 

# Notice that the off-diagonal elements are not exactly zero.
# Rounding errors occur when using numbers with finite precision. 

x_soln = A_inv.dot(b)
print(x_soln)

# Verify the solution:
A.dot(x_soln)
# which is the same as b.


#--------------------------------------------------
# Solve a linear system without the inverse
#--------------------------------------------------



# Use the solve method to find a solution x to the system
# of the form A*x = b
soln = np.linalg.solve(A, b)
soln

# Check the solution
A.dot(soln)
# equals b, so it's the solution. 




#--------------------------------------------------
# Functions for creating arrays 
#--------------------------------------------------

# There are a number of convenient functions 
# for generating matrices of a specific form. 

# Create an array of zeros.
a = np.zeros((2,2))   
print(a)

# Create an array of ones.
b = np.ones((1,2))
print(b)

# Create a constant array. 
c = np.full((2,2), 7)
print(c)

# Create a 2x2 identity matrix. 
d = np.eye(2)
print(d)

# Create an array filled with random values.
e = np.random.random((2,2))
print(e)

# These are often useful for solving algebra problems, 
# since the syntax matches the symbols often used 
# on the blackboard.



#--------------------------------------------------
# Writing an array to a file. 
#--------------------------------------------------

# Produce an array from the range function. 
x_out = (np.array(range(7)) + 1)*0.1
# Produce an array full of constants. 
y_out = np.full(7, 0.1)
# Produce an array that is a function of other arrays. 
z_out = np.sqrt(x_out*x_out + y_out*y_out)
# Notice that multiplication and sqrt are calculated
# element-by-element. 

# Now bind these together into a 2-D array. 
dataOut = np.column_stack((x_out, y_out, z_out))

# You can save the array into a csv file. 
np.savetxt('PythagExample.dat', dataOut, 
           fmt = ('%10.4f %10.4f %10.4f'), header = 'x, y, z')
# This is a small dataset but it is complete with
# column labels (headers) and formatted numbers (fmt). 


#--------------------------------------------------
# Reading an array from a file. 
#--------------------------------------------------


# Load the matrix from a file. 
x, y, z = np.loadtxt('PythagExample.dat', unpack = True)
# Note that all three are assigned at the same time, 
# since the array is unpacked into the separate vectors. 

# Repeat the calculation of z to verify accuracy. 
d = np.sqrt(x*x + y*y)
# Append d to the original column z.
dataOut = np.column_stack((d, z))
# As above, save this to another csv file. 
np.savetxt('PythagOutput.dat', dataOut, 
           fmt = ('%15.10f %10.4f'), header = 'd, z\n')



##################################################
# Examples Using Scipy.
##################################################


# We still need to import numpy to create arrays. 
# We also import the linalg module from scipy 
# to use tools for linear algebra. 

# Create an array for a 3x3 matrix. 
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
A



# Calculate the inverse A^{-1}.
# Roughly speaking, the inverse is defined as follows:
# A^{-1} satisfies A^{-1}*A = A*A^{-1} = I, the identity matrix.
# If x solves A*x = b, then A^{-1}*b = x. 
linalg.inv(A)


# Verify that A^{-1} is, in fact, the identity matrix. 
A.dot(linalg.inv(A)) 
# Note that the off-diagonals are very small numbers
# but not quite zero.
# Recall that computers store numbers up to finite precision.
# There are rounding errors. 



# Solve the above problem (in the numpy example) with the inverse.
A = np.array([[1., 2.], [3., 4.]])
b = np.array([1., 1.])

# Calculate the inverse matrix A^{-1}.
A_inv = linalg.inv(A)

# Multiply the vector b by the inverse A^{-1}.
# This also obtains a solution x to the system
# of the form A*x = b, since A^{-1}*b = x.
soln = A_inv.dot(b)
print(soln)

# Check the solution. 
A.dot(soln)
# Again, it equals b, so it's the solution. 




#--------------------------------------------------
# Solve the parameters in a nonlinear model.
#--------------------------------------------------

# This example uses the following modules, imported above.
# import numpy as np
# from scipy import linalg
# import matplotlib.pyplot as plt

# Generate an artificial dataset. 

# Set parameters. 
beta_0, beta_1 = 5.0, 2.0
# Create a row vector from the range 1 to 10. 
i = np.r_[1:11] # Same as np.array(range(1, 11)).
# Generate the explanatory variable, x. 
xi = 0.1*i

# Generate the dependent variable, y, with a nonlinear model.
yi_true = beta_0*np.exp(-xi) + beta_1*xi
# Add an error term for some random variation. 
yi = yi_true + 0.25 * np.random.randn(len(yi_true))


# Arrange into matrix form. 
A = np.c_[np.exp(-xi)[:, np.newaxis], xi[:, np.newaxis]]
# The newaxis argument increases the dimension of the array by one dimension
# Useful for creating objects one dimension higher. 
# This is used because we are binding column vectors together into
# a matrix. 

# Solve the system by least squares. 
beta_hat, resid, rank, sigma = linalg.lstsq(A, yi)

# Calculate the fitted values on a grid of values. 
xi_grid = np.r_[0.1:1.0:100j]
yi_hat = beta_hat[0]*np.exp(-xi_grid) + beta_hat[1]*xi_grid

# Plot the data and the fitted model
plt.plot(xi,yi,'x',xi_grid,yi_hat)
plt.axis([0,1.1,3.0,5.5])
plt.xlabel('$x_i$')
plt.title('Estimating a Nonlinear Model with linalg.lstsq')
plt.show()

# See the figure in the "Plots" tab in the 
# upper right window of Anaconda.



##################################################
# End.
##################################################
