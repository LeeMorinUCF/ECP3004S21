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
# January 10, 2021
# 
##################################################
#
# Demo for Chapter 3: Functions
# Part B: Designing Functions
#
##################################################
"""

##################################################
## The Function Design Recipe
##################################################

# The five steps to function design are as follows:

# 1. **Examples** Type a few example calls and determine what it 
#     should return for those values. 
#     The name of your function should indicate what is being 
#     calculated in your examples. 
# 2. **Description** Write a few sentences to describe what 
#     your function does. 
# 3. **Header** Type some documentation relating to your function. 
#     It should be clear to the reader what arguments it takes 
#     as input and what value is returned and the types of each variable. 
# 4. **Body** By now, you should be clear about how your function 
#     will work. 
#     Now type the code to perform the calculations. 
# 5. **Test** Run the examples from step 1 to verify that your 
#     function works as expected. 


##################################################
## Function Design Example
##################################################


# Consider the simple example of the function add_two_numbers 
# that, well, adds two numbers.

# Define a function without documentation.
def add_two_numbers(first_number, second_number):
    
    total = first_number + second_number
    
    return total


# The function is fine but how does the user know how it works. 
# Guessing is only reasonable if the function is simple. 

add_two_numbers(3,4)



# That makes sense and it appears to work. 
# If your user wants to know for sure, they can
# search for documentation, as you would for any other function.

help(add_two_numbers)


# There's not much there yet.


# You could print the entire function object but that
# is not very convenient for long and complex functions.

add_two_numbers
# <function __main__.add_two_numbers(first_number, second_number)>

# Instead, add documentation to the function in a docstring.


def add_two_numbers(first_number, second_number):
    """ Add two numbers together and return the sum.
    
    """
    
    total = first_number + second_number
    
    return total




# Now test the documentation by calling for help:

help(add_two_numbers)
# Help on function add_two_numbers in module __main__:

# add_two_numbers(first_number, second_number)
#     Add two numbers together and return the sum.
    
    
# Notice the content from the description in the docstring.

# We can improve the docstring by including examples, 
# so now let's cover all of these step by following
# the *function design recipe*. 



##################################################
## Function Design Recipe
##################################################

# Now apply the function design recipe to the add_two_numbers example.

#-------------------------------------------------
### Examples
#-------------------------------------------------

# Try to think of some examples that will test the limit of your function. 
# Note that we can run the tests only because we have already defined the 
# function in the examples above.

add_two_numbers(3,4)

add_two_numbers(0,4)

add_two_numbers(-3,3)



# Now you know that your function will have a form like this.


def add_two_numbers(first_number, second_number):
    
    
    
    return total




#-------------------------------------------------
### Header
#-------------------------------------------------

# Write a header to contain information about the
# the types of variables in your function. 


def add_two_numbers(first_number: float, second_number: float) -> float:
    
    
    
    return total



#-------------------------------------------------
### Description
#-------------------------------------------------

# Add a description of what your function does, in words.
# Include the list of your examples.

def add_two_numbers(first_number: float, second_number: float) -> float:
    """ Add two numbers together and return the sum.
    >>> add_two_numbers(3,4)
    7
    >>> add_two_numbers(0,4)
    4
    >>> add_two_numbers(-3,3)
    0
    """
    
    
    
    return total




#-------------------------------------------------
### Body
#-------------------------------------------------

# In this case, the body is simple but this is often the most work. 

def add_two_numbers(first_number: float, second_number: float) -> float:
    """ Add two numbers together and return the sum.
    >>> add_two_numbers(3,4)
    7
    >>> add_two_numbers(0,4)
    4
    >>> add_two_numbers(-3,3)
    0
    """
    
    total = first_number + second_number
    
    return total



# It seems like a lot of work to do to prepare to write one line of code.
# With more elaborate functions, having clearly stated the 
# examples, header and description, 
# you should be clear about what it is you will compute and the planning will pay off. 



#-------------------------------------------------
### Test
#-------------------------------------------------

# Finally, test your functions to confirm accuracy. 


add_two_numbers(3,4)

add_two_numbers(0,4)

add_two_numbers(-3,3)


# If all goes well, these examples should all return 
# the values you expect. 
# If not, be sure that your examples are correct
# or modify your function definition. 
# Most of the work in coding is correcting your mistakes. 





##################################################
## Designing More Functions: Practice with the Recipe
##################################################

# Let's run through the function design recipe with a few examples
# to practice the 5 steps:
# 1. **Examples** Type example calls and what you expect it to return.
# Choose appropriate names for your function and it's arguments. 
# 2. **Description** Write a short description to describe what your function does. 
# 3. **Header** Type some documentation to describe the arguments and return value. 
# 4. **Body** Type the code to perform the calculations. 
# 5. **Test** Run the examples to verify that your function works as expected. 


##################################################
## Designing Three Birthday-Related Functions
##################################################



#-------------------------------------------------
### How Many Days Difference?
#-------------------------------------------------

# The first function we'll design will calculate
# the number of days between two days, which are both in the range 
# 1-365, indicating the day of the year.

#### 1. **Examples**: Create example function calls and return values. 

# The first example is simple: the second day comes after the first. 

# >>>  days_difference(200, 224)
# 24

# The second two consider different cases: 
# the first addresses the case when both dates are the same, 
# the second allows the dates to be listed in reverse order. 

 
# >>> days_difference(50, 50)
# 0
# >>> days_difference(100, 99)
# -1

# These examples are more useful than having several examples 
# similar to the first case. 


#### 2. **Description**: Describe what your function does. 

# State the name of the function, the names of the arguments, 
# and the types of variables, for both the arguments
# and the return value. 

 
# >>> def days_difference(day1:int, day2:int) -> int:




#### 3. **Header**: Describe the arguments and return value. 

# Describe, in words, what the function does, 
# so that a user will understand how to use it.
# Users also include yourself, and you will benefit from 
# this explicit statement as you design the body of the function. 

 
# ...     """Return the number of days between day1 and day2, which are
# ...     both in the range 1-365 (thus indicating the day of the
# ...     year).
# ...     """



#### 4. **Body**: Write the code to perform the calculations. 

# With everything mapped out, write the code that performs the calculation. 

 
def days_difference(day1: int, day2: int) -> int:
    """Return the number of days between day1 and day2, which are
    both in the range 1-365 (thus indicating the day of the
    year).
    >>> days_difference(200, 224)
    24
    >>> days_difference(50, 50)
    0
    >>> days_difference(100, 99)
    -1
    """
    return day2 - day1


#### 5. **Test**: Verify that your function works as expected. 

# All programmers make mistakes. 
# The good ones find mistakes and correct them. 
# Run your examples to verify the calculations. 

 
days_difference(200, 224)
# 24
days_difference(50, 50)
# 0
days_difference(100, 99)
# -1

# It *looks good to me* (LGTM). 

# Now that we have a function with a docstring, 
# we can call help on that function. 


 
help(days_difference)
# Help on function days_difference in module __main__:

# days_difference(day1:int, day2:int) -> int
#     Return the number of days between day1 and day2, which are both
#     in the range 1-365 (thus indicating the day of the year).

#     >>> days_difference(200, 224)
#     24
#     >>> days_difference(50, 50)
#     0
#     >>> days_difference(100, 99)
#     -1

 





#-------------------------------------------------
### What Weekday Will It be in the Future?
#-------------------------------------------------

# Now let's write a function to map the the day of the week to the numbers
# 1 to 7, representing Sunday through Saturday, respectively. 
# Our aim is to represent a day that is a certain number of days after
# a day corresponding to another weekday number. 
# We will make it more clear with examples. 

#### 1. **Examples**: Create example function calls and return values. 

# If we start on Tuesday (day 3), it should be Wednesday (day 4)
# one day later.

 
# >>> get_weekday(3, 1)
# 4
 
# Likewise, Saturday (day 7) comes one day after Friday (day 6). 

 
# >>> get_weekday(6, 1)
# 7
 

# Starting from Saturday (day 7), moving one day forward brings us to Sunday (day 1). 

 
# >>> get_weekday(7, 1)
# 1
 
# Moving zero days forward keeps the number on the same day.
# Moving seven days ahead will also result in the same weekday. 

 
# >>> get_weekday(1, 0)
# 1
# >>> get_weekday(4, 7)
# 4
 
# Also, moving any multiple of the seven days, such as ten weeks (70 days), 
# should bring us to the same weekday. 
# After 72 days, we will move from Saturday to another Saturday, ten weeks later,
# and another two days to the next Monday (day 2).

 
# >>> get_weekday(7, 72)
# 2
 



#### 2. **Description**: Describe what your function does. 

# This function takes day numbers as integers and 
# returns an integer from 1 to 7. 

 
# >>> def get_weekday(current_weekday: int, days_ahead: int) -> int:
 

#### 3. **Header**: Describe the arguments and return value. 

# Now we can put this into words. 

 
# ...     """Return which day of the week it will be days_ahead days
# ...     from current_weekday.
# ...
# ...     current_weekday is the current day of the week and is in
# ...     the range 1-7, indicating whether today is Sunday (1),
# ...     Monday (2), ..., Saturday (7).
# ...
# ...     days_ahead is the number of days after today.
# ...     """
 


#### 4. **Body**: Write the code to perform the calculations. 

# Next, we fill in the body of the function. 
# We use the modulud % to evaluate the day number as 
# the remainder after division by 7. 

 
def get_weekday(current_weekday: int, days_ahead: int) -> int:
    """Return which day of the week it will be days_ahead days
    from current_weekday.
    current_weekday is the current day of the week and is in
    the range 1-7, indicating whether today is Sunday (1),
    Monday (2), ..., Saturday (7).
    days_ahead is the number of days after today.
    >>> get_weekday(3, 1)
    4
    >>> get_weekday(6, 1)
    7
    >>> get_weekday(7, 1)
    1
    >>> get_weekday(1, 0)
    1
    >>> get_weekday(4, 7)
    4
    >>> get_weekday(7, 72)
    2
    """
    return current_weekday + days_ahead % 7
 

#### 5. **Test**: Verify that your function works as expected. 

# Now run the tests. 

 
get_weekday(3, 1)
# 4
get_weekday(6, 1)
# 7
get_weekday(7, 1)
# 8

# Wait a minute! Day 8 is one day out of range. 
# This should be a 1, instead, to represent Sunday. 

# Let's look back at the function to make some changes. 


 
def get_weekday(current_weekday: int, days_ahead: int) -> int:
    """Return which day of the week it will be days_ahead days
    from current_weekday.
    current_weekday is the current day of the week and is in
    the range 1-7, indicating whether today is Sunday (1),
    Monday (2), ..., Saturday (7).
    days_ahead is the number of days after today.
    >>> get_weekday(3, 1)
    4
    >>> get_weekday(6, 1)
    7
    >>> get_weekday(7, 1)
    1
    >>> get_weekday(1, 0)
    1
    >>> get_weekday(4, 7)
    4
    >>> get_weekday(7, 72)
    2
    """
    return (current_weekday + days_ahead) % 7
 

# In the first version, we forgot the parentheses (), 
# so that the modulus operated on days_ahead first, 
# an then added current_weekday. 
# In the corrected version, we perform the addition first
# and then convert the final day to a weekday number. 

# With that adjustment in place, let's test the function again. 

 
get_weekday(3, 1)
# 4
get_weekday(6, 1)
# 0
get_weekday(7, 1)
# 1


# The third case is fixed, returning a 1 for Sunday, 
# but now the second case fails, with a zero instead of 
# a weekday from 1 to 7. 

# Now we have to diagnose this problem. 
# Whenever the sum of days_ahead and current_weekday
# evaluate to a multiple of 7, the calculation 
# (current_weekday + days_ahead) % 7 returns zero. 

# How do we fix this? 
# One solution is to subtract one first, then calculate the
# remainder, and then add one back. 
# This change produces the following function. 


 
def get_weekday(current_weekday: int, days_ahead: int) -> int:
    """Return which day of the week it will be days_ahead days
    from current_weekday.
    current_weekday is the current day of the week and is in
    the range 1-7, indicating whether today is Sunday (1),
    Monday (2), ..., Saturday (7).
    days_ahead is the number of days after today.
    >>> get_weekday(3, 1)
    4
    >>> get_weekday(6, 1)
    7
    >>> get_weekday(7, 1)
    1
    >>> get_weekday(1, 0)
    1
    >>> get_weekday(4, 7)
    4
    >>> get_weekday(7, 72)
    2
    """
    return (current_weekday + days_ahead - 1) % 7 + 1
 



# With *that* adjustment in place, let's test the function *again*. 

 
get_weekday(3, 1)
# 4
get_weekday(6, 1)
# 7
get_weekday(7, 1)
# 1
get_weekday(1, 0)
# 1
get_weekday(4, 7)
# 4
get_weekday(7, 72)
# 2
 

# Now all of the test cases return the result we expect. 
# We are done (unless, of course, 
# the function fails in a way that we haven't thought of).
# Let's move on for now. 
# We will learn more about testing later. 


#-------------------------------------------------
### What Day Is My Birthday On?
#-------------------------------------------------

# Now that we have those two functions, we can design a third that
# uses these functions for intermediate calculations. 
# We can figure out what day of the week a birthday falls on, 
# given what day of the week it is today, what the current day of the year is, 
# and what day of the year the birthday falls on. 


#### 1. **Examples**: Create example function calls and return values. 

# If today is Thursday (day 5) and today is the third day of the year, 
# what day will it be on the fourth day of the year? 
# We expect it to be Friday, day 6. 

 
# >>> get_birthday_weekday(5, 3, 4)
# 6
 

# With the first two arguments the same (Thurday on the third day of the year), 
# but the birthday is on the 116th day of the year. 
# Let's look at a calendar: day number 116 would be ...

# ... April 26th, which would also be a Friday (day 6). 

 
# >>> get_birthday_weekday(5, 3, 116)
# 6
 
# What if, instead, we start at day 116, Friday, April 26 
# and the birthday we want is the 3rd day of the year? 
# That gives us Thursday, day 5, following the first example in reverse. 

 
# >>> get_birthday_weekday(6, 116, 3)
# 5

 



#### 2. **Description**: Describe what your function does. 

# We use the function names in our examples and choose
# sensible names for the arguments and specify that 
# all of them are integers. 

 
# >>> def get_birthday_weekday(current_weekday: int, current_day: int,
# ...                          birthday_day: int) -> int:
 



#### 3. **Header**: Describe the arguments and return value. 

# Now we can put this into words. 

 
# ...     """Return the day of the week it will be on birthday_day,
# ...     given that the day of the week is current_weekday and the
# ...     day of the year is current_day.
# ...
# ...     current_weekday is the current day of the week and is in
# ...     the range 1-7, indicating whether today is Sunday (1),
# ...     Monday (2), ..., Saturday (7).
# ...
# ...     current_day and birthday_day are both in the range 1-365.
# ...     """
 



#### 4. **Body**: Write the code to perform the calculations. 

# Let's take stock of the programs we have already:
# - Using days_difference, we can figure out how many days there are
# between two days. 
# - Using get_weekday, we can figure out what day of the week it will be
# given the current day of the week and the number of days away. 

# This is how many days away the birthday falls:
 
# days_difference(current_day, birthday_day)

# Now we can call that days_diff and plug it into get_weekday:
 
# get_weekday(current_weekday, days_diff)


# Putting it all together, we write the following function definition. 

 
def get_birthday_weekday(current_weekday: int, current_day: int,
                         birthday_day: int) -> int:
    """Return the day of the week it will be on birthday_day,
    given that the day of the week is current_weekday and the
    day of the year is current_day.
    current_weekday is the current day of the week and is in
    the range 1-7, indicating whether today is Sunday (1),
    Monday (2), ..., Saturday (7).
    current_day and birthday_day are both in the range 1-365.
    >>> get_birthday_weekday(5, 3, 4)
    6
    >>> get_birthday_weekday(5, 3, 116)
    6
    >>> get_birthday_weekday(6, 116, 3)
    5
    """
    days_diff = days_difference(current_day, birthday_day)
    return get_weekday(current_weekday, days_diff)
 



#### 5. **Test**: Verify that your function works as expected. 

# Run the function definitions in the Python shell and 
# evaluate the examples. 

 
get_birthday_weekday(5, 3, 4)
# 6
get_birthday_weekday(5, 3, 116)
# 6
get_birthday_weekday(6, 116, 3)
# 5
 
# Just as we expected. 


##################################################
## Writing and Running a Program
##################################################

# Recall the example in which we translated temperature from degrees
# Fahrenheit to degrees Celsius. 
# We can save this program in the file temperature.py. 


 
def convert_to_celsius(fahrenheit: float) -> float:
    """Return the number of Celsius degrees equivalent to fahrenheit
    degrees.
    >>> convert_to_celsius(75)
    23.88888888888889
    """

    return (fahrenheit - 32.0) * 5.0 / 9.0


print(convert_to_celsius(80))
print(convert_to_celsius(78.8))
print(convert_to_celsius(10.4))

 

# When you run it, Python will evaluate the three examples and print out those values. 

# Run the script to run examples in temperature.py.
exec(open("temperature.py").read())
# Note that you need to tell Python where the file is.


# 26.666666666666668
# 26.0
# -12.0


# Basically, the Python shell executes all of the commands in the script, 
# including function definitions, but also any other calculations that apear. 
# In Chapter 6, we will use the birthday example in a similar way,
# except that we will exert more control over which statements are evaluated. 



##################################################
## Omitting a Return Statement: None
##################################################

# Consider this function definition without a return statement. 
 
def f(x):
    x = 2 * x

# Now execute it and evaluate the result. 
res = f(3)
res


# Now print the result. 
print(res)


# This value still has a location in memory. 
id(res)


# It has a special type for the empty variable None, called 'NoneType'.
type(res)



# Now add a return statement.
# At least that makes the function design more transparent. 
def f(x):
    x = 2 * x
    return None

print(f(3))






##################################################
## Dealing with Situations That Your Code Doesn't Handle
##################################################

# Consider this example.
 
def pie_percent(n: int) -> int:
    """Assuming there are n people who want to eat a pie, return the
    percentage of the pie that each person gets to eat.
    >>> pie_percent(5)
    20
    >>> pie_percent(2)
    50
    >>> pie_percent(1)
    100
    """

    return int(100 / n)

# The function works...
pie_percent(5)

# ...but there is nothing to stop someone from entering a negative
# number of people. 
pie_percent(-5)

# One way to avoid problems is to add a precondition:

def pie_percent(n: int) -> int:
    """Precondition: n > 0
    Assuming there are n people who want to eat a pie, return the percentage
    of the pie that each person gets to eat.
    >>> pie_percent(5)
    20
    >>> pie_percent(2)
    50
    >>> pie_percent(1)
    100
    """

    return int(100 / n)


# At least when you warn the user, 
# it is not your fault:
# The user should have read the manual (RTM). 
 





##################################################
## End
##################################################