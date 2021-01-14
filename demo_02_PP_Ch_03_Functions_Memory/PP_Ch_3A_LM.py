# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business 
# University of Central Florida
#
# January 7, 2021
# 
##################################################
#
# Demo for Chapter 3: Functions
# Part A: Using Functions
#
##################################################
"""

##################################################
## Functions That Python Provides
##################################################

# Some functions are *built-in*


abs(-9)

abs(3.3)

 

# A *function call* is of the form
# function_name(argument_1, argument_2, argument_3, ./..).
# Arguments can be any value stored in memory. 



day_temperature = 10
night_temperature = 3
abs(day_temperature - night_temperature)

day_temperature = 3
night_temperature = 10
abs(day_temperature - night_temperature)


 
# You can combine the outputs of functions as operands in
# arithmetic operators: 

abs(-7) + abs(3.3)

 



3 + 5 / abs(-2)


 
# or as arguments in other operators


pow(abs(-2), round(4.3))


 

# Some functions convert from one type to another


int(34.6)

int(-4.3)

float(21)


 
# The help function will show documentation for a function.


help(abs)

 
# The round function also converts a floating-point number 
# into an integer:


round(3.8)

round(3.3)

round(3.5)

round(-3.3)

round(-3.5)


 
# but it can also be used to convert to a float with fewer significant digits.


round(3.141592653, 2)


 



help(round)

 
# There is more than one way to calculate exponents. 


help(pow)


#     Some types, such as ints, are able to use a more efficient algorithm when
#     invoked using the three argument form.

 
# If you pass only two arguments, it takes the empty value None by default.


pow(2, 4)

 
# If the third argument is provided, it performs the additional calculation. 


pow(2, 4, 3)

 

##################################################
## Memory Addresses: How Python Keeps Track of Values
##################################################

# The name of each variable corresponds to a location in memory.
# The id function returns an integer that identifies that location in memory.


help(id)
 

# Some values are already stored in memory.


id(-9)

id(23.1)



# Other variables that you create are immediately assiggned to locations in memory.

shoe_size = 8.5
id(shoe_size)

fahrenheit = 77.7
id(fahrenheit)


 
# Even functions are objects in memory and are assiggned to locations in memory. 

id(abs)

id(round)


 

#-------------------------------------------------
### Python Remembers and Reuses Some Objects
#-------------------------------------------------

# Python stores some very common numbers in special places in memory
# and reuses these locations as needed. 

i = 3
j = 3
k = 4 - 1
id(i)

id(j)

id(k)


 
# This is not the case for larger integers or floats. 

i = 30000000000
j = 30000000000
id(i)

id(j)

f = 0.0
g = 0.0
id(f)

id(g)


 


##################################################
## Defining Our Own Functions: Syntax
##################################################

# You might want to have a function that can convert temperature from
# Fahrenheit to Celsius.
# It should work as follows.


# convert_to_celsius(212)
# 100.0
# convert_to_celsius(78.8)
# 26.0
# convert_to_celsius(10.4)
# -12.0

 
# But if you run those function calls before the function is defined, 
# Python throws an error:


convert_to_celsius(212)


 
# So, you have to define the function. 
# Function definitions take the following format:


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


 
# The indenting is important because that is how Python
# knows when the function definition is complete. 


def convert_to_celsius(fahrenheit):
return (fahrenheit - 32) * 5 / 9


 
# After the function is defined, you can use it
# just as you would for built-in functions. 


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

convert_to_celsius(80)


 
# When you use a function to calculate its output from the arguments, 
# it is called *calling* the function.
# Test it with a few values.


def convert_to_celsius(fahrenheit):
	return (fahrenheit - 32) * 5 / 9

convert_to_celsius(80)
convert_to_celsius(78.8)
convert_to_celsius(10.4)

 

# Look for some documentation, just as you would for built-in finctions.


help(convert_to_celsius)


 

# There is no documentation. 
# *You* made the function, *you* provide the documentation. 
# You do that by including a docstring, a description
# enclosed in triple quotes, which includes a written 
# description and some examples. 


def convert_to_celsius(fahrenheit: float) -> float:
    """Return the number of Celsius degrees equivalent to fahrenheit
    degrees.
    convert_to_celsius(75)
    23.88888888888889
    """

    return (fahrenheit - 32.0) * 5.0 / 9.0


convert_to_celsius(80)
convert_to_celsius(78.8)
convert_to_celsius(10.4)

 

# Now try the help function again. 
help(convert_to_celsius)

#-------------------------------------------------
### Keywords Are Words That Are Special to Python
#-------------------------------------------------

# Because the def keyword was used to define a function, 
# it cannot be used as a variable. 


def = 3


# The same applies to built-in function names that are already defined. 


def return(x):

    
 

# But be careful: this does not apply to functions that *you* define. 
# When you overwrite your own function, the original definition 
# is discarded and replaced with the new function. 




##################################################
## Using Local Variables for Temporary Storage
##################################################

# It often helps make code more clear when you use separate 
# local variables for intermediate calculations. 
# These are called *local* variables because they are only 
# defined in the memory allocated within the function. 


def quadratic(a, b, c, x):
    first = a * x ** 2
    second = b * x
    third = c
    return first + second + third

quadratic(2, 3, 4, 0.5)

quadratic(2, 3, 4, 1.5)


 

# After you run the function, these variables 
# no longer exist outside of the function. 


quadratic(2, 3, 4, 1.3)

first



# Even the arguments are only defined within the function. 


a

 

# These arguments, without a default value, must be provided, 
# even if you assigned them a value in a previous function call. 

quadratic(1, 2, 3)


 
# The more errors you see, the easier it will be for you to 
# identify what the problem is and how to fix it. 

##################################################
## Tracing Function Calls in the Memory Model
##################################################

# What do you think this function does?


def f(x):
    x = 2 * x
    return x

x = 1
x = f(x + 1) + f(x + 2)
 

# Python keeps track of all the intermediate calculations
# in separate places in memory, one for each of the different x's above.

# See the explanation in *Practical Programming* on pages 40-46.



##################################################
## End
##################################################