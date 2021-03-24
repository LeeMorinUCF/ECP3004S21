# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Computing Logistic Regression Coefficients
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business Administration
# University of Central Florida
#
# March 24, 2021
#
# This script estimates logistic regression in python, 
# using several numerical methods.
# It uses a sample dataset credit_data.csv with the following variables:
#   default: 1 if borrower defaulted on a loan
#   bmaxrate: Maximum rate of interest on any part of the loan
#   amount: the amount funded on the loan
#   close: borrower takes the option of closing the listing
#     until it is fully funded
#   AA: borrowers FICO score greater than 760
#   A: borrowers FICO score between 720 and 759
#   B: borrowers FICO score between 680 and 719
#   C: borrowers FICO score between 640 and 679
#   D: borrowers FICO score between 600 and 639
#
##################################################
"""

##################################################
# Import Modules.
##################################################


import os # To set working directory
# import numpy as np # Not needed here but often useful
import pandas as pd # To read and inspect data
# from sklearn.linear_model import LogisticRegression

# import statsmodels.formula.api as smf # Another way to estimate logistic regression
import statsmodels.api as sm # Another way to estimate logistic regression

# Need exponential function in likelihood function. 
import numpy as np
# And np arrays are used in calculation. 

# Import scipy package for optimization
# from scipy import optimize
from scipy.optimize import minimize

# To plot regression results
# import matplotlib.pyplot as plt  



##################################################
# Set Working Directory.
##################################################




# Find out the current directory.
os.getcwd()
# Change to a new directory.
git_path = 'C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\'
os.chdir(git_path + 'demo_19_Classification')
# Check that the change was successful.
os.getcwd()


##################################################
# Load Data.
##################################################


credit = pd.read_csv('credit_data.csv')



##################################################
# Inspect Data.
##################################################



# Inspect the target variable.
credit['default'].value_counts()


# Look at the explanatory variables in groups.
credit[['bmaxrate','amount','close','bankcardutil']].describe()
credit[['AA','A','B','C']].describe()



##################################################
# Logistic Regression.
##################################################


#--------------------------------------------------
# Fit the Logistic Model (with statsmodels module).
#--------------------------------------------------

# Select the target variable as y.
y = credit['default']
# y = np.array(credit['default'])

# Create a matrix of explanatory variables.
# Add a column of 1s for the constant. 
credit['Intercept'] = 1
# Get names of explanatory variables (in order).
# X_cols = credit.columns[[10, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
X_cols = credit.columns[[10, 4, 5, 6, 7, 8]]
# Create matrix of explanatory variables.
X = credit[X_cols]
# X = np.array(credit[X_cols])


# Initialize and specify the logistic model.
logit_model_sm = sm.Logit(y, X)

# Fit the model.
logit_model_fit_sm = logit_model_sm.fit()

# Display the parameters.
print(logit_model_fit_sm.params)
# This is the goal: calculate these coefficients.


# Display a summary table of regression results.
print(logit_model_fit_sm.summary())
# Objective is -558.52 in regression output above:
# Log-Likelihood:                -558.52


##################################################
# The likelihood function
##################################################


#--------------------------------------------------
# Define the objective function: 
# The likelihood function
#--------------------------------------------------

def logit_likelihood(beta, y, X):
    X_beta = X.dot(beta)
    exp_X_beta = np.exp(X_beta)
    probs = exp_X_beta/(1 + exp_X_beta)
    like = sum(np.log(probs[y == 1])) + sum(np.log(1 - probs[y == 0]))
    neg_like = - like
    return neg_like



# Test this function with a value of the parameter beta.
beta = logit_model_fit_sm.params
# Goal is -558.52 in regression output above:
# Log-Likelihood:                -558.52
print(logit_likelihood(beta, y, X))
# Check. 


#--------------------------------------------------
# Define the gradient vector of the objective function: 
# The slope of the likelihood function
#--------------------------------------------------

def logit_gradient(beta, y, X):
    X_beta = X.dot(beta)
    exp_X_beta = np.exp(X_beta)
    probs = exp_X_beta/(1 + exp_X_beta)
    error = y - probs
    grad = error.dot(X)
    neg_grad = - grad
    return neg_grad



# Test this function with a value of the parameter beta.
beta = logit_model_fit_sm.params
# Goal is zero when likelihood function is optimized.
print(logit_gradient(beta, y, X))
# Check (almost zero). 



##################################################
# Optimize the Likelihood Function
# Find the beta such that the likelihood function is maximized
##################################################


#--------------------------------------------------
# Nelder-Mead Simplex algorithm
# Use the method = 'nelder-mead' algorithm. 
#--------------------------------------------------


beta_0 = np.zeros(len(logit_model_fit_sm.params))

#--------------------------------------------------
# Code goes here:
#--------------------------------------------------

soln_nm = None

#--------------------------------------------------
#--------------------------------------------------


# The parameters:
print(soln_nm.x)
# Compare with the estimates from logit_model_fit_sm:
print(logit_model_fit_sm.params)

# The objective function:
print(soln_nm.fun)
print(logit_likelihood(soln_nm.x, y, X))



#--------------------------------------------------
# Powell Method 
# AKA Davidon-Fletcher-Powell (DFP)
#--------------------------------------------------


beta_0 = np.zeros(len(logit_model_fit_sm.params))

#--------------------------------------------------
# Code goes here:
#--------------------------------------------------

soln_dfp = None
#--------------------------------------------------
#--------------------------------------------------




# The parameters:
print(soln_dfp.x)
# Compare with the estimates from logit_model_fit_sm:
print(logit_model_fit_sm.params)

# The objective function:
print(soln_dfp.fun)
print(logit_likelihood(soln_dfp.x, y, X))



#--------------------------------------------------
# Broyden-Fletcher-Goldfarb-Shanno algorithm (BFGS)
# First try by only the likelihood function
#--------------------------------------------------


beta_0 = np.zeros(len(logit_model_fit_sm.params))


#--------------------------------------------------
# Code goes here:
#--------------------------------------------------

soln_bfgs = None

#--------------------------------------------------
#--------------------------------------------------




# The parameters:
print(soln_bfgs.x)
# Compare with the estimates from logit_model_fit_sm:
print(logit_model_fit_sm.params)

# The objective function:
print(soln_bfgs.fun)
print(logit_likelihood(soln_bfgs.x, y, X))





#--------------------------------------------------
# Broyden-Fletcher-Goldfarb-Shanno algorithm (BFGS)
# Uses gradient vector, as well as function evaluations
# to reduce number of iterations.
#--------------------------------------------------


beta_0 = np.zeros(len(logit_model_fit_sm.params))

#--------------------------------------------------
# Code goes here:
#--------------------------------------------------

soln_bfgs_jac = None

#--------------------------------------------------
#--------------------------------------------------




# The parameters:
print(soln_bfgs_jac.x)
# Compare with the estimates from logit_model_fit_sm:
print(logit_model_fit_sm.params)

# The objective function:
print(soln_bfgs_jac.fun)
print(logit_likelihood(soln_bfgs_jac.x, y, X))




##################################################

##################################################

#--------------------------------------------------
# Define the Hessian matrix of the objective function: 
# The concavity of the likelihood function
#--------------------------------------------------

def logit_hessian(beta, y, X):
    X_beta = X.dot(beta)
    exp_X_beta = np.exp(X_beta)
    probs = exp_X_beta/(1 + exp_X_beta)
    error = y - probs
    diag = probs*error
    # grad = error.dot(X)
    
    # X_diag = X*np.repeat(diag, len(X.columns), 1)
    # Don't multiply with a diagonal matrix.
    # Create a matrix with repeating rows. 
    rep_diag = pd.concat([diag] * len(X.columns), 
                         axis = 1, ignore_index = True)
    rep_diag.columns = X.columns
    X_diag = X.multiply(rep_diag)
    
    # The definition of the Hessian for the logistic regression.
    # X^T * D * X, 
    # where D is a diagonal matrix with values diag on the diagonal.
    hess = X_diag.transpose().dot(X)
    
    neg_hess = - hess
    return neg_hess



#--------------------------------------------------
# Code goes here:
#--------------------------------------------------


soln_ncg_hess = None

#--------------------------------------------------
#--------------------------------------------------





# The parameters:
print(soln_ncg_hess.x)
# Compare with the estimates from logit_model_fit_sm:
print(logit_model_fit_sm.params)

# The objective function:
print(soln_ncg_hess.fun)
print(logit_likelihood(soln_bfgs_jac.x, y, X))




##################################################
# End
##################################################

