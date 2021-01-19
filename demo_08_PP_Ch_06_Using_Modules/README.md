# Chapter 6: A Modular Approach to Program Organization

You can often solve problems by using programs 
and functions designed by others, rather than solving these 
problems on your own. 
A great advantage of Python is that there is a large community 
of programmers who contribute their own functions.
The typical unit for a set of functions and programs is a *module*. 


## Importing Modules

To gain access to the functions in a module, you *import* it.

```python 
import math
```
The ```math``` module contains a set of mathematical operations. 

A module has type ```module```.
```python 
>>> type(math)
<class 'module'>
``` 
You can acces the help for all the functions in a module just as you
would for a single function, with the ```help``` function. 

```python 
>>> help(math)
Help on module math:

NAME
    math

MODULE REFERENCE
    https://docs.python.org/3.6/library/math

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(...)
        acos(x)
        Return the arc cosine (measured in radians) of x.

    acosh(...)
        acosh(x)
        Return the inverse hyperbolic cosine of x.

[Lots of other functions not shown here.]

``` 

Many common functions--many functions that you might expect would come 
standard with Python--are not available unless you import them
in a module,

```python 
>>> sqrt(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined

``` 
After the ```import math``` statement, these functions are available
using the prefix ```math```. 

```python 
>>> math.sqrt(9)
3.0

``` 
Even the number ```pi``` requires the ```math``` module, 
along with other constants. 

```python 
>>> import math
>>> math.pi
3.141592653589793
>>> radius = 5
>>> print('area is', math.pi * radius ** 2)
area is 78.53981633974483

``` 

You *could* overwrite these values, since they are variables 
like any other, but that is a bad idea, since users would not expect this. 


```python 
>>> import math
>>> math.pi = 3 # DON'T do this!
>>> radius = 5
>>> print('area is', math.pi * radius ** 2)
area is 75

``` 
You don't need to import the entire module. 
You could import only the particular functions and constants that you need. 
When you use the ```from``` statement, it pulls certain elements
by name. 

```python 
>>> from math import sqrt, pi
>>> sqrt(9)
3.0
>>> radius = 5
>>> print('circumference is', 2 * pi * radius)
circumference is 31.41592653589793

``` 
Now these can be referenced as they are named. 
Since they have different names, there are no functions under the
usual name that would be assigned if the entire module were imported. 

```python 
>>> from math import sqrt, pi
>>> math.sqrt(9)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    math.sqrt(9)
NameError: name 'math' is not defined
>>> sqrt(9)
3.0
``` 


A good practice is to select only the functions you need. 
Otherwise, if you select all the functions (using the *wildcard* ```*```)
many functions will be imported into the namespace, 
which could cause conflicts with other variables. 


```python 
>>> from math import *
>>> print(sqrt(8))
2.8284271247461903

``` 


#### Module ```__builtins__```

Many functions are built into Python. 
These are collected within the ```__builtins__``` module. 
You might recognize some of the functions that we have used already. 

```python 
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning',
'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError',
'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError',
'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError',
'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning',
'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError',
'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration',
'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit',
'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError',
'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__',
'__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all',
'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr',
'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict',
'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float',
'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex',
'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license',
'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct',
'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed',
'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum',
'super', 'tuple', 'type', 'vars', 'zip']

``` 

You should avoid naming any variable using the names of functions in 
the ```__builtins__``` module. 



## Application: Linear Algebra


When using computers to solve a problem, one approach is to fully understand the solution before attempting to write a program to solve the problem.
It is often very useful to conceptualize the calculation first and then use a concise specification from which to write the program.
This approach takes advantage of the fast and reliable computation of modern computers: computers can perform calculations more quickly and reliably than humans can by hand.

However, computers are capable of much more.
The above approach is very limited in terms of the nature of problems that can be solved.
Computers can be used to solve problems that you don't know how to solve. 
You can use computers to help you understand a problem as you formulate a solution procedure. 
The most important ingredient is having a precise way of stating the problem. 
In the following we will use the ```numpy``` and ```scipy```
modules to solve a *system of linear equations* for a vector of unknown parameters. 


### The problem

First, consider solving a *system of linear equations* for a vector of unknown parameters. 
The objective is to find a *vector* ```x``` that, when multiplied by the *matrix* ```A``` produces the *vector* ```b```: ```x``` satisfies ```A %*% x == b```.
It is necessary to first understand how this calculation is performed. 
In matrix multiplication, the numbers in the resulting matrix are calculated as the *dot product* of the corresponding rows and columns of the matrices that are multiplied. 
The calculation proceeds in the pattern shown in the following figure. 

<img src="Images/Matrix_Mult_Example.png" width="500">

The simplest such calculation is to solve for a single vector in the multiplication. 

<img src="Images/Matrix_Vector_Example.png" width="500">

Here, we are given the matrix ```A```, on the left, and the product ```b = c(29, 51, 38)``` on the right. 
The objective is to find the (unknown) vector ```x = c(4, 7)```, using only ```A``` and ```b```. 
The most common such problem is when the matrix ```A``` is square, 
that is, it has the same number of rows and columns.


### The solution

An inefficient way to solve this problem is to find the *inverse* of the matrix ```A``` and multipy it against ```b```. 
This works but it takes many more computational steps. 
A better approach is to use row oprations to perform a form of Gaussian elimination. 
Although this may be the approach taken for hand calculations, there are other, more efficient algorithms for finding the solution to a set of equations.
This is a specialized area within mathematics that uses advanced theories in linear algebra to calculate solutions. 
Fortunately, for the practitioner, most computational packages have built-in functions for solving systems of linear equations. 

### Examples

The matrix multiplication operator in ```R``` is the symbol ```%*%```. 
In the first problem, it is used as follows.

```
A <- matrix(seq(6),
            nrow = 2,
            ncol = 3, 
            byrow = TRUE)
x <- matrix(c(10, 20, 30, 11, 21, 31),
            nrow = 3,
            ncol = 2)
b <- A %*% x

> b
     [,1] [,2]
[1,]  140  146
[2,]  320  335
```


The conceptually simple--but computationally expensive--approach is to calculate the inverse of the matrix ```A``` and then multiply ```b``` to achieve the solution ```b```. 

```
# Create a matrix and a vector.
A <- matrix(c(2, 2, 5, 10),
            nrow = 2,
            ncol = 2)
x <- matrix(c(1, 2),
            nrow = 2,
            ncol = 1)
b <- A %*% x

# Calculate the inverse of A.
A_inv <- solve(A)

x_soln_inv <- A_inv %*% b
> x_soln_inv
     [,1]
[1,]    1
[2,]    2       
```

This is useful if the user needs to solve a series of equations with the same matrix ```A``` but a set of different different vectors ```b```.

In general, you would simply solve the system to obtain the solution. 
This requires fewer calculations and is all that is needed when only the solution is required. 

```
# Use the solve function to solve for x.
x_soln <- solve(A, b)

# Compare with the original x:
x_soln_inv
x_soln

```


In the linear regression model, the objective is to find the value of the coefficients that minimize the sum of squared errors. 
This solution is often reduced, using calculus, to solution of a set of linear equations. 


