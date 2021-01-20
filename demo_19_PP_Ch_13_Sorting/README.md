# Chapter 13: Searching and Sorting

## Sorting



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


### Selection Sort


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


### Insertion Sort


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


#### Performance


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



## More Efficient Sorting Algorithms



### A First Attempt

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



## Merge Sort: A Faster Sorting Algorithm


### Merging Two Sorted Lists


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



### Merge Sort



```python 
def mergesort(L: list) -> None:
    """Reorder the items in L from smallest to largest.
	
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> mergesort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

``` 




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

### Merge Sort Analysis


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












## Additional Code Snippets








```python 
"""Test binary search."""

import unittest
from binary_search import binary_search

# The list to search with.
VALUES = [1, 3, 4, 4, 5, 7, 9, 10]


class TestBS(unittest.TestCase):
    def test_first(self):
        """Test a value at the beginning of the list."""

        expected = 0
        actual = binary_search(VALUES, 1)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

    def test_duplicate(self):
        """Test a duplicate value."""

        expected = 2
        actual = binary_search(VALUES, 4)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

    def test_middle(self):
        """Test searching for the middle value."""

        expected = 4
        actual = binary_search(VALUES, 5)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

    def test_last(self):
        """Test searching for the last value."""

        expected = 7
        actual = binary_search(VALUES, 10)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

    def test_missing_start(self):
        """Test searching for a missing value at the start."""

        expected = -1
        actual = binary_search(VALUES, -3)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

    def test_missing_middle(self):
        """Test searching for a missing value in the middle."""

        expected = -1
        actual = binary_search(VALUES, 2)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

    def test_missing_end(self):
        """Test searching for a missing value at the end."""

        expected = -1
        actual = binary_search(VALUES, 11)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

if __name__ == '__main__':
    unittest.main()

``` 

```python 
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

``` 


```python 
import bisect

def bin_sort(values):
    """Sort values in place.  THIS VERSION IS FLAWED"""
    for i in range(1, len(values)):
        bisect.insort_left(values, values[i], 0, i)

``` 

```python 
>>> from binsort_broken import bin_sort
>>> tests = [ [], [1], [1, 2], [2, 1] ]
>>> for t in tests:
...     print t, '->',
...     bin_sort(t)
...     print t
... 
[] -> []
[1] -> [1]
[1, 2] -> [1, 2, 2]
[2, 1] -> [1, 2, 1]

``` 

```python 
def merge(L1, L2):
    """ (list, list) -> list

    Merge sorted lists L1 and L2 into a new list and return that new list.
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


def mergesort(L):
    """ (list) -> NoneType

    Sort L in increasing order.
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


if __name__ == '__main__':

    L = []
    print "befor", L
    mergesort(L)
    print "after", L

    L = [1]
    print "befor", L
    mergesort(L)
    print "after", L

    L = [5, 4, 2, 3, 6, 1]
    print "befor", L
    mergesort(L)
    print "after", L

``` 


```python 
# Make a list of 1-item lists so that we can start merging.
workspace = []
for i in range(len(L)):
    workspace.append([L[i]])

``` 

```python 
from ms import mergesort, merge
import nose

def run_mergesort(original, expected):
    """Sort list original and compare it to list expected."""
    mergesort(original)
    assert original == expected

def run_merge(L1, L2, expected):
    """Merge list original[b1:e1] with original[b2:e2] and compare it to list
    expected."""
    result = merge(L1, L2)
    assert result == expected
    
def test_merge_empty():
    """Test merging a 0-item list."""
    run_merge([], [], [])

def test_merge_one():
    """Test merging a 1-item list and a 1-item list."""
    run_merge([2], [1], [1, 2])

def test_merge_one_two():
    """Test merging a 2-item list and a 1-item list."""
    L = [1, 3, 2]
    run_merge([1, 3], [2], [1, 2, 3])

def test_merge_two_two():
    """Test merging a 2-item list and a 2-item list."""
    run_merge([1, 3], [2, 4], [1, 2, 3, 4])

def test_merge_two_two_same():
    """Test merging a 2-item list and a 2-item list where they have common
    elements."""
    run_merge([1, 3], [1, 3], [1, 1, 3, 3])

def test_empty():
    """Test sorting empty list."""
    run_mergesort([], [])

def test_one():
    """Test sorting a list of one value."""
    run_mergesort([1], [1])

def test_two_ordered():
    """Test sorting an already-sorted list of two values."""
    run_mergesort([1, 2], [1, 2])

def test_two_reversed():
    """Test sorting a reverse-ordered list of two values."""
    run_mergesort([2, 1], [1, 2])

def test_three_identical():
    """Test sorting a list of three equal values."""
    run_mergesort([3, 3, 3], [3, 3, 3])

def test_three_split():
    """Test sorting a list with an odd value out."""
    run_mergesort([3, 0, 3], [0, 3, 3])

if __name__ == '__main__':
    nose.runmodule()

``` 

```python 
def merge(L1, L2):
    """ (list, list) -> list

    Merge sorted lists L1 and L2 into a new list and return that new list.

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


def mergesort(L):
    """ (list) -> NoneType

    Reorder the items in L from smallest to largest.

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


if __name__ == '__main__':

    L = []
    print("before", L)
    mergesort(L)
    print("after", L)

    L = [1]
    print("before", L)
    mergesort(L)
    print("after", L)

    L = [5, 4, 2, 3, 6, 1]
    print("before", L)
    mergesort(L)
    print("after", L)

``` 


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

```


```
# from sort4 import selection_sort
# import unittest


# class TestSelectionSort(unittest.TestCase):

#     def test_empty(self):
#         '''Test sorting empty list.'''

#         L = []
#         expected = []
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

#     def test_one(self):
#         '''Test sorting a list of one value.'''

#         L = [1]
#         expected = [1]
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

#     def test_two_ordered(self):
#         '''Test sorting an already-sorted list of two values.'''

#         L = [1, 2]
#         expected = [1, 2]
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

#     def test_two_reversed(self):
#         '''Test sorting a reverse-ordered list of two values.'''

#         L = [2, 1]
#         expected = [1, 2]
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

#     def test_three_identical(self):
#         '''Test sorting a list of three equal values.'''

#         L = [3, 3, 3]
#         expected = [3, 3, 3]
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

#     def test_three_split(self):
#         '''Test sorting a list with one number different.'''

#         L = [3, 0, 3]
#         expected = [0, 3, 3]
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

#     def test_several(self):
#         '''Test sorting a list with several values, some duplicated.'''

#         L = [-5, 3, 0, 3, -6, 2, 1, 1]
#         expected = [-6, -5, 0, 1, 1, 2, 3, 3]
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

# if __name__ == '__main__':
#     unittest.main()

``` 

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

if __name__ == '__main__':
    import doctest
    doctest.testmod()

``` 
