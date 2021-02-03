#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 23:05:03 2021

@author: lp1
"""

# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Luis Perez
#
# Date: 1/31/2021
# 
##################################################
#
# Sample Script for Assignment 2: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

import math


##################################################
# Function Definitions
##################################################

# Exercise 1
def average(a, b):
  return (a + b) / 2

# Exercise 2
def area_of_circle(r):
  return math.pi * r ** 2 

# Exercise 3
def volume_of_cylinder(r, h):
  return area_of_circle(r) * h

# Exercise 4
def utility(x, y, α):
  return x ** α * y ** (1 - α)

# Exercise 5
def logit(x, β0, β1):
  return math.exp(β0 + x * β1) / (1 + math.exp(β0 + x * β1))


##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results. 


print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating average(10,20)")
print("Expected: " + str(15.0))
print("Got: " + str(average(10,20)))

print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating average(2.5, 3.0)")
print("Expected: " + str(2.75))
print("Got: " + str(average(2.5, 3.0)))

print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating average(50.25,99)")
print("Expected: " + str(74.625))
print("Got: " + str(average(50.25,99)))

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")
print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating area_of_circle(3)")
print("Expected: " + str(28.274))
print("Got: " + str(area_of_circle(3)))
print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating area_of_circle(6.9)")
print("Expected: " + str(149.5712))
print("Got: " + str(area_of_circle(6.9)))
print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating area_of_circle(11.8)")
print("Expected: " + str(437.4354))
print("Got: " + str(area_of_circle(11.8)))

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")
print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating volume_of_cylinder(2, 5)")
print("Expected: " + str(62.8319))
print("Got: " + str(volume_of_cylinder(2, 5)))

print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating volume_of_cylinder(3, 9)")
print("Expected: " + str(254.469))
print("Got: " + str(volume_of_cylinder(3, 9)))

print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating volume_of_cylinder(4.5, 13.5)")
print("Expected: " + str(858.8329))
print("Got: " + str(volume_of_cylinder(4.5, 13.5)))

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating utility(2, 4, 2)")
print("Expected: " + str(1.0))
print("Got: " + str(utility(2,4,2)))
print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating utility(2, 4, 2)")
print("Expected: " + str(1.1628))
print("Got: " + str(utility(5,6,9)))
print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating utility(7.9, 2.3, 3.8)")
print("Expected: " + str(250.1180))
print("Got: " + str(utility(7.9, 2.3, 3.8)))

print("#" + 50*"-")
print("Testing my Examples for Exercise 5.")

print("#" + 50*"-")
print("Exercise 5, Example 1:")
print("Evaluating logit(8, 3, 5)")
print("Expected: " + str(1.0))
print("Got: " + str(logit(8, 3, 5)))
print("#" + 50*"-")

print("Exercise 5, Example 2:")
print("Evaluating logit(2.25, 6, 9.5)")
print("Expected: " + str(0.9999))
print("Got: " + str(logit(2.25, 6, 9.5)))
print("#" + 50*"-")

print("Exercise 5, Example 3:")
print("Evaluating logit(36, 79.5, 2.01)")
print("Expected: " + str(1.0))
print("Got: " + str(logit(36, 79.5, 2.01)))
print("#" + 50*"-")

##################################################
# End
##################################################