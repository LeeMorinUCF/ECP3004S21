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
# March 15, 2021
# 
##################################################
#
# Demo for Chapter 13: Searching and Sorting
# Part A: Searching
#
##################################################
"""


##################################################
# Import Modules.
##################################################


import os # To set working directory
import doctest


##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
git_path = 'C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\'
os.chdir(git_path + 'demo_17_PP_Ch_13_Searching')
# Check that the change was successful.
os.getcwd()


##################################################
## Searching a List
##################################################


# Let's continue searching for values in a list. 
# First, consider the built-in functions and methods available.
# Python lists have a method called ```index```
# that searches for a particular item. 


# It starts at the front of the list and examines each item in turn--a
# technique called linear search. 
# Linear search is used to find items in an *unsorted* list. 
# If there are duplicate values, it finds the leftmost instance of ```value```:


['d', 'a', 'b', 'a'].index('a')
# 1


# We'll walk through several versions of linear search to determine how to compare 
# different algorithms that solve the same problem. 



##################################################
### Linear Search
##################################################

# Linear search starts at index zero and looks at each item one by one.
# For each item, we ask this question:
# Is this the value we are looking for at the current index?
# We'll show three variations and they are all versions
# of the function with this header and docstring. 


from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """

    # examine the items at each index i in lst, starting at index 0:
    #    is lst[i] the value we are looking for?  if so, stop searching.




# In the textbook, on page 245 to 246, you can see a visual description 
# of the process of linear search. 
# It shows a type of accounting exercise to keep track of what you have searched and what remains to be searched. 


#--------------------------------------------------
#### The ```while``` Loop Version of Linear Learch
#--------------------------------------------------

# This is our first version of linear search. 
# We will refine the commented lines to get them closer to Python commands.



from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    
    i = 0 # The index in the next item in lst to examine.
    
    # While the unknown section isn't empty, and lst[i] isn't 
    # the value we are looking for:
    # add 1 to i
    


# That is easier to translate. 
# The unknown section is empty when ```i == len(lst)```, 
# so it isn't empty ```while i != len(lst)```. 



from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """

    i = 0  # The index of the next item in lst to examine.

    # Keep going until we reach the end of lst or until we find value.
    while i != len(lst) and lst[i] != value:
        i = i + 1

    # If we fell off the end of the list, we didn't find value.
    if i == len(lst):
        return -1
    else:
        return i



doctest.testmod()

# The extra code block is needed because the function terminates
# in two situations:
# either the ```value``` is found or we run out of values without finding ```value```. 
# Notice that the second condition ```lst[i] != value```
# terminates early when the ```value``` is found. 

# If it goes to the end without finding ```value```, 
# it returns ```-1``` to indicate that the search failed to find ```value```. 


#--------------------------------------------------
#### The ```for``` Loop Version of Linear Learch
#--------------------------------------------------

# We could replace the ```while``` loop with a ```for``` loop
# by introducing a ```return``` statement when the value is found. 
# We might want to do this because the first ```while``` condition 
# is almost never used, except when the ```value``` is not found. 


from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """... Exactly the same docstring goes here ...
    """
    
    # For each index i in lst:
    #    If lst[i] is the value we are looking for:
    #       return i
    # 
    # If we get here, the value was not in lst, so we return -1. 



# We can translate this into Python.


from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """... Exactly the same docstring goes here ...
    """

    for i in range(len(lst)):
        if lst[i] == value:
            return i

    return -1



# With the ```for``` loop, we no longer need the first ```while``` condition
# because the ```for``` loop iterator controls the iteration. 
# We also avoid incrementing the iterator ```i``` manually. 
# Overall, this produces a faster algorithm, as we will see later. 


#--------------------------------------------------
#### Sentinel Search
#--------------------------------------------------

# The last form of linear search we will study is called *sentinel search*. 
# (A *sentinel* is a guard whose job it is to stand watch.)
# Recall one problem with the ```while``` loop search 
# is that we check ```i != len(lst)``` every iteration, 
# even though it can never evaluate to ```False``` except at the end of the ```lst```. 

# One trick we can use is to add the ```value``` to the end of the list
# to guarantee that the ```value``` will be found. 
# We do have to make sure to adjust the output in case the last item is the one we found. 



from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """... Exactly the same docstring goes here ...
    """
    
    # Set up the sentinel: append value to end of list.
    
    i = 0 # The index of the next item in lst to examine.
    
    # While lst[i] isn't the value we are looking for:
    #   Add 1 to i
    
    # Remove the sentinel.
    
    return i



# We also want to make sure that we clean up our mess:
# we alterest the list by ```append```ing a ```value```, 
# so we need to remove it to preserve the contents of the original list.
# In Python, the finished algorithm is: 


from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """... Exactly the same docstring goes here ...
    """

    # Add the sentinel.
    lst.append(value)

    i = 0

    # Keep going until we find value.
    while lst[i] != value:
        i = i + 1

    # Remove the sentinel.
    lst.pop()

    # If we reached the end of the list we didn't find value.
    if i == len(lst):
        return -1
    else:
        return i



# Note that all three of our searches are correct. 
# Which one you prefer is largely a matter of taste. 
# Some programmers dislike multiple return staements, with some buried
# in the middle of the function. 
# Others dislike modifying the inputs, for fear of introducing an error. 
# Still, others dislike the added ```while``` condition that is rarely used. 

#--------------------------------------------------
#### Timing the Searches
#--------------------------------------------------

# One way to settle the score is to compare them on timing.
# Here is a program that compares the functions. 


import time
import linear_search_1
import linear_search_2
import linear_search_3

from typing import Callable, Any

def time_it(search: Callable[[list, Any], Any], L: list, v: Any) -> float:
    """Time how long it takes to run function search to find
    value v in list L.
    """

    t1 = time.perf_counter()
    search(L, v)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.0

def print_times(v: Any, L: list) -> None:
    """Print the number of milliseconds it takes for linear_search(v, L)
    to run for list.index, the while loop linear search, the for loop
    linear search, and sentinel search.
    """

    # Get list.index's running time.
    t1 = time.perf_counter()
    L.index(v)
    t2 = time.perf_counter()
    index_time = (t2 - t1) * 1000.0

    # Get the other three running times.
    while_time = time_it(linear_search_1.linear_search, L, v)
    for_time = time_it(linear_search_2.linear_search, L, v)
    sentinel_time = time_it(linear_search_3.linear_search, L, v)

    print("{0}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}".format(
            v, while_time, for_time, sentinel_time, index_time))







L = list(range(10000001))  # A list with just over ten million values

print_times(10, L)  # How fast is it to search near the beginning?
print_times(5000000, L)  # How fast is it to search near the middle?
print_times(10000000, L)  # How fast is it to search near the end?


# On my machine, it returned:

#   Length    while    for sentinel  index
#       10	   0.00	  0.00	 39.67	  0.00
#  5000000	 869.59	344.43	449.31	 79.38
# 10000000	1704.08	711.43	906.12	148.91


# As we did last week, we use the function ```perf_counter``` 
# in the ```time``` module to compare performance. 
# The function ```time_it``` will call whichever search function it's given
# on ```v``` and ```L``` and return the time it took to complete the search. 
# Function ```print_times``` calls ```time_it``` 
# with the various linear search functions and prints those search times.

# You'll see that, when the value is early in the list, they all run quickly.
# They differ in terms of the amount of time it takes to complete searches
# for values later in the list. 
# The ```while``` loop search takes much longer than the others. 
# The ```for``` loop is a little faster than the sentinel search. 
# The built-in method ```lst.index``` dominates them all 
# but perhaps this is an unfair comparison because 
# built-in functions are often compiled in a lower-level language, 
# such as C++ or FORTRAN. 


##################################################
## Binary Search
##################################################

# So far, the searching algorithms we have considered assume an unsorted list.
# In this linear search, we have to check *every single value* 
# until we find what we are looking for. 

# If we had a *sorted* list to start with, we could speed up the search considerably. 
# Consider this: if we were searching for a value in a sorted list
# of a million values, we could first check the middle value. 
# If that value is lower than what we are looking for, 
# we have already ruled out 500,000 values! 

# This algorithm is analogous to the *bisection method* that we used last week 
# to solve for the roots of equations. 
# We are essentially solving for the "root"" of the "function"
# ```lst - value```. 

# Binary search and the bisection method work like the game of 20 questions, 
# except all 20 questions are of the form "Is the value in this range?"
# The secret to the power of this method to zoom in quickly on the value
# is the application of logarithms. 
# A *logarithm* of a number is how many times that number can be divided until we get 1. 
# For example, the log (base 2) of 4 is 2. 

# The log (base 2) of 16 is 4.

# The log (base 2) of 64 is 6.

# The log (base 2) of 256 is 8.

# The log (base 2) of 1024 is 10. 

# Continuing on, 2 raised to the power 20 is over a million, 
# so the log (base 2) of a million is less than 20. 
# This means that with 20 questions, we can find a value 
# in a sorted list of a million candidate values. 

# This is a good time to review the workings of 
# the bisection method for solving roots. 
# The analogue for the search problem is in the following program. 




from typing import Any

def binary_search(L: list, v: Any) -> int:
    """Return the index of the first occurrence of value in L, or return
    -1 if value is not in L.

    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 1)
    0
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 4)
    2
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 5)
    4
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 10)
    7
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], -3)
    -1
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 11)
    -1
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 2)
    -1
    >>> binary_search([], -3)
    -1
    >>> binary_search([1], 1)
    0
    """

    # Mark the left and right indices of the unknown section.
    i = 0
    j = len(L) - 1

    while i != j + 1:
        m = (i + j) // 2
        if L[m] < v:
            i = m + 1
        else:
            j = m - 1

    if 0 <= i < len(L) and L[i] == v:
        return i
    else:
        return -1



doctest.testmod()

# Notice that we have an exhaustive list of test cases 
# because the algorithm is quite complicated. 
# Our tests cover these cases:
# - The value is the first item. 
# - The value occurs twice. We want the index of the first one. 
# - The value is in the middle of the list.
# - The value is in the last item. 
# - The value is smaller than everything in the list. 
# - The value is larger than everything in the list. 
# - The value isn't in the list, but it is larger than some and smaller than others. 
# - The list has no items. 
# - The list has one item.


#--------------------------------------------------
### Binary Search Running Time
#--------------------------------------------------

# Now we can compare the binary search lalgorithm to the 
# built-in ```list.index``` method. 


import time
import binary_search


def time_it(search, L, v):
    """ (function, list, object) -> number

    Time how long it takes to run function search to find
    value v in list L.
    """

    t1 = time.perf_counter()
    search(L, v)
    t2 = time.perf_counter()

    return (t2 - t1) * 1000.0


def print_times(v, L):
    """ (object, list) -> NoneType

    Print the number of milliseconds it takes for linear_search(v, L)
    to run for list.index, the while loop linear search, the for loop
    linear search, and sentinel search.
    """

    # Get list.index's running time.
    t1 = time.perf_counter()
    L.index(v)
    t2 = time.perf_counter()
    index_time = (t2 - t1) * 1000.0

    # Get the other three running times.
    binary_time = time_it(binary_search.binary_search, L, v)

    print("{0}\t{1:.4f}\t{2:.4f}\t{3:.2f}".format(
            v, index_time, binary_time, index_time / binary_time))




L = list(range(10000001))  # A list with just over ten million values

print_times(10, L)  # How fast is it to search near the beginning?
print_times(5000000, L)  # How fast is it to search near the middle?
print_times(10000000, L)  # How fast is it to search near the end?

# On my machine, this returned:
    
#   Length     index    binary     ratio
#       10	  0.0014	0.0328	    0.04
#  5000000	 74.6748	0.0120	 6228.61
# 10000000	148.2985	0.0109	13566.79


# The results are impressive. 
# Binary search is much faster and is equally fast regrdless of the 
# location of the value in the list. 


# Keep in mind that this is an unfair comparison, 
# since the ```list.index``` method also works for unsorted lists, 
# so it doesn't take advantage of the sorted list. 
# Still, this is a good reason to investigate algorithms for sorting, 
# which we will do in the next lecture. 




##################################################
## End
##################################################

