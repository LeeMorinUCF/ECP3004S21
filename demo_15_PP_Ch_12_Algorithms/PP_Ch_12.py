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
# March 2, 2021
# 
##################################################
#
# Demo for Chapter 12: Algorithms
#
##################################################
"""


##################################################
# Import Modules.
##################################################


import os # To set working directory



##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
git_path = 'C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\'
os.chdir(git_path + 'demo_15_PP_Ch_12_Algorithms')
# Check that the change was successful.
os.getcwd()


##################################################
## Searching for The Two Smallest Values
##################################################

# We will explore how to find the index of the two smallest numbers 
# in an unsorted list, using three different approaches.

# Consider the following list of the number of humpback whales 
# sighted off the coast of British Columbia over ten years. 
# It is easy to find the smallest value. 

counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]

min(counts)


# If we want to know the year in which this minimum value occurred, 
# we can use the ```list.index``` method. 

low = min(counts)
low

counts.index(low)


# Or, more succinctly:

counts.index(min(counts))


# Now what could we do 
# if we wanted to find the *two* smallest values? 

# Now that we have defined the problem, 
# let's consider the approaches we could take. 
# There are three distinct algorithms that can achieve our goal
# and we'll start with a high-level description of each. 


##################################################
### Find, Remove, Find
##################################################

import find_remove_find5

find_remove_find5.find_two_smallest(counts)




##################################################
### Sort, Identify Minimums, Get Indices
##################################################

import sort_then_find3

sort_then_find3.find_two_smallest(counts)



##################################################
### Walk Through the List
##################################################

import walk_through7

walk_through7.find_two_smallest(counts)


##################################################
### Test Using doctest
##################################################

import doctest

doctest.testmod(find_remove_find5)

doctest.testmod(sort_then_find3)

doctest.testmod(walk_through7)


##################################################
## Timing the Functions
##################################################

import time_comparison

sea_levels = []
sea_levels_file = open('sea_levels.txt', 'r')
for line in sea_levels_file:
    sea_levels.append(float(line))
sea_levels_file.close()



# Time each of the approaches.
find_remove_find_time = time_comparison.time_find_two_smallest(
    find_remove_find5.find_two_smallest, sea_levels)

sort_get_minimums_time = time_comparison.time_find_two_smallest(
    sort_then_find3.find_two_smallest, sea_levels)

walk_through_time = time_comparison.time_find_two_smallest(
    walk_through7.find_two_smallest, sea_levels)

# Print the results to screen.


print('"Find, remove, find" took {:.2f}ms.'.format(find_remove_find_time))
print('"Sort, get minimums" took {:.2f}ms.'.format(
    sort_get_minimums_time))
print('"Walk through the list" took {:.2f}ms.'.format(walk_through_time))


# These times are hardly noticeable for lists with thousands of elements
# but, for large lists, the differences can be very large. 



##################################################
## End
##################################################

