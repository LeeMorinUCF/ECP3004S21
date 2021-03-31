# Nonparametric Methods

This demo, in the corresponding script ```python_nonparametrics.py``` 
gives examples of "regression" models
by considering a number of different model specifications. 
A *model specification* is a precise statement of the equation to be estimated. In this example, many of the model specification choices
  have a nonparametric form and are compared to parametric models.
A *parametric* model is the form that you would find familiar from
  QMB 3200 or a linear regression course: 
  it is an equation with *parameters* (i.e. slope coefficients) to estimate.
A *nonparametric* model specifies the algorithm that performs the model-fitting
  but the form of the equation can be an arbitrary curve in a family of
  functions. 
  Several machine learning models have this property. 
In this demo, we use a sample dataset tractor_sales.csv 
with the following variables:
-  saleprice is the sale price of a tractor in dollars
-  horsepower is the horsepower rating of the engine
-  age is the age of the tractor in years
-  enghours is the number of hours the engine has been run
-  diesel is an indicator that the engine runs on diesel fuel
-  fwd indicates that the tractor has four-wheel-drive
-  manual indicates that the tractor has a manual transmission
-  johndeere indicates that the brand of the tractor is John Deere
-  cab indicates that the tractor has an enclosed cab
-  spring indicates that the tractor was sold in the spring
-  summer indicates that the tractor was sold in the summer
-  winter indicates that the tractor was sold in the winter

We will use the following Python modules:

- os to set the working directory
- numpy for the logistic transformation
- pandas to read and inspect data
- statsmodels.formula.api to estimate linear regression
- statsmodels.nonparametric.kernel_regression for nonparametric kernel regression
- matplotlib.pyplot to plot regression results


We begin by loading the dataset

```python
tractors = pd.read_csv('tractor_sales.csv')
```

Inspect the data before modeling. 
The dataset has three numeric variables
```python
tractors[['saleprice','horsepower','age','enghours']].describe()
           saleprice  horsepower         age      enghours
count     276.000000  276.000000  276.000000    276.000000
mean    20746.557971  101.061594   15.905797   3530.224638
std     27522.114033   84.611711    9.679134   3408.494043
min      1500.000000   16.000000    2.000000      1.000000
25%      7750.000000   47.750000    7.000000    777.250000
50%     12000.000000   80.000000   15.000000   2398.000000
75%     20925.000000  108.500000   24.000000   5409.750000
max    200000.000000  535.000000   33.000000  18744.000000
```

There are also several binary variables.
```python
tractors[['manual','johndeere','cab',
          'spring', 'summer', 'winter']].describe()
           manual   johndeere         cab      spring      summer     winter
count  276.000000  276.000000  276.000000  276.000000  276.000000  276.00000
mean     0.702899    0.141304    0.543478    0.224638    0.231884    0.17029
std      0.457812    0.348968    0.499011    0.418102    0.422802    0.37657
min      0.000000    0.000000    0.000000    0.000000    0.000000    0.00000
25%      0.000000    0.000000    0.000000    0.000000    0.000000    0.00000
50%      1.000000    0.000000    1.000000    0.000000    0.000000    0.00000
75%      1.000000    0.000000    1.000000    0.000000    0.000000    0.00000
max      1.000000    1.000000    1.000000    1.000000    1.000000    1.00000
```

We will use these variables to predict the price of used tractors. 



## Visualizing the dependent variable

### Histograms


First, plot a histogram with the default width of bins.

```python
n, bins, patches = plt.hist(x = tractors['saleprice'], 
                            bins = 'auto', 
                            color = '#0504aa',
                            alpha = 0.7, rwidth = 0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.title('Histogram of Tractor Sales Prices')
plt.show()
```

You might not know it but you have just conducted
nonparametric estimation.

Now, let's see if we can fine-tune this picture.


We can choose the number of bins to determine
the smoothness the distribution.

```python
n, bins, patches = plt.hist(x = tractors['saleprice'], 
                            bins = 10, 
                            color = '#0504aa',
                            alpha = 0.7, rwidth = 0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.title('Histogram of Tractor Sales Prices')
plt.show()
```

With 10 bins it appears to have a smoothly declining density.



Try it again with many bins.

```python
n, bins, patches = plt.hist(x = tractors['saleprice'], 
                            bins = 100, 
                            color = '#0504aa',
                            alpha = 0.7, rwidth = 0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.title('Histogram of Tractor Sales Prices')
plt.show()
```

Now it looks very choppy with too many
gaps between the populated bins.
The picture is too jagged.

At this point, you should appreciate the default values,
although sometimes you will want to do some fine-tuning
to investigate the data.


### Kernel density somoothing

Another way to visualize the density is by
*kernel density smooting*, which is so called
not because *we* intend to plot a density
but because *the method* uses a density to
calculate the plot.

It takes a weighted average, using a density
called a *kernel* at each point on the plot.

```python
dist = tractors['saleprice']

fig, ax = plt.subplots()
dist.plot.kde(ax = ax, legend = False, 
              title = 'Density of Tractor Sales Prices')
dist.plot.hist(density = True, ax = ax)
ax.set_ylabel('Probability')
ax.grid(axis = 'y')
ax.set_facecolor('#d8dcd6')
```


The kernel-smoothed density is essentially a
weighted average of the neigboring points, taken at
each value along the horizontal axis.


Similar to histograms, you can adjust the *bandwidth*
parameter to adjust the smoothness of the density.
The bandwidth determines the distance from each location
on the density that the weighted average weights heavily.


With a large bandwidth you get a smoother density.

```python
fig, ax = plt.subplots()
dist.plot.kde(ax = ax, legend = False, 
              title = 'Density of Tractor Sales Prices', 
              bw_method = 1)
dist.plot.hist(density = True, ax = ax)
ax.set_ylabel('Probability')
ax.grid(axis = 'y')
ax.set_facecolor('#d8dcd6')
```


Notice, however, that the density bleeds into negative territory,
which is not posible with sales.
(This doesn't make sense: no one pays for you to take their tractor.)

This density does not look very much like the histogram.

Try it again with a smaller bandwidth.

```python
fig, ax = plt.subplots()
dist.plot.kde(ax = ax, legend = False, 
              title = 'Density of Tractor Sales Prices', 
              bw_method = 0.1)
dist.plot.hist(density = True, ax = ax)
ax.set_ylabel('Probability')
ax.grid(axis = 'y')
ax.set_facecolor('#d8dcd6')
```

This is better but now the density is very jagged.
There are peaks on the prices that happened to occur
and valleys on the prices where sales did not occur.



## Logarithmic transformation

When regression modelling, the model fit is often more
accurate when the variable is nearly nrmally distributed.

Let's consider the log tractor price as the dependent variable.

```python
tractors['log_saleprice'] = np.log(tractors['saleprice'])
```
Now let's plot a histogram of the log sales prices.

With some trial-and-error, I chose 20 bins.
```python
n, bins, patches = plt.hist(x = tractors['log_saleprice'], 
                            bins = 20, 
                            color = '#0504aa',
                            alpha = 0.7, rwidth = 0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.title('Histogram of Log of Tractor Sales Prices')
plt.show()
```

This histogram looks almost symmetric.
It is much close to the normal distribution.

Now let's plot a density.

```python
dist_log = tractors['log_saleprice']

fig, ax = plt.subplots()
dist_log.plot.kde(ax = ax, legend = False, 
              title = 'Density of Log of Tractor Sales Prices', 
              bw_method = 0.5)
dist_log.plot.hist(density = True, ax = ax)
ax.set_ylabel('Probability')
ax.grid(axis = 'y')
ax.set_facecolor('#d8dcd6')
```

This looks very smooth but also plausible.
We should build a model to predict the
log of the tractor prices.

Note that when we do this, the coefficients no longer
have the same interpretation:
With this specification, the change in the explanatory
variables (the characteristics of the tractors)
indicates a proportional change in the
dependent variable (the prices of the tractors).



## Linear Regression.

In an econometrics course, you might fit a
linear regression model such as this one.

### Fit a Linear Regression Model (with ```statsmodels``` module).

This is a module designed in the format that would
commonly be used by statusticians (and in econometrics class).



Initialize and specify the logistic model.

```python
sm_fmla = "log_saleprice ~ \
    horsepower + \
    age + enghours + \
    diesel + fwd + manual + johndeere + cab + \
    spring + summer + winter"

reg_model_sm = sm.ols(formula = sm_fmla, 
                      data = tractors)
```

Fit the model.
```python
reg_model_fit_sm = reg_model_sm.fit()
```

Display a summary table of regression results.
```python
print(reg_model_fit_sm.summary())
```

You can see statistically significant relationships
with these variables.
Notice the positive relationship between prices
and horsepower.
We will investigate this relationship further.



### A nonlinear parametric model

Fit a model with quadratic form for horsepower.


Consider a polynomial functional form for horsepower.
The idea is that horsepower improves performance up to a limit,
then extra power does not add value; it only consumes more fuel,
so buyers don't want to pay as much for tractors with
higher fuel costs.

Create a variable squared_horsepower
to investigate quadratic relationship of sale price to horsepower.
```python
tractors['squared_horsepower'] = tractors['horsepower']**2
```

Now fit a regression model with this extra variable.
```python
sm_fmla = "log_saleprice ~ \
    horsepower + squared_horsepower + \
    age + enghours + \
    diesel + fwd + manual + johndeere + cab + \
    spring + summer + winter"

reg_model_sm = sm.ols(formula = sm_fmla, 
                      data = tractors)
```

Fit the model and display a summary table of regression results.
```python
reg_model_fit_sm = reg_model_sm.fit()

print(reg_model_fit_sm.summary())
```


## Nonparametric estimation


Now consider that the quadratic model may not be quite right.
Maybe it is some other nonlinear function.

A nonparametric approach can estimate the relationship
flexibly to determine what functional form should be used.

For kernel regression, we will pass the prices and horsepower
as separate arrays.

```python
y = tractors['log_saleprice']
X = tractors['horsepower']
```

Initialize the model object.
```python
kde_reg = npreg.KernelReg(endog = y, exog = X, var_type = 'c')
```

Fit the predictions to a grid of values.
```python
X_grid = np.arange(0, 500, 10)
kde_pred = kde_reg.fit(data_predict = X_grid)
```

Plot the fitted curve with a scattergraph of the data.
```python
fig, ax = plt.subplots()
ax.plot(tractors['horsepower'], tractors['log_saleprice'], 
        '.', alpha = 0.5)
ax.plot(X_grid, kde_pred[0], '-', color='tab:blue', alpha = 0.9)
plt.show()
```

### Tuning the bandwidth

In the above example, an algorithm determines
the size of the bandwidth.
You can also specify it as an array
the same length as the number of variables
(but we only used one variable: horsepower).


Initialize the model object.
```python
kde_reg = npreg.KernelReg(endog = y, exog = X, var_type = 'c', 
                          bw = np.array([10]))

# Fit the predictions to a grid of values. 
X_grid = np.arange(0, 500, 10)
kde_pred = kde_reg.fit(data_predict = X_grid)
```

Plot the fitted curve with a scattergraph of the data.
```python
fig, ax = plt.subplots()
ax.plot(tractors['horsepower'], tractors['log_saleprice'], 
        '.', alpha = 0.5)
ax.plot(X_grid, kde_pred[0], '-', color='tab:blue', alpha = 0.9)
plt.show()
```

You can see it is more variable and,
similarly, could be made smoother.


## Semiparametric estimation

Now, let's fit this curve in a linear regression model.

Initialize the model object, the 
fit the predictions to a grid of values. 

```python
kde_reg = npreg.KernelReg(endog = y, exog = X, var_type = 'c')

# X_grid = np.arange(0, 500, 10)
kde_pred = kde_reg.fit() 
```
Notice that this time, we did not pass a list of gridpoints
to produce a graph:
the default fits to the horsepower observations in the dataset, 
which we use to create a new variable.

Now, create the variable with this predicted curve.
```python
tractors['horsepower_np'] = kde_pred[0]
```

Then fit a regression model with this extra variable.
```python
sm_fmla = "log_saleprice ~ \
    horsepower_np + \
    age + enghours + \
    diesel + fwd + manual + johndeere + cab + \
    spring + summer + winter"

reg_model_sm = sm.ols(formula = sm_fmla, 
                      data = tractors)
```

Fit the model and display a summary table of regression results.
```python
reg_model_fit_sm = reg_model_sm.fit()

print(reg_model_fit_sm.summary())
```

The fit is an improvement but the quadratic form
for horsepower was already fairly good.
In business, you have to balance the added accuracy in prediction
against the added complexity of the estimation method. 
The tradeoff is in both computing time (both in and out of the computer)
but also in the risk of complications later on, 
in addition to the more lengthy explanation to the stakeholders.
This last point may seems insignificant to you now, 
but later you might find that it is difficult to book time
with a Vice President to make a decision on your findings. 


## Other Nonparametric Methods

How does this relate to the nnparametric methods described in
the textbook *Business Data Science* by Matt Taddy?
The nonparametric techniques discussed in Chapter 9
use decision trees to fit an arbitrary function to the data.
This produces a step function, or piecewise constant function
to approximate the relationship between, say, 
sales price and horsepower. 

Although decision trees produce a cruder approximation to the relationship, 
the main advantage of this method is in efficiency and, 
as a result, scalability:
it can be applied to datasets with a large number of variables
to determine which variables should be included in the model. 
Once you have a manageable number of variables, 
you can use an approach like the one we took above 
to estimate a well-specified model, 
with the flexibility to account for the nonlinearity present in the data. 



