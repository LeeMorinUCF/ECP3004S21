# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Linear Regression with the sklearn Module
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business
# University of Central Florida
#
# January 20, 2021
#
# This script outlies one approach to linear regression in python.
# It uses a sample dataset housing_data.csv with the following variables:
#     obsn_num an integer label for each observation
#     house_price (property values, in millions)
#     income (in millions)
#     in_cali (whether the property is in California)
#     earthquake (whether an earthquake had occurred)
# This example uses the scikitlearn (sklearn) module for estimation.
#
##################################################
"""



##################################################
# Import Modules.
##################################################


import os # To set working directory
import pandas as pd # To read and inspect data
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt  # To plot regression results
from sklearn.metrics import mean_squared_error, r2_score # For model performance




##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\demo_09_Modules_for_Regression')
# Check that the change was successful.
os.getcwd()




##################################################
# Load Data.
##################################################


housing = pd.read_csv('housing_data.csv')



##################################################
# Inspect Data.
##################################################


# What did we just read?
type(housing)

# Take a look at the individual types of columns in the data frame.
housing.dtypes


# Inspect a few rows of data.
housing.head(3)
housing.tail(3)

# Check the dimensions of the data.
housing.index
housing.columns


# Calculate summary statistics for your data.
housing.describe()


# Drop the observation numbers.
housing = housing.drop('obsn_num', axis = 1)


# Display the correlation matrix.
housing.corr()



##################################################
# Simple Regression.
##################################################


# Define the target and predictor variables.
Y = housing[['house_price']]
X_1 = housing[['income']]


Y.describe()
X_1.describe()


#--------------------------------------------------
# Fit the Regression Model.
#--------------------------------------------------

# Initialize the regression model object.
reg_model_1 = LinearRegression()

# Fit the linear regression model.
reg_model_1.fit(X_1, Y)

# Obtain predictions.
Y_pred_1 = reg_model_1.predict(X_1)



#--------------------------------------------------
# Plot the results.
#--------------------------------------------------

# Plot the regression line with the data.
plt.scatter(X_1, Y)
plt.plot(X_1, Y_pred_1, color = 'red')
plt.xlabel('Income')
plt.ylabel('House Price')
plt.title('Regression of House Price on Income')
plt.show()

# You can save the figure to place within a document.
# plt.savefig('Reg_Example_1.pdf')


# Plot the target variable with the predictions.
plt.scatter(Y_pred_1, Y)
# Doesn't look very good.

# Let's look at some summary statistics.


#--------------------------------------------------
# Summary statistics
#--------------------------------------------------

# The intercept
print('Intercept: %f \n' % reg_model_1.intercept_)

# The slope coefficient
print('Coefficients: %f \n' % reg_model_1.coef_)

# Coefficient of determination (R-squared)
r_sq = reg_model_1.score(X_1, Y)
print('Coefficient of determination:', r_sq)


# Other statistics using the sklearn.metrics module.


# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(Y, Y_pred_1))

# R-squared
print('R-squared: %.2f' % r2_score(Y, Y_pred_1))


##################################################
# Multiple Regression.
##################################################



# Select the full set of predictor variables.

housing.columns[1:4]

X = housing[housing.columns[1:4]]

X.describe()


#--------------------------------------------------
# Fit the Regression Model.
#--------------------------------------------------

# Initialize the regression model object.
reg_model_full = LinearRegression()

# Fit the linear regression model.
reg_model_full.fit(X, Y)

# Obtain predictions.
Y_pred_full = reg_model_full.predict(X)



#--------------------------------------------------
# Summary statistics
#--------------------------------------------------

# The intercept
print('Intercept: %f \n' % reg_model_full.intercept_)

# The slope coefficient
for i in range(len(reg_model_full.coef_[0])):
    print('\nCoefficients %d: %f \n' % (i, reg_model_full.coef_[0][i]))


# Coefficient of determination (R-squared)
r_sq = reg_model_full.score(X, Y)
print('Coefficient of determination:', r_sq)


# This is a minimalist version of linear regression.
# It avoids unnecessary computation if, for example, 
# you were running many models in a loop. 
# Also, sklearn can estimate many more types of models, 
# and it is often used for machine learning. 

# If you prefer more statistics printed out automatically, 
# then use the statsmodels module.


##################################################
# End
##################################################
