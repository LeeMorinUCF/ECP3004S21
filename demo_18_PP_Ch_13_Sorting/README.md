# Chapter 13: Searching and Sorting

Last day we talked about searching and one of the best algorithms 
for searching in a list was *binary search*, 
which depends on a *sorted* list. 
From the comparison of timing of the algorithms, 
we know that there was a substantial improvement in searching time
but whether the end-to-end computing time is shorter
depends on how efficiently we can sort a list. 
Today, we will learn a few ways to produce a sorted list
and compare how much computing time it takes. 

## Sorting

The following table in the file ```canfire.dat``` shows
the number of acres burned in forest fires
in Canada from 1918 to 1988. 
What were the worst years?

```python 
No. of acres burned in forest fires in CANADA (excl. Yukon & NWT) 1918-1988
                  563000 7590000 1708000
 2142000 3323000 6197000 1985000 1316000
 1824000  472000 1346000 6029000 2670000
 2094000 2464000 1009000 1475000  856000
 3027000 4271000 3126000 1115000 2691000
 4253000 1838000  828000 2403000  742000
 1017000  613000 3185000 2599000 2227000
  896000  975000 1358000  264000 1375000
 2016000  452000 3292000  538000 1471000
 9313000  864000  470000 2993000  521000
 1144000 2212000 2212000 2331000 2616000
 2445000 1927000  808000 1963000  898000
 2764000 2073000  500000 1740000 8592000
10856000 2818000 2284000 1419000 1328000
 1329000 1479000 3084000
```

One way to find out which years were the N worst years 
is to sort the list and then take the last N values. 

```python 
def find_largest(n: int, L: list) -> list:
    """Return the n largest values in L in order from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> find_largest(3, L)
    [4, 5, 7]
    """

    copy = sorted(L)
    return copy[-n:]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

``` 

This algorithm is short, clean, and easy to understand, 
but it relies on a bit of black magic. 
How *does* function ```sorted``` work 
(along with the method ```list.sort()```)? 
How efficient are these algorithms? 

Many sorting algorithms have been developed over the years. 
Broadly speaking, they can be divided into two categories:
those that are simple but inefficient
and those that are efficient but harder to understand and implement. 

Both of the simple sorting algorithms that we will study
keep track of data in two sections.
The section at the beginning is the set of values sorted so far.
The set at the end comprises the set of values that have yet to be sorted. 
Both of these algorithms work their way through the list, 
making the sorted section one unit longer on each iteration. 
Here is an outline of our code:

```python
i = 0 # The index of the first item in the list lst. lst[:i] is sorted.
while i != len(L):
    # Do something to incorporate L[i] into the sorted section.
    i = i + 1
```
Many Python programmers would use a ```for``` loop,
rather than incrementing ```i```. 
The important part that differs between algorithms 
is the ```Do something``` part.

### Selection Sort

*Selection sort* works by searching the unknown section 
for the smallest item and moving it into the index ```i```. 
For this algorithm to work, the items in the sorted section 
must all be smaller than those in the unsorted section. 



```python
i = 0 # The index of the first unknown item in the list lst. 

# lst[:i] is sorted and those items are smaller than those in lst[i:].
while i != len(L):
    # Find the index of the smallest item in L[i:]
    # Swap that smallest item with L[i]
    i = i + 1
```

In this algorithm, since we know that all of the unsorted items 
are larger than the sorted items, 
we always know where to put the next item: location ```i```. 
This works because we are selecting the items in order. 
On the first iteration, ```i``` is 0 and ```lst[0:]``` is the entire list. 
This means that on the first iteration, we take the smallest item and
move it to the front. 
On the second iteration, we take the second-smallest item
and move it into the second position. 

Let's start with this ```selection_sort``` function, 
written partly in English. 

```python 
def selection_sort(L: list) -> None:
    """Reorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0
    while i != len(L):
        # Find the index of the smallest item in L[i:]
        # Swap that smallest item with L[i]
        i = i + 1

``` 

We can replace the second comment with a single line of code.

```python 
def selection_sort(L: list) -> None:
    """Reorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0
    while i != len(L):
        # Find the index of the smallest item in L[i:]
        L[i], L[smallest] = L[smallest], L[i]
        i = i + 1

``` 
This uses the notation for multiple assignment with tuples.

Now all we have to do is find the index of the smallest item
in ```L[i:]```. 
This is complex enough (without cheating and using a built-in function)
that it's worth putting in a function of its own. 

```python 


def find_min(L: list, b: int) -> int:
    """Precondition: L[b:] is not empty.
    Return the index of the smallest value in L[b:].

    >>> find_min([3, -1, 7, 5], 0)
    1
    >>> find_min([3, -1, 7, 5], 1)
    1
    >>> find_min([3, -1, 7, 5], 2)
    3
    """

    smallest = b  # The index of the smallest so far.
    i = b + 1
    while i != len(L):
        if L[i] < L[smallest]:
            # We found a smaller item at L[i].
            smallest = i

        i = i + 1

    return smallest

def selection_sort(L: list) -> None:
    """Reorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0
    while i != len(L):
        smallest = find_min(L, i)
        L[i], L[smallest] = L[smallest], L[i]
        i = i + 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

``` 
Function ```find_min``` examines each item in ```L[b:]```, 
keeping track of the minimum so far in the variable ```smallest```. 
Whenever it finds a smaller value, it updates ```smallest```. 

As with searching, this sorting algorithm is complex enough that 
a few examples will not be enough to test all the corner cases. 
Here is our list of test cases:
- An empty list.
- A list of length 1.
- A list of length 2 (this is the shortest case in which items are moved)
- An already-sorted list.
- A list with all the same values.
- A list with duplicates. 

Here is our function with the expanded doctests:

```python
def selection_sort(L: list) -> None:
    """Reorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    >>> L = []
    >>> selection_sort(L)
    >>> L
    []
    >>> L = [1]
    >>> selection_sort(L)
    >>> L
    [1]
    >>> L = [2, 1]
    >>> selection_sort(L)
    >>> L
    [1, 2]
    >>> L = [1, 2]
    >>> selection_sort(L)
    >>> L
    [1, 2]
    >>> L = [3, 3, 3]
    >>> selection_sort(L)
    >>> L
    [3, 3, 3]
    >>> L = [-5, 3, 0, 3, -6, 2, 1, 1]
    >>> selection_sort(L)
    >>> L
    [-6, -5, 0, 1, 1, 2, 3, 3]
    """

    i = 0

    while i != len(L):
        smallest = find_min(L, i)
        L[i], L[smallest] = L[smallest], L[i]
        i = i + 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

```
As with binary search, the set of test cases takes up more space than the function itself. 
Eventually we will outgrow doctest, convenient as it may be,
and use another method of testing in Chapter 15: *Testing and Debugging*. 

### Insertion Sort

Like selection sort, *insertion sort* keeps a sorted section at the beginning of the list. 
Rather than scanning the remaining list for the next smallest item, 
it takes the next item in the list 
and inserts it in order in the sorted section. 


```python
i = 0 # The index of the first unknown item in the list lst. 

# lst[:i] is sorted.
while i != len(L):
    # Move the item at index i to where it belongs in lst[:i + i].
    i = i + 1
```

Note the ```i + 1``` where we move an item to lst[:i + i]. 
This is because the next item might be larger than all the rest
that have been sorted so far. 
If so, that item won't move. 

The outline of our function is:
```python 
def insertion_sort(L: list) -> None:
    """Reorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> insertion_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0
    while i != len(L):
        # Insert L[i] where it belongs in L[0:i+1].
        i = i + 1

``` 
This is the same starting point as for selection sort, 
except for the comment inside the loop. 
As with selection sort, we'll write a helper function to do the work. 


```python 


def insert(L: list, b: int) -> None:
    """Precondition: L[0:b] is already sorted.
    Insert L[b] where it belongs in L[0:b + 1].

    >>> L = [3, 4, -1, 7, 2, 5]
    >>> insert(L, 2)
    >>> L
    [-1, 3, 4, 7, 2, 5]
    >>> insert(L, 4)
    >>> L
    [-1, 2, 3, 4, 7, 5]
    """

    # Find where to insert L[b] by searching backwards from L[b]
    # for a smaller item.
    i = b
    while i != 0 and L[i - 1] >= L[b]:
        i = i - 1

    # Move L[b] to index i, shifting the following values to the right.
    value = L[b]
    del L[b]
    L.insert(i, value)

def insertion_sort(L: list) -> None:
    """Reorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> insertion_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0

    while i != len(L):
        insert(L, i)
        i = i + 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

``` 
How does this work?
This works by finding where ```L[b]``` belongs and then moving it. 
Where does it belong?
It belongs after every value that is less than or equal to this value
and before every value that is greater.


Note that we need the check ```i != 0``` in case ```L[b]``` 
is smaller than every value in ```L[:b]```. 


#### Performance

Now that we have two sorting algorithms
and both are easy to understand, 
we can decide which one to use based on how much time 
it takes to run them. 

```python 
import time
import random
from sorts import selection_sort
from sorts import insertion_sort

def built_in(L: list) -> None:
    """Call list.sort --- we need our own function to do this so that we can
    treat it as we treat our own sorts.
    """

    L.sort()

def print_times(L: list) -> None:
    """Print the number of milliseconds it takes for selection sort, insertion
    sort, and list.sort to run.
    """

    print(len(L), end='\t')
    for func in (selection_sort, insertion_sort, built_in):
        if func in (selection_sort, insertion_sort) and len(L) > 10000:
            continue

        L_copy = L[:]
        t1 = time.perf_counter()
        func(L_copy)
        t2 = time.perf_counter()
        print("{0:7.1f}".format((t2 - t1) * 1000.), end='\t')

    print()  # Print a newline.

for list_size in [10, 1000, 2000, 3000, 4000, 5000, 10000]:
    L = list(range(list_size))
    random.shuffle(L)
    print_times(L)

``` 

In the demo script, we will run this test to see how "fast" they are.

You will see that they are much slower than the built-in sorting function, 
since our algorithms are thousands of times slower. 

To analyze the computing time, think about what the algorithm does in the inner loop. 
On the first iteration of selection sort, the algorithm examines
*every* element in the list just to add one sorted item. 
On the second iteration, it re-examines all but one item. 
On successive iterations, it keeps wastefully re-examining the same items over and over again. 

The same can be said for the insertion sort algorithm, except in the other order.
It examines one item on the first iteration, 
two on the second, and so on. 
You might notice that insertion sort is *slightly* faster. 
This is because, on average, only half the values are being examined on each iteration. 
With selection sort, *every* value in the list needs to be re-examined. 


## More Efficient Sorting Algorithms

How can we get closer to the performance of ```list.sort```?


### A First Attempt

Consider this code:

```python 
import bisect

def bin_sort(values: list) -> list:
    """Return a sorted version of the values.  (This does not mutate values.)
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> bin_sort(L)
    [-1, 2, 3, 4, 5, 7]
    """
	
    result = []
    for v in values:
        bisect.insort_left(result, v)

    return result

``` 
This code uses ```bisect.insort_left``` to figure out where to put 
each value from the original list into a new list that is
kept in sorted order. 
It uses binary search to do this. 
Essentially, we can use this to speed up the time it takes to
insert values within a sorting algorithm. 


## Merge Sort: A Faster Sorting Algorithm

There are several well-known, fast sorting algorithms:
merge sort, quick sort and heap sort are the ones that 
computer science majors might study. 
Most of these involve techniques that we haven't learnt yet
but merge sort can be written to be more accessible. 
Merge sort is built on the idea that taking two sorted lists 
and merging them takes an amount of time that is
proportional to the number of items in those lists, 
rather than a multiple of the length of those lists.

### Merging Two Sorted Lists

Let's start with a pair of small lists. 
Given two sorted lists ```L1``` and ```L2```, 
we can produce a new sorted list by running along ```L1``` and ```L2```
and comparing pairs of elements. 

Here is the code for ```merge```:

```python 
def merge(L1: list, L2: list) -> list:
    """Merge sorted lists L1 and L2 into a new list and return that new list.
    >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """

    newL = []
    i1 = 0
    i2 = 0

    # For each pair of items L1[i1] and L2[i2], copy the smaller into newL.
    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 += 1
        else:
            newL.append(L2[i2])
            i2 += 1

    # Gather any leftover items from the two sections.
    # Note that one of them will be empty because of the loop condition.
    newL.extend(L1[i1:])
    newL.extend(L2[i2:])
    return newL

if __name__ == '__main__':
    import doctest
    doctest.testmod()

``` 
In this algorithm, ```i1``` and ```i2``` 
are the indices into ```L1``` and ```L2```, respectively:
in each iteration, we compare ```L1[i1]``` and ```L2[i2]```
and copy the smaller item to the resulting list. 
At the end of the loop, we have run out of the items 
in one of the two lists, and the two ```extend``` calls
will append the rest of the items to the result. 


### Merge Sort

Now, let's use this algorithm to sort a list. 
We'll start with the header for ```mergesort```. 


```python 
def mergesort(L: list) -> None:
    """Reorder the items in L from smallest to largest.
	
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> mergesort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

``` 
Function ```mergesort``` uses ```merge``` to do most of the work. 
Here is the algorithm, which creates and keeps track
of a list of lists:
- Take list ```L``` and make a list of one-item lists from it.
- As long as there are two lists left to merge, merge them,
and append the new list to the list of lists. 
The first step is straightforward: 

```python
# Make a list of 1-item lists so that we can start merging.
workspace = []
for i in range(len(L)):
    workspace.append([L[i]])

```
The second step is trickier. 
If we remove the two lists, 
then we'll run into the same problem we had with ```bin_sort```:
all the following lists will need to shift over, 
which takes time proportional to the number of lists. 
Instead, we'll keep track of the next lists to merge.

Here is a revised algorithm:
- Take list ```L``` and make a list of 1-item lists from it. 
- Start index ```i``` of at 0.
- As long as there are two lists (at indices ```i``` and ```i+1```), 
merge them, append the new list to the list of lists, 
and increment ```i``` by 2. 
Now translate this to python code. 


```python 
def mergesort(L: list) -> None:
    """Reorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> mergesort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    # Make a list of 1-item lists so that we can start merging.
    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])

    # The next two lists to merge are workspace[i] and workspace[i + 1].
    i = 0
    # As long as there are at least two more lists to merge, merge them.
    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        newL = merge(L1, L2)
        workspace.append(newL)
        i += 2

    # Copy the result back into L.
    if len(workspace) != 0:
        L[:] = workspace[-1][:]

``` 

Notice that since we're always making new lists, 
we need to copy the merged lists back into the parameter ```L```. 

### Merge Sort Analysis

As before, we can time this sorting algorithm
and compare it with the others.

```python 
import time
import random
from sorts import selection_sort
from sorts import insertion_sort
from sorts import mergesort


def built_in(L):
    """ (list) -> NoneType
    Call list.sort --- we need our own function to do this so that we can
    treat it as we treat our own sorts."""

    L.sort()


def print_times(L):
    """ (list) -> NoneType

    Print the number of milliseconds it takes for selection sort, insertion
    sort, and list.sort to run.
    """

    print(len(L), end='\t')
    for func in (selection_sort, insertion_sort, mergesort, built_in):
        if func in (selection_sort, insertion_sort) and len(L) > 10000:
            continue

        L_copy = L[:]
        t1 = time.perf_counter()
        func(L_copy)
        t2 = time.perf_counter()
        print("{0:7.1f}".format((t2 - t1) * 1000.), end='\t')
    print()  # Print a newline.

for list_size in [10, 1000, 2000, 3000, 4000, 5000, 10000]:
    L = list(range(list_size))
    random.shuffle(L)
    print_times(L)

``` 

When we run this comparison in the demo script, 
we'll see that ```mergesort``` is orders of magnitude faster
than either selection sort or insertion sort.
It's still not as fast as the built-in ```list.sort```
but at least it's computing time grows at the same rate, 
it just takes a fixed multiple of time to compute. 





