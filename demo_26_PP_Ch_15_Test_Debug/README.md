
# Chapter 15: Testing and Debugging

Once you gain enough skill to make programs run without error, 
how do you know that the program is correct? 
In the *Function Design Recipe*, we make sure to provide examples
to test a function. 
Finding good test cases is a skill that you will develop over time. 

Professional programmers do not just test their code, 
they provide test cases so that other programmers can test the code for themselves,
which is immensely useful if any modifications are needed, 
many time zones away or long after you have moved on to another company. 

## Why Do You Need to Test? 

*Quality assurance*, or QA, is the process of checking whether 
software works correctly. 
It isn't a process that is done after production, 
as it might be in the manufacturing of physical goods. 
In software development, tests are built into the production of the product. 

There are several stages of a software development project. 
1. *Requirements* The customer specifies what the program needs to do and 
any constraints or deadlines. 
1. *Design* The software developers make a high-level plan for the software, 
which involves splitting the problem into smaller well-defined problems. 
1. *Coding* This is the most glamorous part but often takes less time than you might imagine. 
1. *Testing* This is the real work of making sure the program does what it is supposed to, 
in a variety of cases. 
1. *Deployment* This is when the software is released to customers
or used in a business process. 

You might notice that your computer occasionally needs to download and install upgrades. 
This means that the software is released with bugs or security vulnerabilities 
that are discovered through use. 
Some of these bugs are known about before the product is deployed
but might only inconvenience a small number of users,
so a manager makes a cost-benefit decision to release the software anyway. 
It'll never be perfect but if it were, it would be released long after the competition. 

The thing is, the later that problems are found, 
the more difficult or expensive it is to fix them. 
What is a developer to do? 
Provide test cases. 
This ensures that downstream users can detect problem, 
including new problems are created by the inevitable updates. 

Testing is one more job to do, 
that you may not think you have time for, but *testing saves time*. 
Without tests, you will waste many more hours attempting to track down
bugs that you should have tested out earlier. 



## Case Study: Testing ```above_freezing```

Many weeks ago, we designed a function to determine whether 
a temperature is above freezing. 

```python 
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

``` 

We ran some example calls using ```doctest```. 
But we're missing a test:
what happens if the temperature is zero? 
Consider the next version of this function. 



```python 
def above_freezing_v2(celsius: float) -> bool:
    """Return True iff temperature celsius degrees is above freezing.

    >>> above_freezing_v2(5.2)
    True
    >>> above_freezing_v2(-2)
    False
    """

    return celsius >= 0

``` 

Both of these functions produce the same value for all of the examples given. 
How do we settle a tie-breaker? 
We can find test cases for which each function produces different values. 

The temperature zero degrees celcius provides such a test case. 

```python 
>>> above_freezing(0)
False
>>> above_freezing_v2(0)
True

``` 

Cases like these are called *boundary cases* or *corner cases*, 
which represent the boundary across which the function returns different values. 
Boolean expressions are a good place to look for these
but it might also depend on the mathematics behind the problem at hand. 



### Testing ```above_freezing``` Using ```unittest```


Once you settle on the test cases, you need to perform the tests. 
One way is to call the functions yourself
and we have already used ```doctest``` to do this semi-automatically. 
The latter approach is preferred because it does not have as much potential for human error. 
An even better way is to use formal *unit testing* with the ```unittest``` module. 
A *unit test* exercises just one isolated component of a program. 

With the ```unittest``` module, we write what are called *test classes*
from the class ```unittest.TestCase```. 
The first test class tests the function ```above_freezing```.

```python 
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

unittest.main()

``` 

Note that these tests are essentially a set of *method* definitions
which return the tests of some assertions over the expected value of 
some function calls. 
Each test case follows this pattern:

```python
expected = << the value we expect will be returned >>
actual = << call on the function being tested >>
self.assertEqual(expected, actual, 
    "Error message in case of failure.")
```

To *assert* something is to claim that a statement is true;
in this case, we assert that the value ``expected``` equals ```actual```. 
At the bottom of the file, the command ```unittest.main()```
executes every function with a name beginning with ```test```. 

When the program above is executed, called ```test_above_freezing.py```, 
the following output.

```python 
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
``` 
The first line of output has three dots, one for each test that was executed. 
A dot indicates that the test was run successfully: the test case passed. 
The remaining output states that three test cases ran in less than a milisecond
and that all test cases passed. 

If our faulty function named ```above_feeezing_v2``` were used instead, 
as in ``````test_above_freezing_v2.py```, it would give the following output.


```python 
.F.
======================================================================
FAIL: test_above_freezing_at_zero (__main__.TestAboveFreezing)
Test a temperature that is at freezing.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_above_freezing.py", line 30, in test_above_freezing_at_zero
    "The temperature is at the freezing mark.")
AssertionError: False != True : The temperature is at the freezing mark.

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)

``` 

Instead of three dots, for three passes, 
it gives two dots and one ```F```, 
which states that one test *failed*. 
Furthermore, it states which test failed, 
and exactly what values triggered the failure. 

Let's compare ```unittest``` with ```doctest```. 

- For large suites of tests, which are useful for complex programs, 
it is nice to have the tesing code in a separate file, 
instead of an excessively long docstring. 
- In ```unittest```, each test case can be in a separate method, 
making the test cases independent of each other. 
In cotrast, the test cases in docstrings retain values in memory
from the previous function calls. 
- With each test case in a separate method, rather than in a docstring, 
we can instead write a docstring for each test case, 
so a future user knows what potential problem the test case is testing for. 
- The third argument in ```assertEqual``` is an error message that can be used to 
communicate information about the nature of the failure. 
With ```doctest```, there is no straightforward way to inform the user
after a failure. 



## Case Study: Testing ```running_sum```

When testing ```above_freezing```, we tested a function 
that involved only immutable types. 
In this case study, we will learn how to test functions
that involve mutable types, such as lists or dictionaries. 

Suppose we need to write a function that modifies a list so that it 
contains a running sum of the values in it. 
For example, if the list is ```[1, 2, 3]```, 
the list should be mutated so that the first value is ```1```,
the second value is the sum of the first two numbers, ```1 + 2```, 
and the third value is the sum of all three numbers. ```1 + 2 + 3```,
so we expect that the list ```[1, 2, 3]``` 
will be mutated to the list ```[1, 3, 6]```.

Following the function design recipe, the following 
function was designed, which appears in the file ```sums.py```. 


```python 
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

``` 

The structure of the function is unusual:
Because there is no return statement, the function ```running_sum```
returns ```None```. 
Writing a test that determines whether ```None``` is returned will
not reveal whether the function works correctly. 
You need to check whether the list that was passed to the function 
was mutated correctly. 
To do this, the test case has to have three steps:
1. Create a variable that refers to a list.
1. Call the function, passing that variable to it.
1. Check whether the list that was passed to that function 
was mutated correctly.

Following these steps, we created the variable, ```L```, 
that refers to the list ```[4, 0, 2, -5, 0]```, 
we called ```running_sum(L)```, 
and confirmaed that ```L``` now refers to ```[4, 4, 6, 1, 1]```. 

Although this test case passes, 
it doesn't guarantee that this function always works--in fact, 
the function contains a bug. 
In the next section, we will design a set of test cases that 
thoroughly test this function and discover the bug. 

### Choosing test cases for ```running_sum```


The function ```running_sum``` has one parameter, which is a ```List[float]```. 
For our test cases, we have to decide on the size of the list 
and the values of the elements of the list. 
For size, we should test with the empty list, 
a short list with one item,
another list with two items (the shortest case where two numbers interact), 
and a longer list with several items. 

When passed either the empty list or a list of length one, 
the modified list should be the same as the original. 

When passed a two-number list, 
the modified list should have the first number unchanged
and the second number equal to the sum of the two numbers. 

For longer lists, things get more interesting. 
The values can be negative, positive or zero, 
so the resulting values can be bigger than, less than, 
or the same as they were originally. 
We'll divide our tests of longer lists into four cases,
all negative values, all positive values, 
and a mix of negative, zero and positive values. 

Test Case Description         |         List before       |      List After
------------------------------|---------------------------|-------------------------|
Empty list                    |     ```[1]```             |  ```[1]```              |
One-item list                 |     ```[5]```             |  ```[5]```              |
Two-item list                 |    ```[2.5]```            | ```[2.5]```             |
Multiple items, all negative  |    ```[-1,-5,-3,-4]```    | ```[-1, -6, -9, -13]``` |
Multiple items, all zero      |    ```[0,0,0,0]```        | ```[0,0,0,0]```         | 
Multiple items, all positive  |    ```[4,2,3,6]```        | ```[4, 6, 9, 15]```     |
Multiple items, mixed         |    ```[4, 0, 2, -5, 0]``` | ```[4, 4, 6, 1, 1]```   |

Now that we've decided on our test cases, 
the next step is to implement them using ```unittest```. 
The following unit tests are implemented in the script ```test_sums.py```.


```python 
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

unittest.main()

``` 

Next, we run the tests.
We see that only three of the tests passed (indicated by the three dots)
and four tests failed (four ```F```s). 


```python 
..FF.FF
======================================================================
FAIL: test_running_sum_multi_negative (__main__.TestRunningSum)
Test a list of negative values.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_running_sum.py", line 38, in test_running_sum_multi_negative
    "The list contains only negative values.")
AssertionError: Lists differ: [-1, -6, -9, -13] != [-5, -10, -13, -17]

First differing element 0:
-1
-5

- [-1, -6, -9, -13]
+ [-5, -10, -13, -17] : The list contains only negative values.

======================================================================
FAIL: test_running_sum_multi_positive (__main__.TestRunningSum)
Test a list of positive values.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_running_sum.py", line 55, in test_running_sum_multi_positive
    "The list contains only positive values.")
AssertionError: Lists differ: [4, 6, 9, 15] != [10, 12, 15, 21]

First differing element 0:
4
10

- [4, 6, 9, 15]
+ [10, 12, 15, 21] : The list contains only positive values.

======================================================================
FAIL: test_running_sum_one_item (__main__.TestRunningSum)
Test a one-item list.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_running_sum.py", line 21, in test_running_sum_one_item
    self.assertEqual(expected, argument, "The list contains one item.")
AssertionError: Lists differ: [5] != [10]

First differing element 0:
5
10

- [5]
+ [10] : The list contains one item.

======================================================================
FAIL: test_running_sum_two_items (__main__.TestRunningSum)
Test a two-item list.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_running_sum.py", line 29, in test_running_sum_two_items
    self.assertEqual(expected, argument, "The list contains two items.")
AssertionError: Lists differ: [2, 7] != [7, 12]

First differing element 0:
2
7

- [2, 7]
+ [7, 12] : The list contains two items.

----------------------------------------------------------------------
Ran 7 tests in 0.002s

FAILED (failures=4)

``` 

In the report card, we find that the three tests that passed
include the case with the empty list, the list with several zeros
and the list with a mixture of values, positive, nagative or zero. 


To find the bug, let's start with the simplest case that failed:
the single-item list.


```python 
======================================================================
FAIL: test_running_sum_one_item (__main__.TestRunningSum)
Test a one-item list.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/campbell/pybook/gwpy2/Book/code/testdebug/test_running_sum.
  py", line 21, in test_running_sum_one_item
    self.assertEqual(expected, argument, "The list contains one item.")
AssertionError: Lists differ: [5] != [10]
First differing element 0:
5
10

- [5]
+ [10] : The list contains one item.
``` 

For this test, the list argument was ```[5]```. 
After the function call, we expected the list to be ```[5]```
but the list was mutated to become ```[10]```.
Looking back at the function definition for ```running_sum```, 
in the statement ```L[i] = L[i - 1] + L[i]```, 
when ```i``` refers to zero, ```L[i - 1]``` refers to the last element of the list.
The 5 was counted twice. 
```L[0]``` shouldn't be changed because 
the running sum of ```L[0]``` is simply ```L[0]```. 

So then, if the function is wrong, how did the other test cases pass?
In each of those cases, ```L[-1] + L[0]``` produced the same value as ```L[0]```.
Look at those test cases: in each one that passed `L[-1]```
was either missing or zero.
Interestingly, the error was hidden in one of the more complex test cases, 
while it was exposed with one of the simoplest.

To fix the problem, we can adjust the loop
to start at element 1, 
leaving element zero unchanged. 
The script ```sums_v2.py``` implements this correction.

```python 
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

``` 

Now we can test this version of our function
with the test cases in ```test_sums_v2.py```. 
We get the following result. 


```python 
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK

``` 

The tests passed. 
We now generalize the steps we took to find these test cases. 

## Choosing Test Cases

Having a set of tests that pass is good:
it shows that your program does what you expected
in the cases that you have thought of. 
However, for complex programs, there will be many situations
that do not occur to you. 
Tests can show the absence of specific bugs
but cannot show the absence of all bugs. 

It is important to make sure you have good *test coverage*. 
Here are some guidelines that you can follow
to come up with a thorough set of test cases. 

- *Think about size*
When a test involves a collection, such as a list, string, dictionary or file, 
do the following:
  - Test the empty collection
  - Test a collection with one item in it. 
  - Test a general case with several items. 
  - Test the smallest interesting cases, 
  such as sorting a list containing two values. 

- *Think about dichotomies*
A *dichotomy* is a contrast between two things. 
Examples of dichotomies are empty/full, even/odd, 
positive/negative, and alphabetic/nonalphabetic. 
If a function deals with two or more different categories or situations, 
test all of them. 

- *Think about boundaries*
If a function behaves differently around a boundary or threshold, 
test exactly on that boundary. 

- *Think about order* 
If a function behaves differently when the same elements are used 
in a different order, identify those orders and test each one of them. 
For the sorting example mentioned in an earlier chapter, 
you will want one list in order and another unordered. 


Following these guidelines, 
you will get better and better at detecting errors and
will commit fewer and fewer errors over time. 
You will become more conscious of the errors that can occur
and that is the whole point of focusing on quality.
The more you do it, 
the less likely it becomes for problems to arise. 

## Hunting Bugs

Bugs are discovered through testing or through program use, 
although the later is what good testing can avoid. 
Regardless of how they are discovered, 
tracking down and eliminating bugs is part of life for every programmer. 

Debugging a program is like diagnosing a medical condition. 
To find the cause, you start by working backward from the symptoms. 
Then you find a solution and test it again to make sure that
it solves the problem. 

At least that is how it is supposed to work. 
Many novice programmers attempt to debug their code 
by making arbitrary changes. 
Auto mechanics have a term for someone who makes similar changes: *parts changers*
These novice mechanics will order and change car parts in an attempt to solve a problem,
which often results in replacing working parts and revisiting the same problem. 
Programmers, on the other hand, do not have to order and pay for parts, 
so it is tempting to try to solve a problem without "paying the price"
to find out exactly what the problem is. 

Here are some guidelines for tracking down the cause of a problem:

1. *Make sure you know what the program is supposed to do.* 
Sometimes this means doing the calculation by hand to find the correct answer.
Sometimes the answer is in the documentation for a module. 

1. *Repeat the failure.*
You can debug problems only when they go wrong, 
so find a test case that makes the program fail reliably.
Once you find one, find a simpler test case, which might give
you better clues to solve the problem. 


1. *Divide and conquer.*
Once you have a test case that makes the program fail, 
find the first moment when something goes wrong. 
Printing a message such as ```print("Beginning Step 2.")```
or ```print("Completed Step 2.")``` helps you find out how far the program ran
(although the ```Traceback``` message often helps).
You could start by printing objects that are are inputs to the calculation. 
Then, change inputs to the calculation to start by troubleshooting a simpler case. 


1. *Make one change at a time.*
Test after each such change: rerun your program and reproduce the error.
Check whether the error still occurs or a new error appears. 
If you make more than one change, you won't know which change in the code
made a change to the error, if any remains. 

1. *Keep records.* 
Like any other scientist, you should keep records. 
Otherwise, you may not recall what tests you have run. 
This will help you organize your thoughts to tackle the problem
but it will also prove invaluable to tell your colleagues
when the time comes to seek help. 
Sometimes a fresh set of eyes can catch something you missed. 



## Exercises


### Exercise 1


```python 
from typing import List

def double_preceding(values: List[float]) -> None:
    """Replace each item in the list with twice the value of the
    preceding item, and replace the first item with 0.

    >>> L = [1, 2, 3]
    >>> double_preceding(L)
    >>> L
    [0, 2, 4]
    """


    if values != []:
        temp = values[0]
        values[0] = 0
        for i in range(1, len(values)):
            values[i] = 2 * temp
            temp = values[i]

``` 


### Exercise 5

```python 
def find_min_max(values: list):
    """Print the minimum and maximum value from values.
    """

    min = None
    max = None
    for value in values:
        if value > max:
            max = value
        if value < min:
            min = value

    print('The minimum value is {0}'.format(min))
    print('The maximum value is {0}'.format(max))

``` 


### Exercise 6


```python 
from typing import List

def average(values: List[float]) -> float:
    """Return the average of the numbers in values.  Some items in values are
    None, and they are not counted toward the average.

    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    """

    count = 0  # The number of values seen so far.
    total = 0  # The sum of the values seen so far.
    for value in values:
        if value is not None:
            total += value

        count += 1

    return total / count

if __name__ == '__main__':
    import doctest
    doctest.testmod()

``` 



```python 
>>> import test_average
>>> test_average.average([None, 30, 20])
16.666666666666668

``` 
