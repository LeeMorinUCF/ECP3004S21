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


