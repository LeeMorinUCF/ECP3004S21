# Regression in Python

This is a quick introduction to the concept of regression analysis. 
For those of you who have taken a course in regression analysis, 
this will be a review. 
For others, this is a quick overview of modeling in Python. 
We will focus on the implementation of the estimation
but not the interpretation of the statistics, 
which is outside the scope of this course. 
Please consult a statistics or econometrics textbook
for further details. 

## Linear Regression 

Linear regression is a statistical method for obtaining a prediction of an outcome 
<img src="https://render.githubusercontent.com/render/math?math=Y_i"> 
from an observed variable.

### The Regression Equation


The prediction takes the form of a linear equation for the prediction of 
<img src="https://render.githubusercontent.com/render/math?math=Y_i"> 
as a linear combination of the variables
<img src="https://render.githubusercontent.com/render/math?math=X_i">
multiplied by the parameter
<img src="https://render.githubusercontent.com/render/math?math=\beta_1">, 
plus an intercept
<img src="https://render.githubusercontent.com/render/math?math=\beta_0">.

<img src="Images/Regression_Equation.png">


### The Minimization Problem

The parameters 
<img src="https://render.githubusercontent.com/render/math?math=\beta_1"> 
and
<img src="https://render.githubusercontent.com/render/math?math=\beta_0">
are estimated by minimizing the sum of squared residuals from the regression line defined by
<img src="https://render.githubusercontent.com/render/math?math=\beta_1"> 
and
<img src="https://render.githubusercontent.com/render/math?math=\beta_0">.
The residuals are the differerences from the observed values 
<img src="https://render.githubusercontent.com/render/math?math=Y_i"> 
from the values predicted by the regression line. 


<img src="Images/Regression_Minimization.png">


### Estimating a Linear Regression in Python

Estimating a linear regression in R involves three main steps.
1. Reading in the data.
1. Preparing the data.
1. Specifying the regression equation.
1. Calculating the statistics for the regression model.


As above, you can read in the data with the ```read_csv``` from the ```pandas``` module for data analysis. 

```
import pandas as pd
my_data = pd.read_csv('name_of_my_data_set_file.csv')
```

Much like the ```lm``` function in R, you pass the dataset and the fornula to the ```ols``` method in the ```statsmodels``` module. 
```
import statsmodels.formula.api as sm
reg_model_sm = sm.ols(formula = "Y ~ X_1 + X_2 + X_3", data = my_data).fit()
```


The results of the regression are stored in the object ```reg_model_sm```. 
You can print out the regression results by summarizing ```reg_model_sm``` which was created by the ```ols``` method.
This is done by using the ```summary``` method for that object. 


```
# Display a summary table of regression results.
print(reg_model_sm.summary())

```



### The Fit of a Regression Model

The quality of fit of a regression model is determined by the degree to which the observations fit close to the regression line. 
It is represented by the statistic 
<img src="https://render.githubusercontent.com/render/math?math=r^2">, 
pronounced "R-squared."
This statistic ranges from 
<img src="https://render.githubusercontent.com/render/math?math=r^2 = 1">, 
for a model that fits the data perfectly,
to 
<img src="https://render.githubusercontent.com/render/math?math=r^2 = 0">, 
if the dependent variable 
<img src="https://render.githubusercontent.com/render/math?math=Y_i">
is unrelated to the explanatory variable
<img src="https://render.githubusercontent.com/render/math?math=X_i">.
This statistic is shown in the regression output under the headings
```R-squared``` and ```Adj. R-squared```.
Again, the ```Adj. R-squared``` includes an adjustment, or penalty, to account for the number of variables in the model, because
the ```Adj. R-squared``` can only be improved by including more variables in the model. 

<img src="Images/Linear_regression.png">


## Data Preparation and Analysis

For most regression projects, data preparation most of the work. 
The ```pandas``` package is very useful for doing most forms of data manipulation. 


### Where is your data?


Before anything else, set the working directory.
This tells python which folder you will be working in. 
It should be the location in which you have your dataset. 


```python
>>> import os
# Find out the current directory.
>>> os.getcwd()
# Change to a new directory.
# os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\demo_09_Modules_for_Regression')
>>> os.chdir('C:\\Users\\le279259\\OneDrive - University of Central Florida\\Documents\\GitHub\\ECP3004S21\\demo_09_Modules_for_Regression')
# Check that the change was successful.
>>> os.getcwd()
'C:\\Users\\le279259\\OneDrive - University of Central Florida\\Documents\\GitHub\\ECP3004S21\\demo_09_Modules_for_Regression'
```


### The ```pandas``` Package


This package is tailored for the data analyst, with more convenient methods for manipulating data tables.
Combined with ```numpy```, above, for handling numerical objects, and ```matplotlib``` for plotting outputs, this trio is a powerful combination for data analysis.

```python
>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib.pyplot as plt
```


You can create a series of values.
```python
>>> s = pd.Series([1,3,5,np.nan,6,8])
>>> s
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
```

You can easily manipulate dates.

```python
>>> dates = pd.date_range('20130101', periods=6)
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
```

You can combine the above to create data frames, much like you might read from files.

```python
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
>>> df
                   A         B         C         D
2013-01-01  0.312279 -0.689811  0.085896 -0.542083
2013-01-02 -0.531894 -0.551255  0.575098  0.994047
2013-01-03  0.318610 -0.129641 -0.070425 -0.770762
2013-01-04 -0.326679  0.148532  0.917764 -1.035208
2013-01-05  1.483810  0.411542  0.914557  1.772632
2013-01-06 -0.045553 -1.560606 -0.593070 -0.095951
```

You can create a data frame, which is another type of object for organizing data.

```python
>>> df2 = pd.DataFrame({ 'A' : 1.,
        'B' : pd.Timestamp('20130102'),
        'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
        'D' : np.array([3] * 4,dtype='int32'),
        'E' : pd.Categorical(["test","train","test","train"]),
        'F' : 'foo' })
>>> df2
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
```

Take a look at the individual types of columns in the data frame.

```python
>>> df2.dtypes
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
```

That is only one attribute of a data frame. There are many others.

```python
>>> df2.head(3)
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
>>> df2.tail(3)
     A          B    C  D      E    F
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> df.index
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df.columns
Index(['A', 'B', 'C', 'D'], dtype='object')
>>> df.values
array([[ 0.31227853, -0.68981113,  0.08589623, -0.54208322],
       [-0.53189446, -0.55125458,  0.57509792,  0.99404662],
       [ 0.31860967, -0.12964078, -0.07042486, -0.77076157],
       [-0.32667853,  0.14853208,  0.91776385, -1.035208  ],
       [ 1.48380991,  0.41154229,  0.91455671,  1.77263155],
       [-0.04555334, -1.56060619, -0.59306953, -0.0959513 ]])
```

A useful function will calculate summary statistics for your data.

```python
>>> df.describe()
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.201762 -0.395206  0.304970  0.053779
std    0.713888  0.705169  0.602573  1.102886
min   -0.531894 -1.560606 -0.593070 -1.035208
25%   -0.256397 -0.655172 -0.031345 -0.713592
50%    0.133363 -0.340448  0.330497 -0.319017
75%    0.317027  0.078989  0.829692  0.721547
max    1.483810  0.411542  0.917764  1.772632
```

Linear algebra operations are also a possibility, such as the transpose.

```python
>>> df.T
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A    0.312279   -0.531894    0.318610   -0.326679    1.483810   -0.045553
B   -0.689811   -0.551255   -0.129641    0.148532    0.411542   -1.560606
C    0.085896    0.575098   -0.070425    0.917764    0.914557   -0.593070
D   -0.542083    0.994047   -0.770762   -1.035208    1.772632   -0.095951
```

There are many options to get subsets of the data frame.

```python
>>> df['A']
2013-01-01    0.312279
2013-01-02   -0.531894
2013-01-03    0.318610
2013-01-04   -0.326679
2013-01-05    1.483810
2013-01-06   -0.045553
Freq: D, Name: A, dtype: float64
>>> df[0:3]
                   A         B         C         D
2013-01-01  0.312279 -0.689811  0.085896 -0.542083
2013-01-02 -0.531894 -0.551255  0.575098  0.994047
2013-01-03  0.318610 -0.129641 -0.070425 -0.770762
>>> df['20130102':'20130104']
                   A         B         C         D
2013-01-02 -0.531894 -0.551255  0.575098  0.994047
2013-01-03  0.318610 -0.129641 -0.070425 -0.770762
2013-01-04 -0.326679  0.148532  0.917764 -1.035208
```

You can also use boolean logic to get subsets.

```python
>>> df[df.A > 0]
                   A         B         C         D
2013-01-01  0.312279 -0.689811  0.085896 -0.542083
2013-01-03  0.318610 -0.129641 -0.070425 -0.770762
2013-01-05  1.483810  0.411542  0.914557  1.772632
>>> df[df > 0]
                   A         B         C         D
2013-01-01  0.312279       NaN  0.085896       NaN
2013-01-02       NaN       NaN  0.575098  0.994047
2013-01-03  0.318610       NaN       NaN       NaN
2013-01-04       NaN  0.148532  0.917764       NaN
2013-01-05  1.483810  0.411542  0.914557  1.772632
2013-01-06       NaN       NaN       NaN       NaN
```

The symbol ```NaN``` is an abbreviation for "not a number". 
It is used as a placeholder when the value is missing. 



There are many other functions to operate on data frames in combination with the ```pandas``` package.


Drop values from columns (axis=1).
```python
>>> print(df2)
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> df.drop('B', axis=1)
     A    C  D      E    F
0  1.0  1.0  3   test  foo
1  1.0  1.0  3  train  foo
2  1.0  1.0  3   test  foo
3  1.0  1.0  3  train  foo
>>> print(df2)
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
```

Notice that the drop command only produced the requested dataset, 
instead of permanently removing it.  

Sort by the values along an axis

```python
>>> df2.sort_values(by='E')
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
2  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
3  1.0 2013-01-02  1.0  3  train  foo
```




### File IO with Microsoft Excel


Pandas has more advanced tricks for file I/O (that is, Input/Output). 

Here are some samples of code to use when the corresponding
files exist in your working directory.

One of the most common way to work with a dataset is to read and write to a csv file.

```python
>>> pd.read_csv('file.csv', header=None, nrows=5)
>>> pd.to_csv('myDataFrame.csv')
```

You can also read from Excel files, by selecting the worksheet. 

```python
>>> xlsx = pd.ExcelFile('file.xls')
>>> df = pd.read_excel(xlsx,  'Sheet1')
```


You can also write to an Excel worksheet. 

```python
>>> pd.read_excel('file.xlsx')
>>> pd.to_excel('dir/myDataFrame.xlsx',  sheet_name='Sheet1')
```


For examples of the use of the pandas package to prepare data
for linear regression and estimate the model, see the sample files
```reg_with_stats_models.py``` and ```reg_with_sklearn.py``` above.


