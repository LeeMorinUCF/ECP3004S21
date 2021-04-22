#!/usr/bin/python
"""
##################################################
# 
# ECP 3004: Python for Business Analytics
# 
# Testing and Debugging
# 
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business Administration
# University of Central Florida
# 
# April 13, 2021
# 
# Chapter 15: Testing and Debugging
# 
# This program provides examples of unit tests. 
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
# git_path = 'C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\'
# os.chdir(git_path + 'demo_26_PP_Ch_15_Test_Debug')
drive_path = 'C:\\Users\\le279259\\OneDrive - University of Central Florida\\Documents\\'
# git_path = 'GitHub\\ECP3004S21\\'
git_path = 'Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\'
os.chdir(drive_path + git_path + 'demo_26_PP_Ch_15_Test_Debug')
# Check that the change was successful.
os.getcwd()


##################################################
## Case Study: Testing ```above_freezing```
##################################################


# Many weeks ago, we designed a function to determine whether 
# a temperature is above freezing. 

def convert_to_celsius(fahrenheit: float) -> float:
    """Return the number of Celsius degrees equivalent to fahrenheit degrees.

    >>> convert_to_celsius(75)
    23.88888888888889
    """

    return (fahrenheit - 32.0) * 5.0 / 9.0

def above_freezing(celsius: float) -> bool:
    """Return True iff temperature celsius degrees is above freezing.

    >>> above_freezing(5.2)
    True
    >>> above_freezing(-2)
    False
    """

    return celsius > 0

if __name__ == '__main__':
    fahrenheit = float(input('Enter the temperature in degrees Fahrenheit: '))
    celsius = convert_to_celsius(fahrenheit)
    if above_freezing(celsius):
        print('It is above freezing.')
    else:
        print('It is below freezing.')


# We ran some example calls using ```doctest```. 
# But we're missing a test:
# what happens if the temperature is zero? 
# Consider the next version of this function. 

def above_freezing_v2(celsius: float) -> bool:
    """Return True iff temperature celsius degrees is above freezing.

    >>> above_freezing_v2(5.2)
    True
    >>> above_freezing_v2(-2)
    False
    """

    return celsius >= 0



# Both of these functions produce the same value for all of the examples given. 
# How do we settle a tie-breaker? 
# We can find test cases for which each function produces different values. 

# The temperature zero degrees celcius provides such a test case. 


above_freezing(0)
# False


above_freezing_v2(0)
# True



# Cases like these are called *boundary cases* or *corner cases*, 
# which represent the boundary across which the function returns different values. 
# Boolean expressions are a good place to look for these
# but it might also depend on the mathematics behind the problem at hand. 


#--------------------------------------------------
### Testing ```above_freezing``` Using ```unittest```
#--------------------------------------------------

# Once you settle on the test cases, you need to perform the tests. 
# One way is to call the functions yourself
# and we have already used ```doctest``` to do this semi-automatically. 
# The latter approach is preferred because it does not have as much potential for human error. 
# An even better way is to use formal *unit testing* with the ```unittest``` module. 
# A *unit test* exercises just one isolated component of a program. 

# With the ```unittest``` module, we write what are called *test classes*
# from the class ```unittest.TestCase```. 
# The first test class tests the function ```above_freezing```.


import unittest
import temperature


class TestAboveFreezing(unittest.TestCase):
    """Tests for temperature.above_freezing."""

    def test_above_freezing_above(self):
        """Test a temperature that is above freezing."""

        expected = True
        actual = temperature.above_freezing(5.2)
        self.assertEqual(expected, actual,
            "The temperature is above freezing.")

    def test_above_freezing_below(self):
        """Test a temperature that is below freezing."""

        expected = False
        actual = temperature.above_freezing(-2)
        self.assertEqual(expected, actual,
            "The temperature is below freezing.")

    def test_above_freezing_at_zero(self):
        """Test a temperature that is at freezing."""

        expected = False
        actual = temperature.above_freezing(0)
        self.assertEqual(expected, actual,
            "The temperature is at the freezing mark.")

# unittest.main()


# Note that these tests are essentially a set of *method* definitions
# which return the tests of some assertions over the expected value of 
# some function calls. 
# Each test case follows this pattern:

# expected = << the value we expect will be returned >>
# actual = << call on the function being tested >>
# self.assertEqual(expected, actual, 
#     "Error message in case of failure.")


# To *assert* something is to claim that a statement is true;
# in this case, we assert that the value ``expected``` equals ```actual```. 
# At the bottom of the file, the command ```unittest.main()```
# executes every function with a name beginning with ```test```. 

# When the program above is executed, called ```test_above_freezing.py```, 
# the following output.

unittest.main()

# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s

# OK


# The first line of output has three dots, one for each test that was executed. 
# A dot indicates that the test was run successfully: the test case passed. 
# The remaining output states that three test cases ran in less than a milisecond
# and that all test cases passed. 

# If our faulty function named ```above_feeezing_v2``` were used instead, 
# as in ``````test_above_freezing_v2.py```, it would give the following output.

import temperature_v2 as temperature

unittest.main()


# .F.
# ======================================================================
# FAIL: test_above_freezing_at_zero (__main__.TestAboveFreezing)
# Test a temperature that is at freezing.
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "test_above_freezing.py", line 30, in test_above_freezing_at_zero
#     "The temperature is at the freezing mark.")
# AssertionError: False != True : The temperature is at the freezing mark.

# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s

# FAILED (failures=1)


# Instead of three dots, for three passes, 
# it gives two dots and one ```F```, 
# which states that one test *failed*. 
# Furthermore, it states which test failed, 
# and exactly what values triggered the failure. 



##################################################
## Case Study: Testing ```running_sum```
##################################################

# When testing ```above_freezing```, we tested a function 
# that involved only immutable types. 
# In this case study, we will learn how to test functions
# that involve mutable types, such as lists or dictionaries. 

# Suppose we need to write a function that modifies a list so that it 
# contains a running sum of the values in it. 
# For example, if the list is ```[1, 2, 3]```, 
# the list should be mutated so that the first value is ```1```,
# the second value is the sum of the first two numbers, ```1 + 2```, 
# and the third value is the sum of all three numbers. ```1 + 2 + 3```,
# so we expect that the list ```[1, 2, 3]``` 
# will be mutated to the list ```[1, 3, 6]```.

# Following the function design recipe, the following 
# function was designed, which appears in the file ```sums.py```. 



from typing import List

def running_sum(L: List[float]) -> None:
    """Modify L so that it contains the running sums of its original items.

    >>> L = [4, 0, 2, -5, 0]
    >>> running_sum(L)
    >>> L
    [4, 4, 6, 1, 1]
    """

    for i in range(len(L)):
        L[i] = L[i - 1] + L[i]


# Test it the old fashioned way.
L = [4, 0, 2, -5, 0]
running_sum(L)
L

# The structure of the function is unusual:
# Because there is no return statement, the function ```running_sum```
# returns ```None```. 
# Writing a test that determines whether ```None``` is returned will
# not reveal whether the function works correctly. 
# You need to check whether the list that was passed to the function 
# was mutated correctly. 
# To do this, the test case has to have three steps:
# 1. Create a variable that refers to a list.
# 2. Call the function, passing that variable to it.
# 3. Check whether the list that was passed to that function 
# was mutated correctly.

# Following these steps, we created the variable, ```L```, 
# that refers to the list ```[4, 0, 2, -5, 0]```, 
# we called ```running_sum(L)```, 
# and confirmaed that ```L``` now refers to ```[4, 4, 6, 1, 1]```. 

# Although this test case passes, 
# it doesn't guarantee that this function always works--in fact, 
# the function contains a bug. 
# In the next section, we will design a set of test cases that 
# thoroughly test this function and discover the bug. 

#--------------------------------------------------
### Choosing test cases for ```running_sum```
#--------------------------------------------------


# The function ```running_sum``` has one parameter, which is a ```List[float]```. 
# For our test cases, we have to decide on the size of the list 
# and the values of the elements of the list. 
# For size, we should test with the empty list, 
# a short list with one item,
# another list with two items (the shortest case where two numbers interact), 
# and a longer list with several items. 

# When passed either the empty list or a list of length one, 
# the modified list should be the same as the original. 

# When passed a two-number list, 
# the modified list should have the first number unchanged
# and the second number equal to the sum of the two numbers. 

# For longer lists, things get more interesting. 
# The values can be negative, positive or zero, 
# so the resulting values can be bigger than, less than, 
# or the same as they were originally. 
# We'll divide our tests of longer lists into four cases,
# all negative values, all positive values, 
# and a mix of negative, zero and positive values. 

# Test Case Description         |         List before       |      List After
# ------------------------------|---------------------------|-------------------------|
# Empty list                    |     ```[1]```             |  ```[1]```              |
# One-item list                 |     ```[5]```             |  ```[5]```              |
# Two-item list                 |    ```[2.5]```            | ```[2.5]```             |
# Multiple items, all negative  |    ```[-1,-5,-3,-4]```    | ```[-1, -6, -9, -13]``` |
# Multiple items, all zero      |    ```[0,0,0,0]```        | ```[0,0,0,0]```         | 
# Multiple items, all positive  |    ```[4,2,3,6]```        | ```[4, 6, 9, 15]```     |
# Multiple items, mixed         |    ```[4, 0, 2, -5, 0]``` | ```[4, 4, 6, 1, 1]```   |

# Now that we've decided on our test cases, 
# the next step is to implement them using ```unittest```. 
# The following unit tests are implemented in the script ```test_sums.py```.



import unittest
import sums as sums

class TestRunningSum(unittest.TestCase):
    """Tests for sums.running_sum."""

    def test_running_sum_empty(self):
        """Test an empty list."""

        argument = []
        expected = []
        sums.running_sum(argument)
        self.assertEqual(expected, argument, "The list is empty.")

    def test_running_sum_one_item(self):
        """Test a one-item list."""

        argument = [5]
        expected = [5]
        sums.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains one item.")

    def test_running_sum_two_items(self):
        """Test a two-item list."""

        argument = [2, 5]
        expected = [2, 7]
        sums.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains two items.")

    def test_running_sum_multi_negative(self):
        """Test a list of negative values."""

        argument = [-1, -5, -3, -4]
        expected = [-1, -6, -9, -13]
        sums.running_sum(argument)
        self.assertEqual(expected, argument,
            "The list contains only negative values.")

    def test_running_sum_multi_zeros(self):
        """Test a list of zeros."""

        argument = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        sums.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains only zeros.")

    def test_running_sum_multi_positive(self):
        """Test a list of positive values."""

        argument = [4, 2, 3, 6]
        expected = [4, 6, 9, 15]
        sums.running_sum(argument)
        self.assertEqual(expected, argument,
            "The list contains only positive values.")

    def test_running_sum_multi_mix(self):
        """Test a list containing mixture of negative values, zeros and
        positive values."""

        argument = [4, 0, 2, -5, 0]
        expected = [4, 4, 6, 1, 1]
        sums.running_sum(argument)
        self.assertEqual(expected, argument,
            "The list contains a mixture of negative values, zeros and"
                         + "positive values.")

# unittest.main()



# Next, we run the tests.
# We see that only three of the tests passed (indicated by the three dots)
# and four tests failed (four ```F```s). 

unittest.main()


# ..FF.FF
# ======================================================================
# FAIL: test_running_sum_multi_negative (__main__.TestRunningSum)
# Test a list of negative values.
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "test_running_sum.py", line 38, in test_running_sum_multi_negative
#     "The list contains only negative values.")
# AssertionError: Lists differ: [-1, -6, -9, -13] != [-5, -10, -13, -17]

# First differing element 0:
# -1
# -5

# - [-1, -6, -9, -13]
# + [-5, -10, -13, -17] : The list contains only negative values.

# ======================================================================
# FAIL: test_running_sum_multi_positive (__main__.TestRunningSum)
# Test a list of positive values.
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#     ...

# ======================================================================
# FAIL: test_running_sum_one_item (__main__.TestRunningSum)
# Test a one-item list.
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   ...
# ...
# ...
# ...

# ----------------------------------------------------------------------
# Ran 7 tests in 0.002s

# FAILED (failures=4)



# In the report card, we find that the three tests that passed
# include the case with the empty list, the list with several zeros
# and the list with a mixture of values, positive, nagative or zero. 


# To find the bug, let's start with the simplest case that failed:
# the single-item list.



# ======================================================================
# FAIL: test_running_sum_one_item (__main__.TestRunningSum)
# Test a one-item list.
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/campbell/pybook/gwpy2/Book/code/testdebug/test_running_sum.
#   py", line 21, in test_running_sum_one_item
#     self.assertEqual(expected, argument, "The list contains one item.")
# AssertionError: Lists differ: [5] != [10]
# First differing element 0:
# 5
# 10

# - [5]
# + [10] : The list contains one item.


# For this test, the list argument was ```[5]```. 
# After the function call, we expected the list to be ```[5]```
# but the list was mutated to become ```[10]```.
# Looking back at the function definition for ```running_sum```, 
# in the statement ```L[i] = L[i - 1] + L[i]```, 
# when ```i``` refers to zero, ```L[i - 1]``` refers to the last element of the list.
# The 5 was counted twice. 
# ```L[0]``` shouldn't be changed because 
# the running sum of ```L[0]``` is simply ```L[0]```. 

# So then, if the function is wrong, how did the other test cases pass?
# In each of those cases, ```L[-1] + L[0]``` produced the same value as ```L[0]```.
# Look at those test cases: in each one that passed `L[-1]```
# was either missing or zero.
# Interestingly, the error was hidden in one of the more complex test cases, 
# while it was exposed with one of the simoplest.

# To fix the problem, we can adjust the loop
# to start at element 1, 
# leaving element zero unchanged. 
# The script ```sums_v2.py``` implements this correction.


from typing import List

def running_sum(L: List[float]) -> None:
    """Modify L so that it contains the running sums of its original items.

    >>> L = [4, 0, 2, -5, 0]
    >>> running_sum(L)
    >>> L
    [4, 4, 6, 1, 1]
    """

    for i in range(1, len(L)):
        L[i] = L[i - 1] + L[i]
        
        
# Now we can test this version of our function
# with the test cases in ```test_sums_v2.py```. 
# We get the following result. 


import unittest
import sums_v2 as sums

class TestRunningSum(unittest.TestCase):
    """Tests for sums.running_sum."""

    def test_running_sum_empty(self):
        """Test an empty list."""

        argument = []
        expected = []
        sums.running_sum(argument)
        self.assertEqual(expected, argument, "The list is empty.")

    def test_running_sum_one_item(self):
        """Test a one-item list."""

        argument = [5]
        expected = [5]
        sums.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains one item.")

    def test_running_sum_two_items(self):
        """Test a two-item list."""

        argument = [2, 5]
        expected = [2, 7]
        sums.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains two items.")

    def test_running_sum_multi_negative(self):
        """Test a list of negative values."""

        argument = [-1, -5, -3, -4]
        expected = [-1, -6, -9, -13]
        sums.running_sum(argument)
        self.assertEqual(expected, argument,
            "The list contains only negative values.")

    def test_running_sum_multi_zeros(self):
        """Test a list of zeros."""

        argument = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        sums.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains only zeros.")

    def test_running_sum_multi_positive(self):
        """Test a list of positive values."""

        argument = [4, 2, 3, 6]
        expected = [4, 6, 9, 15]
        sums.running_sum(argument)
        self.assertEqual(expected, argument,
            "The list contains only positive values.")

    def test_running_sum_multi_mix(self):
        """Test a list containing mixture of negative values, zeros and
        positive values."""

        argument = [4, 0, 2, -5, 0]
        expected = [4, 4, 6, 1, 1]
        sums.running_sum(argument)
        self.assertEqual(expected, argument,
            "The list contains a mixture of negative values, zeros and"
                         + "positive values.")


unittest.main()

# .......
# ----------------------------------------------------------------------
# Ran 7 tests in 0.000s

# OK



# The tests passed. And we're done.





##################################################
# End
##################################################
