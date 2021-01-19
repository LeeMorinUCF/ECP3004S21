# Data Analysis with Python

## Before anything else, set the working directory.
```python
import os
# Find out the current directory.
os.getcwd()
# Change to a new directory.
os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\ECO5445_Fall2019\\GitRepos\\Original\\demo_10_python_num')
# Check that the change was successful.
os.getcwd()
```

## The ```pandas``` Package

This package is tailored for the data analyst, with more convenient methods for manipulating data tables.
Combined with ```numpy```, above, for handling numerical objects, and ```matplotlib``` for plotting outputs, this trio is a powerful combination for data analysis.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# You can create a series of values.
s = pd.Series([1,3,5,np.nan,6,8])
s

# You can easily manipulate dates.
dates = pd.date_range('20130101', periods=6)
duplicates

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

```


Pandas has more advanced tricks for file I/O

```python
# Read and Write to CSV
pd.read_csv('file.csv', header=None, nrows=5)
pd.to_csv('myDataFrame.csv')

# Read multiple sheets from the same file
xlsx = pd.ExcelFile('file.xls')
df = pd.read_excel(xlsx,  'Sheet1')

# Read and Write to Excel
pd.read_excel('file.xlsx')
pd.to_excel('dir/myDataFrame.xlsx',  sheet_name='Sheet1')
```
There are many other functions to operate on data frames in combination with the ```pandas``` package.
Try either of the commands below, for an arbitrary data frame with column names 'a', 'c', or 'Country' as in the following examples.  

```python
# Drop values from rows (axis=0, the default)
s.drop(['a',  'c'])

# Drop values from columns(axis=1)
df.drop('Country', axis=1)

# Sort by labels along an axis
df.sort_index()

# Sort by the values along an axis

df.sort_values(by='Country')
```


For examples of the use of the pandas package to prepare data
for linear and logistic regression, see the sample files
```python_linear_regression.py``` and ```python_logistic_regression.py``` above.
