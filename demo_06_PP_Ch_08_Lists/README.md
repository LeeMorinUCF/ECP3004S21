# Chapter 8: Storing Collections of Data Using Lists


## Storing and Accessing Data in Lists

A list is an ordered collection of zero or more objects. 

For example, this is a list of the number of whales seen per day
near the Coal Oil Point Natural Reserve in the two
weeks starting on February 24, 2008.

```python 
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> whales
[5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]

``` 

You can select a particular element of the list using square brackets. 


```python 
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> whales[0]
5
>>> whales[1]
4
>>> whales[12]
1
>>> whales[13]
3

``` 
Notice the relationship between the index numbers 0 to 13
and the corresponding values from the list. 

You can't select a value out of range...

```python 
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> whales[1001]
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
IndexError: list index out of range

``` 
...unless you reach in the negative direction...
```python 
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> whales[-1]
3
>>> whales[-2]
1
>>> whales[-14]
5
```
...but don't go too far backwards, either: 
```python 
>>> whales[-15]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

``` 
Like any other variable, you can assign individual elements to 
other variables. 
```python 
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> third = whales[2]
>>> print('Third day:', third)
Third day: 7

``` 


### The Empty List

Like the empty string, the empty list contains no elements, 

```python 
>>> whales = []
``` 
so all index numbers are out of range. 

```python 
>>> whales[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> whales[-1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
``` 


### Lists Are Heterogeneous

A list does not have to contain the same type of variables. 

```python 
>>> krypton = ['Krypton', 'Kr', -157.2, -153.4]
>>> krypton[1]
'Kr'
>>> krypton[2]
-157.2

``` 
For some programmers with experience in other languages, 
this is a strange possibility. 
The user has to be careful to rememeber or check for the types of elements
to avoid errors. 


## Type Annotations for Lists

In type contracts for functions, you can specify that the argument is a ```list```.

```python 
>>> def average(L: list) -> float:
...     """Return the average of the values in L.
...
...     >>> average([1.4, 1.6, 1.8, 2.0])
...     1.7
...     """

``` 

You can also explicitly state that the argument is a list *of floats*, 
using the *capital-L* ```List from the ```typing``` module.

```python 
>>> from typing import List
>>> def average(L: List[float]) -> float:
...     """Return the average of the values in L.
...
...     >>> average([1.4, 1.6, 1.8, 2.0])
...     1.7
...     """

``` 


## Modifying Lists

You cange the values of lists. That is, lists are *mutable*. 

```python 
>>> nobles = ['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']

``` 
Notice that ```'neon'``` is spelled incorrectly. 
You can change it by assigning a new value to that element. 


```python 
>>> nobles[1] = 'neon'
>>> nobles
['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']

``` 

The fact that you can do this illustrates that each element is assigned 
its own location in memory. 

Compare this to numbers and strings, which are *immutable*. 


```python 
>>> name = 'darwin'
>>> name[0] = 'D'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```


Methods that appear to change strings, actually create new ones. 


```python 
>>> name = 'Darwin'
>>> capitalized = name.upper()
>>> print(capitalized)
DARWIN
>>> print(name)
Darwin

``` 
Methods are similar to functions but are related to a cetain data type. 
We will loop back to them in Chapter 7. 


## Operations on Lists

Some operations, such as ```len``` apply to many data types.
Here are some others that apply to lists. 

```python 
>>> half_lives = [887.7, 24100.0, 6563.0, 14, 373300.0]
>>> len(half_lives)
5
>>> max(half_lives)
373300.0
>>> min(half_lives)
14
>>> sum(half_lives)
404864.7
>>> sorted(half_lives)
[14, 887.7, 6563.0, 24100.0, 373300.0]
>>> half_lives
[887.7, 24100.0, 6563.0, 14, 373300.0]

``` 
Some operators can be applied to lists:

```python 
>>> original = ['H', 'He', 'Li']
>>> final = original + ['Be']
>>> final
['H', 'He', 'Li', 'Be']

``` 
Notice that the binary operator ```+``` only works when the operands are of the same type.
A single string is not the same as a list with one element that is a single string.


```python 
>>> ['H', 'He', 'Li'] + 'Be'   
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "str") to list

``` 
The ```*``` operator works similarly, when compared to strings. 

```python 
>>> metals = ['Fe', 'Ni']
>>> metals * 3
['Fe', 'Ni', 'Fe', 'Ni', 'Fe', 'Ni']

``` 

You can use the ```del``` operator to *delete*
an element from a list. 

```python 
>>> metals = ['Fe', 'Ni']
>>> del metals[0]
>>> metals
['Ni']
``` 




### The ```in``` Operator on Lists

The ```in``` operator checks whether an object is an element of the list.
It returns a Boolean variable that can be used to execute conditional staements. 

```python 
>>> nobles = ['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']
>>> gas = input('Enter a gas: ')
Enter a gas: argon
>>> if gas in nobles:
...     print('{} is noble.'.format(gas))
...
argon is noble.
>>> gas = input('Enter a gas: ')
Enter a gas: nitrogen
>>> if gas in nobles:
...     print('{} is noble.'.format(gas))
...
>>>
``` 
It only checks for a single item. For example,

```python 
>>> [1, 2] in [0, 1, 2, 3]
False

``` 
but

```python 
>>> [1, 2] in [0, [1, 2], 3]
True
```
in which the smaller list ```[1, 2]``` is an element of the full list.


## Slicing Lists

Some geneticists study types of worm, C. elegans, and refer to 
them with 3-letter abbreviations. 

```python 
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']

``` 
We can take a *slice* of the list to retain selected values in a smaller list. 

```python 
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> useful_markers = celegans_phenotypes[0:4]
``` 
If you leave out the leading or trailing index number, 
it will slice either from the beginning or to the end of the list. 

```python 
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_phenotypes[:4]
['Emb', 'Him', 'Unc', 'Lon']
>>> celegans_phenotypes[4:]
['Dpy', 'Sma']

``` 
Leaving both limits blank slices the entire list. 

```python 
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_copy = celegans_phenotypes[:]
>>> celegans_phenotypes[5] = 'Lvl'
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> celegans_copy
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']

``` 
Notice that the command ```celegans_phenotypes[5] = 'Lvl'``` command
did not change ```celegans_copy```, which is a *clone* of the list. 
Since there is a copy, Python changes the location in memory 
for ```celegans_phenotypes[5] once it is changed. 
Meanwhile, ```celegans_phenotypes[5]``` still refers to the original location in memory. 



## Aliasing: What's in a Name?

Instead of slicing, you can create an *alias*, which is an alternative name for something. 
The outcome is different than above. 

```python 
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_alias = celegans_phenotypes
>>> celegans_phenotypes[5] = 'Lvl'
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> celegans_alias
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
``` 

Note that we dropped the slice ```[:]``` when we assigned the alias ```celegans_alias```. 
As a result, changes made to the original list are also made to the alias.
The index numbers of the alias still point to the same places in memory as the 
elements of the original list. 



### Mutable Parameters


Consider this example:
a function that returns a list after removing the last element. 

```python 
>>> def remove_last_item(L: list) -> list:
...     """Return list L with the last item removed.
...
...     Precondition: len(L) >= 0
...
...     >>> remove_last_item([1, 3, 2, 4])
...     [1, 3, 2]
...     """
...     del L[-1]
...     return L
...
>>>
``` 

Now use it with the following list. 

```python 
>>> celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> remove_last_item(celegans_markers)
['Emb', 'Him', 'Unc', 'Lon', 'Dpy']
>>> celegans_markers
['Emb', 'Him', 'Unc', 'Lon', 'Dpy']
``` 
Notice that the original list was altered:
the modifications applied to the same places in memory. 

In fact, for this function, you don't need the return statement to create the
alias. 
The function will change the list by accessing the memory locations directly. 

```python 
>>> def remove_last_item(L: list) -> None:
...     """Remove the last item from L.
...
...     Precondition: len(L) >= 0
...
...     >>> remove_last_item([1, 3, 2, 4])
...     """
...     del L[-1]
...
>>> celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> remove_last_item(celegans_markers)
>>> celegans_markers
['Emb', 'Him', 'Unc', 'Lon', 'Dpy']

``` 
If we want to restrict the type of the list, we could use the 
```typing``` module to specify the type as, say, ```float```. 
Since this function will work the same for lists of any type, 
we can explicity state that it applies to lists of ```Any``` type.

```python 
>>> from typing import List, Any
>>> def remove_last_item(L: List[Any]) -> None:
...     """Remove the last item from L.
...
...     Precondition: len(L) >= 0
...
...     >>> remove_last_item([1, 3, 2, 4])
...     """
...     del L[-1]

``` 


## List Methods


Methods are like functions that operate on specific kinds of objects (see Chapter 6). 
Here are some examples.

```python 
>>> colors = ['red', 'orange', 'green']                 
>>> colors.extend(['black', 'blue'])
>>> colors                             
['red', 'orange', 'green', 'black', 'blue']
>>> colors.append('purple')            
>>> colors
['red', 'orange', 'green', 'black', 'blue', 'purple']
>>> colors.insert(2, 'yellow')         
>>> colors
['red', 'orange', 'yellow', 'green', 'black', 'blue', 'purple']
>>> colors.remove('black')                              
>>> colors
['red', 'orange', 'yellow', 'green', 'blue', 'purple']

``` 
notice that these methods modify the list, instead of creating new lists. 
See the list on page 142 for a menu of methods to choose from. 


## Working in a List of Lists

An element of a list can be...another list. 

```python 
>>> life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]

``` 

Notice that each single element of the full list is a list in its own right. 


```python 
>>> life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
>>> life[0]
['Canada', 76.5]
>>> life[1]
['United States', 75.5]
>>> life[2]
['Mexico', 72.0]

``` 
To select elements of the individual lists within the full list, 
use a second pair of square brackets. 


```python 
>>> life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
>>> life[1]
['United States', 75.5]
>>> life[1][0]
'United States'
>>> life[1][1]
75.5
``` 

Each of the sublists can be assigned to new variables. 

```python 
>>> life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
>>> canada = life[0]
>>> canada
['Canada', 76.5]
>>> canada[0]
'Canada'
>>> canada[1]
76.5

``` 
As for a single list, this creates an alias for that list, 
unless you take a slice with ```[:]```.

```python 
>>> life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
>>> canada = life[0]
>>> canada[1] = 80.0
>>> canada
['Canada', 80.0]
>>> life
[['Canada', 80.0], ['United States', 75.5], ['Mexico', 72.0]]

``` 

### Where Did My List Go?

It is easy to forget that many list methods return ```None```
rather than creating and returning a new list. 

```python 
>>> colors = 'red orange yellow green blue purple'.split()
>>> colors
['red', 'orange', 'yellow', 'green', 'blue', 'purple']
>>> sorted_colors = colors.sort()
>>> print(sorted_colors)
None
>>> colors
['blue', 'green', 'orange', 'purple', 'red', 'yellow']

``` 
The new variable ```sorted_colors``` contains only the value ```None```, 
returned by the list method ```sort```. 
The ```sort``` operation is performed on the original list, 
on which the method is applied. 




## Exercises









### Exercise 7

```python 
def same_first_last(L: list) -> bool:
    """Precondition: len(L) >= 2

    Return True if and only if first item of the list is the same as the
    last.

    >>> same_first_last([3, 4, 2, 8, 3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])

    >>> same_first_last([4.0, 4.5])

    """

``` 

### Exercise 8

```python 
def is_longer(L1: list, L2: list) -> bool:
    """Return True if and only if the length of L1 is longer than the length
    of L2.

    >>> is_longer([1, 2, 3], [4, 5])
    True
    >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])

    >>> is_longer(['a', 'b', 'c'], [1, 2, 3]

    """

``` 




## Additional Code Snippets



```python 
>>> from multiplication_table import *
>>> print_table()
        1       2       3       4       5
1       1       2       3       4       5
2       2       4       6       8       10
3       3       6       9       12      15
4       4       8       12      16      20
5       5       10      15      20      25

``` 





```python 
>>> x = None
>>> x
>>> print(x)
None

``` 



```python 
>>> file = open("planets.txt", "w")

``` 

```python 
>>> half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
>>> i = 2
>>> i < len(half_lives)
True

>>> half_lives[i]
6537.0
>>> j = 5
>>> j < len(half_lives)
False
>>> half_lives[j]
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
IndexError: list index out of range

``` 



```python 
>>> sum(['a', 'b', 'c'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

``` 
