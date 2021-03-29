# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Data Analysis with Pandas: Nonparametric Methods
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business Administration
# University of Central Florida
#
# March 27, 2021
# 
# python_nonparametrics gives examples of "regression" models
#   by considering a number of different model specifications.
# In this example, many of the model specification choices
#   have a nonparametric form and are compared to parametric models.
# It uses a sample dataset tractor_sales.csv with the following variables:
#   saleprice is the sale price of a tractor in dollars
#   horsepower is the horsepower rating of the engine
#   age is the age of the tractor in years
#   enghours is the number of hours the engine has been run
#   diesel is an indicator that the engine runs on diesel fuel
#   fwd indicates that the tractor has four-wheel-drive
#   manual indicates that the tractor has a manual transmission
#   johndeere indicates that the brand of the tractor is John Deere
#   cab indicates that the tractor has an enclosed cab
#   spring indicates that the tractor was sold in the spring
#   summer indicates that the tractor was sold in the summer
#   winter indicates that the tractor was sold in the winter
#
##################################################
"""


##################################################
# Import Modules.
##################################################


import os # To set working directory
import numpy as np # For log transformation
# import math
import pandas as pd # To read and inspect data

import statsmodels.formula.api as sm # to estimate linear regression
# import statsmodels.formula.api as smf # Another way to estimate regression
# import statsmodels.api as sm # Another way to estimate regression

import statsmodels.nonparametric.kernel_regression as npreg
# FOr nonparametric kernel regression

import matplotlib.pyplot as plt  # To plot regression results
# import seaborn as sns # Another package for plotting data
# sns.set(style="white")
# sns.set(style="whitegrid", color_codes=True)


##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
git_path = 'C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\'
os.chdir(git_path + 'demo_21_nonparametrics')
# Check that the change was successful.
os.getcwd()



##################################################
# Load Data.
##################################################


tractors = pd.read_csv('tractor_sales.csv')



##################################################
# Inspect Data.
##################################################


# Take a look at the individual types of columns in the data frame.
tractors.dtypes


# Inspect a few rows of data.
tractors.head(3)
tractors.tail(3)

# Check the dimensions of the data.
tractors.index
tractors.columns


# Calculate summary statistics for your data.
tractors.describe()

# Look at a few variables at a time.
tractors[['saleprice','horsepower','age','enghours']].describe()

tractors[['manual','johndeere','cab',
          'spring', 'summer', 'winter']].describe()


# Display the correlation matrix.
# tractors.corr()
# Look at a few variables at a time.

# Continuous variables:
tractors[['saleprice','horsepower','age','enghours']].corr()

# Tractor characteristics:
tractors[['saleprice','manual','johndeere','cab']].corr()

# Timing of sale:
tractors[['saleprice','spring', 'summer', 'winter']].corr()


# Inspect the target variable.
tractors['saleprice'].value_counts()



#--------------------------------------------------
# Visualizing the dependent variable
# with histograms
#--------------------------------------------------


# Plot a histogram (default width of bins).
n, bins, patches = plt.hist(x = tractors['saleprice'], 
                            bins = 'auto', 
                            color = '#0504aa',
                            alpha = 0.7, rwidth = 0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.title('Histogram of Tractor Sales Prices')
plt.show()


# You might not know it but you have just conducted
# nonparametric estimation. 

# Now, let's see if we can fine-tune this picture.


# We can choose the number of bins to determine
# the smoothness the distribution. 
n, bins, patches = plt.hist(x = tractors['saleprice'], 
                            bins = 10, 
                            color = '#0504aa',
                            alpha = 0.7, rwidth = 0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.title('Histogram of Tractor Sales Prices')
plt.show()

# With 10 bins it appears to have a smoothly declining density.



# Try it again with many bins.

n, bins, patches = plt.hist(x = tractors['saleprice'], 
                            bins = 100, 
                            color = '#0504aa',
                            alpha = 0.7, rwidth = 0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.title('Histogram of Tractor Sales Prices')
plt.show()

# Now it looks very choppy with too many 
# gaps between the populated bins. 
# The picture is too jagged. 

# At this point, you should appreciate the default values, 
# although sometimes you will want to do some fine-tuning 
# to investigate the data. 

#--------------------------------------------------
# Kernel density somoothing
#--------------------------------------------------

# Another way to visualize the density is by
# *kernel density smooting*, which is so called 
# not because *we* intend to plot a density
# but because *the method* uses a density to 
# calculate the plot. 

# It takes a weighted average, using a density 
# called a *kernel* at each point on the plot. 

dist = tractors['saleprice']

fig, ax = plt.subplots()
dist.plot.kde(ax = ax, legend = False, 
              title = 'Density of Tractor Sales Prices')
dist.plot.hist(density = True, ax = ax)
ax.set_ylabel('Probability')
ax.grid(axis = 'y')
ax.set_facecolor('#d8dcd6')



# The kernel-smoothed density is essentially a
# weighted average of the neigboring points, taken at
# each value along the horizontal axis. 


# Similar to histograms, you can adjust the *bandwidth*
# parameter to adjust the smoothness of the density.


# The bandwidth determines the distance from each location
# on the density that the weighted average weights heavily. 


# With a large bandwidth you get a smoother density. 


fig, ax = plt.subplots()
dist.plot.kde(ax = ax, legend = False, 
              title = 'Density of Tractor Sales Prices', 
              bw_method = 1)
dist.plot.hist(density = True, ax = ax)
ax.set_ylabel('Probability')
ax.grid(axis = 'y')
ax.set_facecolor('#d8dcd6')



# Notice, however, that the density bleeds into negative territory, 
# which is not posible with sales. 
# (No one pays for you to take their tractor.)

# This density does not look very much like the histogram. 

# Try it again with a smaller bandwidth.

fig, ax = plt.subplots()
dist.plot.kde(ax = ax, legend = False, 
              title = 'Density of Tractor Sales Prices', 
              bw_method = 0.1)
dist.plot.hist(density = True, ax = ax)
ax.set_ylabel('Probability')
ax.grid(axis = 'y')
ax.set_facecolor('#d8dcd6')

# This is better but now the density is very jagged.
# There are peaks on the prices that happened to occur
# and valleys on the prices where sales did not occur.



#--------------------------------------------------
# Logarithmic transformation
#--------------------------------------------------

# When regression modelling, the model fit is often more
# accurate when the variable is nearly nrmally distributed.

# Let's consider the log tractor price as the dependent variable.

tractors['log_saleprice'] = np.log(tractors['saleprice'])

# Now let's plot a histogram of the log sales prices.

# With some trial-and-error, I chose 20 bins.
n, bins, patches = plt.hist(x = tractors['log_saleprice'], 
                            bins = 20, 
                            color = '#0504aa',
                            alpha = 0.7, rwidth = 0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.title('Histogram of Log of Tractor Sales Prices')
plt.show()

# This histogram looks almost symmetric.
# It is much close to the normal distribution.

# Now let's plot a density. 

dist_log = tractors['log_saleprice']

fig, ax = plt.subplots()
dist_log.plot.kde(ax = ax, legend = False, 
              title = 'Density of Log of Tractor Sales Prices', 
              bw_method = 0.5)
dist_log.plot.hist(density = True, ax = ax)
ax.set_ylabel('Probability')
ax.grid(axis = 'y')
ax.set_facecolor('#d8dcd6')

# This looks very smooth but also plausible. 
# We should build a model to predict the
# log of the tractor prices.

# Note that when we do this, the coefficients no longer
# have the same interpretation:
# With this specification, the change in the explanatory
# variables (the characteristics of the tractors)
# indicates a proportional change in the
# dependent variable (the prices of the tractors). 



##################################################
# Linear Regression.
##################################################

# In an econometrics course, you might fit a 
# linear regression model such as this one.

#--------------------------------------------------
# Fit a Linear Regression Model (with statsmodels module).
#--------------------------------------------------

# This is a module designed in the format that would
# commonly be used by statusticians (and in econometrics class). 



# Initialize and specify the logistic model.

sm_fmla = "log_saleprice ~ \
    horsepower + \
    age + enghours + \
    diesel + fwd + manual + johndeere + cab + \
    spring + summer + winter"

reg_model_sm = sm.ols(formula = sm_fmla, 
                      data = tractors)


# Fit the model.
reg_model_fit_sm = reg_model_sm.fit()

# Display a summary table of regression results.
print(reg_model_fit_sm.summary())

# You can see statistically significant relationships
# with these variables.
# Notice the positive relationship between prices
# and horsepower. 
# We will investigate this relationship further. 

#--------------------------------------------------
# Fit a model with quadratic form for horsepower.
#--------------------------------------------------


# Consider a polynomial functional form for horsepower.
# Idea: Horsepower improves performance up to a limit,
# then extra power does not add value, only consumes more fuel, 
# so buyers don't want to pay as much for tractors with
# higher fuel costs.

# Create a variable squared_horsepower
# to investigate quadratic relationship of sale price to horsepower.
tractors['squared_horsepower'] = tractors['horsepower']**2

# Now fit a regression model with this extra variable.
sm_fmla = "log_saleprice ~ \
    horsepower + squared_horsepower + \
    age + enghours + \
    diesel + fwd + manual + johndeere + cab + \
    spring + summer + winter"

reg_model_sm = sm.ols(formula = sm_fmla, 
                      data = tractors)


# Fit the model.
reg_model_fit_sm = reg_model_sm.fit()

# Display a summary table of regression results.
print(reg_model_fit_sm.summary())



##################################################
# Nonparametric estimation
##################################################

# Now consider that the quadratic model may not be quite right. 
# Maybe it is some other nonlinear function. 

# A nonparametric approach can estimate the relationship
# flexibly to determine what functional form should be used. 

# For kernel regression, we will pass the prices and horsepower
# as separate arrays. 

y = tractors['log_saleprice']
X = tractors['horsepower']

# Initialize the model object.
kde_reg = npreg.KernelReg(endog = y, exog = X, var_type = 'c')

# Fit the predictions to a grid of values. 
X_grid = np.arange(0, 500, 10)
kde_pred = kde_reg.fit(data_predict = X_grid)


# Plot the fitted curve with a scattergraph of the data. 
fig, ax = plt.subplots()
ax.plot(tractors['horsepower'], tractors['log_saleprice'], 
        '.', alpha = 0.5)
ax.plot(X_grid, kde_pred[0], '-', color='tab:blue', alpha = 0.9)
plt.show()


#--------------------------------------------------
# Tuning the bandwidth
#--------------------------------------------------

# In the above example, an algorithm determines 
# the size of the bandwidth. 
# You can also specify it as an array
# the same length as the number of variables
# (but we only used one variable: horsepower). 


# Initialize the model object.
kde_reg = npreg.KernelReg(endog = y, exog = X, var_type = 'c', 
                          bw = np.array([10]))

# Fit the predictions to a grid of values. 
X_grid = np.arange(0, 500, 10)
kde_pred = kde_reg.fit(data_predict = X_grid)


# Plot the fitted curve with a scattergraph of the data. 
fig, ax = plt.subplots()
ax.plot(tractors['horsepower'], tractors['log_saleprice'], 
        '.', alpha = 0.5)
ax.plot(X_grid, kde_pred[0], '-', color='tab:blue', alpha = 0.9)
plt.show()

# You can see it is more variable and, 
# similarly, could be made smoother. 


##################################################
# Semiparametric estimation
##################################################

# Now, let's fit this curve in a linear regression model. 

# Initialize the model object.
kde_reg = npreg.KernelReg(endog = y, exog = X, var_type = 'c')

# Fit the predictions to a grid of values. 
# X_grid = np.arange(0, 500, 10)
kde_pred = kde_reg.fit() # default fits to observations in dataset.

# Create a variable with this predicted curve.
tractors['horsepower_np'] = kde_pred[0]

# Now fit a regression model with this extra variable.
sm_fmla = "log_saleprice ~ \
    horsepower_np + \
    age + enghours + \
    diesel + fwd + manual + johndeere + cab + \
    spring + summer + winter"

reg_model_sm = sm.ols(formula = sm_fmla, 
                      data = tractors)


# Fit the model.
reg_model_fit_sm = reg_model_sm.fit()

# Display a summary table of regression results.
print(reg_model_fit_sm.summary())

# The fit is an improvement but the quadratic form
# for horsepower was fairly good. 


##################################################
# End
##################################################
