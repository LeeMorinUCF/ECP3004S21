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
# Demo for Chapter 2: Hello, Python
#
##################################################
"""


##################################################
## Expressions and Values: Arithmetic in Python
##################################################


# Python does arithmetic as you expect. For example:
  
4 + 13
  

# Other operations work similarly:
  
15 - 3

4 * 7


# Division produces numbers with decimals, called  floats ,
  
5 / 2

  

# even if the result is a whole number (called an integer or  int )

4 / 2

  


### Types

# An expression involving two floats produces a float

17.0 - 10.0
  

# Python typically uses the most general data type, 
# such as a float, even when one operand is an integer. 
 
17.0 - 10

17 - 10.0



# The dot is enough to identify a number as a float, 
# even if there are no decimals specified.
  
17 - 10.

17. - 10


# Some programmers think this is bad form, since a single dot
# could easily be missed, but python is built with many such shortcuts. 


#-------------------------------------------------
### Integer Division, Modulo, and Exponentiation
#-------------------------------------------------

# Two forward-slashes denote *integer division*, 
# which ignores the decimal remainder. 

53 // 24

# The remainder is calculated with the *modulo* operator. 
  
53 % 24
  

# Python doesn't round with integer division; it takes the  floor 

17 // 10
  

# If the number is negative, the floor is still one number lower:

-17 // 10
  

# When a sign is negative, the sign of the modulo output is 
# the sign of the divisor (the second operand).
  
-17 % 10

17 % -10

  
# These operators work with floats, as well, 
# except the result is still rounded to the nearest whole number.
  
3.3 // 1

3 // 1.0

3 // 1.1

3.5 // 1.1

3.5 // 1.3

  
# A double asterisk calculates an exponent
  
3 ** 6
  

# The above examples, with two operands, apply *binary operators*.
# Negation is a *unary operator* because it applies to one operand. 

-5

--5

---5


  

# It works exactly as you would expect if you repeatedly multiplied
# a number by negative 1. 



##################################################
## What *Is* a Type?
##################################################

# A type is a set of values, combined with a set of operations on those values. 
# In the above examples, the set of values are  int  or  float , 
# combined with the arithmetic operators. 


#-------------------------------------------------
### Finite Precision
#-------------------------------------------------

# Computers can calculate only a limited set of values, as
# numbers are held to only so many decimal places:

2 / 3

5 / 3


# Sometimes the calculations that would be equivalent on paper
# turn out to have small differences in variables with finite precision. 

2 / 3 + 1

5 / 3


# The size of the operands makes a difference as well, 
# especially when combining two numbers of very different magnitude.
  
10000000000 + 0.00000000001


#-------------------------------------------------
### Operator Precedence
#-------------------------------------------------

# Convert temperature from Fahrenheit to Celsius:
  
212 - 32 * 5 / 9

# Is that correct? No, because the order of operations
# dictate that the multiplication and division be completed first. 
# Use parentheses to force the priority of operations over *subexpressions*. 
  
(212 - 32) * 5 / 9
  

# Oerators with hiher precedence are evaluated before those with lower precedence. 
  
-2 ** 4

-(2 ** 4)

(-2) ** 4
  

# Exponentiation has higher precedence than negation.


##################################################
## Variables and Computer Memory: Remembering Values
##################################################

# The *assignment operator*,  = , assigns a value to be stored
# in a particular location in memory:

degrees_celsius = 26.0


# The variable *degrees_celsius* can be though of as the *address*
# to that location in memory. 
# Once it is assigned, it can be used in subsequent calculations. 
  
degrees_celsius = 26.0
degrees_celsius

9 / 5 * degrees_celsius + 32

degrees_celsius / degrees_celsius

 
 
# New variables can be assigned values from operations involving
# the other variables in memory. 
  
degrees_celsius = 15.5
difference = 100 - degrees_celsius
difference



#-------------------------------------------------
### Values, Variables and Computer Memory
#-------------------------------------------------

# How does the computer perform these calculations? 
# It performs the calcualtions one-at-a-time, in order of precedence,
# and stores the intermediate calculations in temporary
# locations in memory.
  
degrees_celsius = 26.0 + 5
degrees_celsius

  
# The  26.0 + 5  expression must be evaluated first, and stored somewhere, 
# before it is assigned to the variable  degrees_celsius ,
# and similarly for  2 * difference  in the following.
  
difference = 20
double = 2 * difference
double

difference = 5
double

# Notice that the later change to  difference 
# did not change the value of  double .


#-------------------------------------------------
### Augmented Assignment
#-------------------------------------------------

# You can update the value of a variable using the operations above:
  
score = 50
score

score = score + 20
score
  

# The shorthand notation  +=  performs both the addition 
# and the reassignment in one operator. 
  
score = 50
score

score += 20
score

  
# It works similarly for multiplication.
  
d = 2
d *= 3 + 4
d

  
# These two operations produce the same output:
  
number = 10
number *= number
number

  
number = 10
number = number * number
number
  

# You can repeat these operations to create a sequence of values

  
number = 3
number

number = 2 * number
number

number = number * number
number

  

##################################################
## How Python Tells You Something Went Wrong
##################################################

# Troubleshooting, called *debugging*, is a big part of programming. 
# Over time, you will gain experience deciphering error messages
# and finding *bugs*. 
# Some are self explanatory: 
  
3 + moogah

  
# For this command to work, there would have to be a variable
# named  moogah  in memory, i.e. defined before this calculation. 

# Binary operators require two operands:
  
2 +
  
# otherwise the syntax is invalid. 

# Some values are protected. 
# For example, numbers cannot be assigned new values. 

  
12 = x



##################################################
## A Single Statement That Spans Multiple Lines
##################################################

# The backslash operator will allow a single command to extend to the next line. 
 
2 + \
3
  
# Sometimes, you can use rewrite the expression, so that it is clear
# that the expression extends to the next line. 
  
(2 +
3)
 

# How to translate pre-heating time from Fahrenheit (in the cookbook)
# to Celsius (on the oven controls):
  
room_temperature_c = 20
cooking_temperature_f = 350
oven_heating_rate_c = 20
oven_heating_time = (
((cooking_temperature_f - 32) * 5 / 9) - room_temperature_c) / \
oven_heating_rate_c
oven_heating_time

  

# We can use whitespace to make it clearer:
  
oven_heating_time = (
    ((cooking_temperature_f - 32) * 5 / 9) - room_temperature_c) / \
    oven_heating_rate_c
  

# We can also spread the calculation out over several lines 
# to make each part more clear.
  
oven_heating_time = (
    ((cooking_temperature_f - 32) * 5 / 9) -
     room_temperature_c) / \
    oven_heating_rate_c
  

# We could also change the order of calculations
# to perform intermediate calculations separately. 
  
room_temperature_c = 20
cooking_temperature_f = 350
cooking_temperature_c = (cooking_temperature_f - 32) * 5 / 9
oven_heating_rate_c = 20
oven_heating_time = (cooking_temperature_c - room_temperature_c) / \
    oven_heating_rate_c
oven_heating_time
  

# Coders differ in terms of their preferred style. 
# Some like to play *code golf* by performing a calculation in 
# the minimum number of lines. 
# That's fine, for an expert, but a beginner should separate 
# calculations to simplify the coding (and debugging). 

# In fact, a good way to produce reliable programs is to 
# separate the calculation into small parts that are easy to code 
# and to test--then you might not have to do any debugging.


##################################################
## Describing Code
##################################################

# Help a human understand your program by using the  #  character. 
# Python ignores anything in a line after the  #  character
# (and the entire line if it begins with  # ).


  
# Python ignores this sentence because of the # symbol.

  
# A future user that understands what is going on will be happier
# to use your program. 
# Sometimes the future user is *future you*.



##################################################
## End
##################################################
