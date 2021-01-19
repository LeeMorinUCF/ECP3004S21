# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6358: Software Tools for Business Analytics
#
# Data Analysis with Pandas: Linear Regression
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business Administration
# University of Central Florida
#
# October 15, 2020
#
# This script outlies a few approaches to linear regression in python.
# It uses a sample dataset housing_data.csv with the following variables:
#     obsn_num an integer label for each observation
#     house_price (property values, in millions)
#     income (in millions)
#     in_cali (whether the property is in California)
#     earthquake (whether an earthquake had occurred)
#
##################################################
"""



##################################################
# Import Modules.
##################################################


import os # To set working directory
# import numpy as np # Not needed here but often useful
import pandas as pd # To read and inspect data
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt  # To plot regression results
from sklearn.metrics import mean_squared_error, r2_score # For model performance
import statsmodels.formula.api as sm # Another way to estimate linear regression




##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\QMB6358_Fall_2020\\GitRepos\\QMB6358F20\\demo_12_linear_models_in_python')
# os.chdir('C:\Users\le279259\Documents\Teaching\QMB6358_Fall_2020\GitRepos\QMB6358F20\demo_12_linear_models_in_python')
# Check that the change was successful.
os.getcwd()



##################################################
# Digression about slashes in strings
##################################################

# Much of file IO is about handling strings.
# When you read and write to the computer, 
# you read and write character strings
# to and from the files.


# What's going on with the slashes and double slashes?
# A slash is a special character
"C:/Users/le279259/Documents/Teaching/QMB6358_Fall_2020/GitRepos/QMB6358F20"


# A slash can also replicate other buttons on your keyboard.
# for example '\t' prints a tab.
print("This\tis\ta\ttab")
# '\n' creates a new line, like the return button:
print("These\nare\nseparate\nlines")


# You have to be careful about what you put in a string.
# For quotes inside quotes, single quotes can appear in double quotes.
"This won't throw an error"

# If you used single quotes on the outside, you would need
# to use the slash to tell python that you actually 
# want to print an apostrophe, instead of endint the 
# string after 'This isn'.
'This won\'t throw an error'
# but
# 'This won't run without error'

# The same goes if you want to print a double quote
# inside a string:
"This is a \"string\" inside a string"

# These tricks will be useful for the section on File IO.



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
# plt.show()
plt.savefig('Reg_Example_1.pdf')


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
# print('Coefficients: %f \n' % reg_model_full.coef_)

# Coefficient of determination (R-squared)
# r_sq = reg_model_full.score(X_1, Y)
# print('Coefficient of determination:', r_sq)




#--------------------------------------------------
# Fit the Regression Model (with statsmodels module instead).
#--------------------------------------------------

# Fit the regression model.
reg_model_full_sm = sm.ols(formula = "house_price ~ income + in_cali + earthquake", data = housing).fit()

# Display the parameters.
print(reg_model_full_sm.params)


# Display a summary table of regression results.
print(reg_model_full_sm.summary())



# Compare with univariate approach above.
reg_model_1_sm = sm.ols(formula = "house_price ~ income", data = housing).fit()
print(reg_model_1_sm.summary())


# Calculate sum of squared residuals. 
print(sum(reg_model_full_sm.resid**2))


##################################################
# End
##################################################
