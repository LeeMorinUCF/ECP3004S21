# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Data Analysis with Pandas
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business
# University of Central Florida
#
# February 10, 2021
#
##################################################
"""



##################################################
# Import Modules.
##################################################

import os # To set working directory
import pandas as pd # To read and inspect data
import numpy as np # For operations on numpy arrays.


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
# Pandas.
##################################################

# You can create a series of values.

s = pd.Series([1,3,5,np.nan,6,8])
s


# You can easily manipulate dates.

dates = pd.date_range('20130101', periods=6)
dates


# You can combine the above to create data frames, much like you might read from files.

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df


# You can create a data frame, which is another type of object for organizing data.

df2 = pd.DataFrame({ 'A' : 1.,
        'B' : pd.Timestamp('20130102'),
        'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
        'D' : np.array([3] * 4,dtype='int32'),
        'E' : pd.Categorical(["test","train","test","train"]),
        'F' : 'foo' })
df2


# Take a look at the individual types of columns in the data frame.

df2.dtypes


# That is only one attribute of a data frame. There are many others.

df2.head(3)
df2.tail(3)
df.index
df.columns
df.values


# A useful function will calculate summary statistics for your data.

df.describe()


# Linear algebra operations are also a possibility, such as the transpose.

df.T


# There are many options to get subsets of the data frame.

df['A']

df[0:3]

df['20130102':'20130104']


# You can also use boolean logic to get subsets.

df[df.A > 0]

df[df > 0]

# The symbol NaN is an abbreviation for "not a number". 
# It is used as a placeholder when the value is missing. 



# There are many other functions to operate on data frames in combination with the pandas package.
# Try either of the commands below, for an arbitrary data frame with column names 'a', 'c', or 'Country' as in the following examples.  




# Drop values from columns(axis=1)
print(df2)

df2.drop('B', axis=1)

print(df2)


# Notice that the drop command only produced the requested dataset, 
# instead of permanently removing it. 


# Sort by the values along an axis

df2.sort_values(by='E')



#--------------------------------------------------
# File IO with Microsoft Excel
#--------------------------------------------------


# Pandas has more advanced tricks for file I/O (that is, Input/Output). 

# Here are some samples of code to use when the corresponding 
# files exist in your working directory. 

# One of the most common way to work with a dataset is to read and write to a csv file.


pd.read_csv('file.csv', header=None, nrows=5)
pd.to_csv('myDataFrame.csv')


# You can also read from Excel files, by selecting the worksheet. 


xlsx = pd.ExcelFile('file.xls')
df = pd.read_excel(xlsx,  'Sheet1')


# You can also write to an Excel worksheet. 


pd.read_excel('file.xlsx')
pd.to_excel('dir/myDataFrame.xlsx',  sheet_name='Sheet1')




# For examples of the use of the pandas package to prepare data
# for linear regression and estimate the model, see the sample files
# reg_with_stats_models.py and reg_with_sklearn.py above.




##################################################
# End.
##################################################
