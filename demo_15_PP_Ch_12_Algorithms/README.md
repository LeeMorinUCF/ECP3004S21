# Chapter 12: Designing Algorithms

An *algorithm* is a set of steps that accomplishes a task. 
Each function in a program, as well as the program itself, 
is an algorithm written in a language such as Python.

Here, we will discuss the process of designing an algorithm, 
which is best done in a combination of English and mathematics
before it is translated into Python. 

The specific approach we will use is calle *top-down design*. 
Start by describing the solution in English 
and then mark staments that can be translated directly into Python.
Then rewrite the remaining statements until they can all be
translated into Python. 


## Searching for The Two Smallest Values

We will explore how to find the index of the two smallest numbers 
in an unsorted list, using three different approaches.

Consider the following list of the number of humpback whales 
sighted off the coast of British Columbia over ten years. 
It is easy to find the smallest value. 

```python 
>>> counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
>>> min(counts)
96
``` 

If we want to know the year in which this minimum value occurred, 
we can use the ```list.index``` method. 

```python 
>>> counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
>>> low = min(counts)
>>> counts.index(low)
6
``` 

Or, more succinctly:

```python 
>>> counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
>>> counts.index(min(counts))
6
``` 

Now what could we do if we wanted to find the *two* smallest values? 
There is no method to do this directly, 
so we have to design an algorithm. 
As with any other function, start with the header.

```python 
from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """

``` 


Now that we have defined the problem, 
let's consider the approaches we could take. 
There are three distinct algorithms that can achieve our goal
and we'll start with a high-level description of each. 
This is the first step in designing each of the algorithms.

- *Find, remove, find.* Find the index of the minimum, 
remove it from the list, and find the new minimum from the list.
Then, replace the first item and, if necessary, 
adjust the second index number to account for the first index. 

- *Sort, identify minimums, get indices.* Sort the list, 
get the two smallest numbers, and then find their index numbers
in the original list. 

- *Walk through the list.* Examine each value in that order, 
keep track of the two smallest values found so far, 
and update these values when a new smaller number is found. 

The first two algorithms mutate the list, either by removing an item or sorting. 
We need to put things back the way we found them. 
Notice that the second example in the docstring above
verifies that the list has not been modified. 


### Find, Remove, Find

Now let's write the first algorithm in words, in the form of comments.

```python 
from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """
    # Find the index of the minimum item in L
    # Remove that item from the list
    # Find the index of the new minimum item in the list
    # Put the smallest item back in the list
    # If necessary, adjust the second index
    # Return the two indices

``` 

Tackle the first line first. 
Calling ```help(list)``` we find no function that does exactly that. 
Now split that sentence into two:


```python 
def find_two_smallest(L):
    """ (see above) """

    # Get the minimum item in L            <-- This line is new
    # Find the index of that minimum item  <-- This line is new
    # Remove that item from the list
    # Find the index of the new minimum item in the list
    # Put the smallest item back in the list
    # If necessary, adjust the second index
    # Return the two indices

``` 

Now the first two sentences match Python functions and methods:
```min``` does the first and ```list.index``` does the second. 
The method ```list.remove``` will take care of the next line. 
The next sentence 
```Find the index of the new minimum item in the list``` 
is a repetition of the first two sentences with the new list. 
Add these commands under each line, 
keeping the comments there so that later users, including *future you*,
will understand the algorithm. 

```python 
def find_two_smallest(L):
    """ (see above) """

    # Find the index of the minimum and remove that item
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)

    # Find the index of the new minimum
    next_smallest = min(L)
    min2 = L.index(next_smallest)

    # Put the smallest item back in the list
    # If necessary, adjust the second index
    # Return the two indices

``` 
Now we need to replace the smallest item. 
Since removing a value changes the indices of the following items, 
we will need to add ```1``` to ```min2``` if the smallest item 
came before the second-smallest item.
Let's make that description more precise.


```python 
def find_two_smallest(L):
    """ (see above) """

    # Find the index of the minimum and remove that item
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)

    # Find the index of the new minimum
    next_smallest = min(L)
    min2 = L.index(next_smallest)

    # Put smallest back into L
    # Fix min2 in case it was affected by the removal and reinsertion:
    # If min1 comes before min2, add 1 to min2
    # Return the two indices

``` 

That's enough refinement to do it all in Python. 


```python 
from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """

    # Find the index of the minimum and remove that item
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)

    # Find the index of the new minimum
    next_smallest = min(L)
    min2 = L.index(next_smallest)

    # Put smallest back into L
    L.insert(min1, smallest)

    # Fix min2 in case it was affected by the removal and reinsertion:
    if min1 <= min2:
        min2 += 1

    return (min1, min2)

``` 

That seemed like a lot of thought and care, and it is, 
but this process is necessary to avoid problems later. 
The extra comments pay for themselves many times over. 
The goal is not to minimize the number of keystrokes
but to improve the odds of getting it right without undue frustration. 


### Sort, Identify Minimums, Get Indices

As above, let's start with one instruction per line. 

```python 
from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """

    # Sort a copy of L
    # Get the two smallest numbers
    # Find their indices in the original list L
    # Return the two indices

``` 

The first step is covered by the built-in function ```sorted```. 
This returns a copy of the list with the smallest items at the top. 
Notice that we are resisting the temptation to modify the list
with ```list.sorted```. 
The function ```sorted``` makes a copy without breaking a fundamental rule: 
never mutate the contents of parameters unless said so in the docstring. 

```python 
def find_two_smallest(L):
    """ (see above) """

    # Get a sorted copy of the list so that the two smallest items are at the
    # front
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]

    # Find their indices in the original list L
    # Return the two indices

``` 

Now we can find the indices and return them 
in the same way we did in find-remove-find.

```python 
from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """

    # Get a sorted copy of the list so that the two smallest items are at the
    # front
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]

    # Find the indices in the original list L
    min1 = L.index(smallest)
    min2 = L.index(next_smallest)

    return (min1, min2)

``` 

### Walk Through the List

Again, let's start with a description. 


```python 
from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """

    # Examine each value in the list in order
    # Keep track of the indices of the two smallest values found so far
    # Update the indices when a new smaller value is found
    # Return the two indices

``` 

Let's swap the order of the first two statements
because the second describes the entire process. 
Also, when we use a phrase like "for each" we think of iteration;
since the third line is part of the iteration, we'll indent it.


```python 
def find_two_smallest(L):
    """ (see above) """

    # Keep track of the indices of the two smallest values found so far
    # Examine each value in the list in order
    #     Update the indices when a new smaller value is found
    # Return the two indices

``` 

Since we're using a loops, we need to consider the three parts of a loop:
first, we initialize variables; 
second, we set up the loop condition;
and third, we write the loop body. 
Rewrite the first line. 

```python 
def find_two_smallest(L):
    """ (see above) """

    # Set min1 and min2 to the indices of the smallest and next-smallest
    # values at the beginning of L
    # Examine each value in the list in order
    #     Update the indices when a new smaller value is found
    # Return the two indices

``` 

Now we can turn the first line into code:

```python 
def find_two_smallest(L):
    """ (see above) """

    # Set min1 and min2 to the indices of the smallest and next-smallest
    # Values at the beginning of L
    if L[0] < L[1]:
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0

    # Examine each value in the list in order
    #     Update the indices when a new smaller value is found
    # Return the two indices

``` 
Note that we keep the English sentence in as a comment. 

Now we move to the loop. 
With loops, there are three choices:
- a ```for``` loop over the values,
- a ```for``` loop over the indices, or
- a ```while``` loop over the indices.

Since our goal is to find indices, 
and we are looking over the entire list, 
we should use a ```for``` loop over the values. 


```python 
def find_two_smallest(L):
    """ (see above) """

    # Set min1 and min2 to the indices of the smallest and next-smallest
    # values at the beginning of L
    if L[0] < L[1]:
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0

    # Examine each value in the list in order
    for i in range(2, len(values)):
    #     Update min1 and/or min2 when a new smaller value is found
    # Return the two indices

``` 

Now for the body of the loop. 
Consider the statement 
```Update min1 and/or min2 when a new smaller value is found```.
There are three possibilities:

- If ```L[i]``` is smaller than both ```min1``` or ```min2```, 
then this is the new smallest value. 
Now ```min1``` holds the second-smallest 
and ```min2``` holds the third-smallest value, 
which is no longer necessary. Update both of them. 

- If ```L[i]``` is larger than ```min1``` 
but smaller than ```min2```, 
then this is the new second-smallest value. 
Replace ```min2```.

- If ```L[i]``` is larger than both ```min1```  and ```min2```,
skip it. 

Replace the relevant comments with these more precise statements. 

```python 
def find_two_smallest(L):
    """ (see above) """
	
    # Set min1 and min2 to the indices of the smallest and next-smallest
    # values at the beginning of L
    if L[0] < L[1]:
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0

    # Examine each value in the list in order
    for i in range(2, len(L)):
    #
    #     L[i] is smaller than both min1 and min2, in between, or
    #     larger than both:
    #     If L[i] is smaller than min1 and min2, update them both
    #     If L[i] is in between, update min2
    #     If L[i] is larger than both min1 and min2, skip it
	
    return (min1, min2)

``` 

Now, we have a complete set of English statements 
that are easily translated into Python. 

```python 
from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """

    # Set min1 and min2 to the indices of the smallest and next-smallest
    # values at the beginning of L
    if L[0] < L[1]:
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0

    # Examine each value in the list in order
    for i in range(2, len(L)):
        # L[i] is smaller than both min1 and min2, in between, or
        # larger than both

        # New smallest?
        if L[i] < L[min1]:
            min2 = min1
            min1 = i

        # New second smallest?
        elif L[i] < L[min2]:
            min2 = i

    return (min1, min2)

``` 

There is no code necessary for the "larger than both" case. 




## Timing the Functions

With three options, we now have the luxury of deciding
which one is better. 


*Profiling* a program is the process of measuring 
how long it takes to run and how much memory it uses.
These measurements--time and space--are the fundamental concepts 
of the theoretical study of algorithms. 
Faster is better than slower 
but programs that need more memory than your computer can handle
are not useful. 
We will analyze our three functions to see how they perform.

We will use the data in the file ```sea_levels.txt```, 
which provides 1,400 monthly readings of air pressure 
in Darwin, Australia, from 1882 to 1998. 

The module ```time``` contains the functions relating to time. 
One of these function is ```perf_counter```, 
which returns a time in seconds.
We can call it before and after our code is run 
to find out how many seconds elapsed 
(and multiplying by 1,000 to convert to milliseconds). 

```python 
import time

t1 = time.perf_counter()

# Code to time goes here

t2 = time.perf_counter()
print('The code took {:.2f}ms'.format((t2 - t1) * 1000.))

``` 

Now, let's write a script that imports our three modules
and runs the algorithms to time them. 
The ```Callable[[List[float]], Any]``` part of the type contract
allows any type to be returned:
we only care about the time they take. 


```python 
import time
import find_remove_find5
import sort_then_find3
import walk_through7

from typing import Callable, List, Any

def time_find_two_smallest(find_func: Callable[[List[float]], Any],
                           lst: List[float]) -> float:
    """Return how many seconds find_func(lst) took to execute.
    """

    t1 = time.perf_counter()
    find_func(lst)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.0

if __name__ == '__main__':
    # Gather the sea level pressures
    sea_levels = []
    sea_levels_file = open('sea_levels.txt', 'r')
    for line in sea_levels_file:
        sea_levels.append(float(line))
    sea_levels_file.close()

    # Time each of the approaches
    find_remove_find_time = time_find_two_smallest(
        find_remove_find5.find_two_smallest, sea_levels)

    sort_get_minimums_time = time_find_two_smallest(
        sort_then_find3.find_two_smallest, sea_levels)

    walk_through_time = time_find_two_smallest(
        walk_through7.find_two_smallest, sea_levels)

    print('"Find, remove, find" took {:.2f}ms.'.format(find_remove_find_time))
    print('"Sort, get minimums" took {:.2f}ms.'.format(
        sort_get_minimums_time))
    print('"Walk through the list" took {:.2f}ms.'.format(walk_through_time))

``` 

Run this program to see the differences. 
```python 
"Find, remove, find" took 0.07ms.
"Sort, get minimums" took 0.13ms.
"Walk through the list" took 0.25ms.
```


These times are hardly noticeable for lists with thousands of elements
but, for large lists, the differences can be very large. 




