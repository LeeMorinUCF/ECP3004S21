# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Data Analysis with Pandas: Logistic Regression
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business Administration
# University of Central Florida
#
# March 21, 2021
#
# This script outlies a few approaches to logistic regression in python.
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

# from __future__ import division
# (Needed if you are using Python 2 - which you should NOT be doing!)

##################################################
# Import Modules.
##################################################


import os # To set working directory
# import numpy as np # Not needed here but often useful
import pandas as pd # To read and inspect data
from sklearn.linear_model import LogisticRegression

import statsmodels.formula.api as smf # Another way to estimate logistic regression
import statsmodels.api as sm # Another way to estimate logistic regression

import matplotlib.pyplot as plt  # To plot regression results
import seaborn as sns # Another package for plotting data
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)


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


# Take a look at the individual types of columns in the data frame.
credit.dtypes


# Inspect a few rows of data.
credit.head(3)
credit.tail(3)

# Check the dimensions of the data.
credit.index
credit.columns


# Calculate summary statistics for your data.
credit.describe()

# Look at a few variables at a time.
credit[['bmaxrate','amount','close','bankcardutil']].describe()
credit[['AA','A','B','C']].describe()

# Drop the observation numbers, if you like.
# housing = housing.drop('obsn_num', axis = 1)


# Display the correlation matrix.
credit.corr()
# Look at a few variables at a time.
credit[['default','bmaxrate','amount','close','bankcardutil']].corr()
credit[['default','AA','A','B','C']].corr()

# Inspect the target variable.
credit['default'].value_counts()

# Plot a bar chart.
sns.countplot(x = 'default', data = credit, palette = 'hls')


# Verify that data differs by default status.
credit.groupby('default').mean()

# Look at a few variables at a time.
credit[['default','bmaxrate','amount','close','bankcardutil']].groupby('default').mean()
credit[['default','AA','A','B','C']].groupby('default').mean()

# As a rule, if the distribution of the explanatory variables differ 
# between the Y = 1 and Y = 0 observations, 
# then there is the potential that you can use the explanatory variables 
# to predict the probability that Y = 1.


##################################################
# Logistic Regression.
##################################################


#--------------------------------------------------
# Fit the Logistic Model (with statsmodels module).
#--------------------------------------------------

# This is a module designed in the format that would
# commonly be used by statusticians (and in econometrics class). 


# Get names of explanatory variables
X_cols = credit.columns[1:]

# Initialize and specify the logistic model.
logit_model_sm = sm.Logit(credit['default'], credit[X_cols])

# Fit the model.
logit_model_fit_sm = logit_model_sm.fit()

# Display the parameters.
print(logit_model_fit_sm.params)



# Display a summary table of regression results.
print(logit_model_fit_sm.summary())



#--------------------------------------------------
# Fit the Logistic Model (with sklearn module).
#--------------------------------------------------

# This is a module that might be used for other 
# machine learning models. 
# It's a little less user-friendly but more powerful. 

# Split the data into target and predictor variables.

X = credit.loc[:, credit.columns != 'default']
y = credit.loc[:, credit.columns == 'default']

# Normally would have saved some data for testing but can calculate ROC in sample.



# Initialize the regression model object.
logit_model_fit_sk = LogisticRegression()

# Fit the logistic regression model.
logit_model_fit_sk.fit(X, y.values.flatten())
# Note that it will complain if you just pass 
# the column vector y. 

# Obtain predictions.
pred_probs = logit_model_fit_sk.predict_proba(X)

# Summary statistics of predictions
pred_probs.min()

pred_probs.mean()

pred_probs.max()



#--------------------------------------------------
# Evaluating the Logistic Model.
#--------------------------------------------------

# Plotting an ROC Curve


# Calculate the values required for an ROC curve.
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
# logit_roc_auc = roc_auc_score(y, logit_model_fit_sk.predict(X))
logit_roc_auc = roc_auc_score(y, logit_model_fit_sk.predict_proba(X)[:,1])
fpr, tpr, thresholds = roc_curve(y, logit_model_fit_sk.predict_proba(X)[:,1])

# Plot the ROC curve.
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.savefig('Logit_ROC.pdf')
plt.show()



##################################################
# End
##################################################
