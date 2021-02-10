# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Linear Regression with the statsmodels Module
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
# This example uses the statsmodels module for estimation.
#
##################################################
"""



##################################################
# Import Modules.
##################################################


import os # To set working directory
import pandas as pd # To read and inspect data
import statsmodels.formula.api as sm # Another way to estimate linear regression




##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\demo_09_Modules_for_Regression')
# os.chdir('C:\Users\le279259\Documents\Teaching\QMB6358_Fall_2020\GitRepos\QMB6358F20\demo_12_linear_models_in_python')
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


#--------------------------------------------------
# Fit the Regression Model.
#--------------------------------------------------

# Fit the regression model.
reg_model_full_sm = sm.ols(formula = "house_price ~ income + in_cali + earthquake", data = housing).fit()

# Display the parameters.
print(reg_model_full_sm.params)


# Display a summary table of regression results.
print(reg_model_full_sm.summary())



# Compare with a bivariate model.
reg_model_1_sm = sm.ols(formula = "house_price ~ income", data = housing).fit()
print(reg_model_1_sm.summary())




##################################################
# End
##################################################
