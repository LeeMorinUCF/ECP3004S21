# PP_Ch_8_Lists

# Storing Collections of Data Using Lists


## Storing and Accessing Data in Lists


```python 
>>> # Number of whales seen per day
>>> [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]

``` 


```python 
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> whales
[5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]

``` 


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

```python 
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> whales[1001]
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
IndexError: list index out of range

``` 

```python 
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> whales[-1]
3
>>> whales[-2]
1
>>> whales[-14]
5
>>> whales[-15]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

``` 

```python 
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> third = whales[2]
>>> print('Third day:', third)
Third day: 7

``` 


### The Empty List

```python 
>>> whales = []


``` 

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

```python 
>>> krypton = ['Krypton', 'Kr', -157.2, -153.4]
>>> krypton[1]
'Kr'
>>> krypton[2]
-157.2

``` 


## Type Annotations for Lists



```python 
>>> def average(L: list) -> float:
...     """Return the average of the values in L.
...
...     >>> average([1.4, 1.6, 1.8, 2.0])
...     1.7
...     """

``` 

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


```python 
>>> nobles = ['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']

``` 


```python 
>>> name = 'Darwin'
>>> capitalized = name.upper()
>>> print(capitalized)
DARWIN
>>> print(name)
Darwin

``` 


## Operations on Lists



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


```python 
>>> original = ['H', 'He', 'Li']
>>> final = original + ['Be']
>>> final
['H', 'He', 'Li', 'Be']

``` 



```python 
>>> ['H', 'He', 'Li'] + 'Be'   
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "str") to list

``` 


```python 
>>> metals = ['Fe', 'Ni']
>>> metals * 3
['Fe', 'Ni', 'Fe', 'Ni', 'Fe', 'Ni']

``` 


```python 
>>> metals = ['Fe', 'Ni']
>>> del metals[0]
>>> metals
['Ni']
``` 




### The ```in``` Operator on Lists

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


```python 
>>> [1, 2] in [0, 1, 2, 3]
False

``` 



## Slicing Lists



```python 
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']

``` 

```python 
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> useful_markers = celegans_phenotypes[0:4]
``` 

```python 
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_phenotypes[:4]
['Emb', 'Him', 'Unc', 'Lon']
>>> celegans_phenotypes[4:]
['Dpy', 'Sma']

``` 

```python 
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_copy = celegans_phenotypes[:]
>>> celegans_phenotypes[5] = 'Lvl'
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> celegans_copy
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']

``` 




## Aliasing: What's in a Name?



```python 
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_alias = celegans_phenotypes
>>> celegans_phenotypes[5] = 'Lvl'
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> celegans_alias
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']

``` 




### Mutable Parameters




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

```python 
>>> celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> remove_last_item(celegans_markers)
['Emb', 'Him', 'Unc', 'Lon', 'Dpy']
>>> celegans_markers
['Emb', 'Him', 'Unc', 'Lon', 'Dpy']
``` 


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

## Working in a List of Lists


```python 
>>> life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]

``` 




```python 
>>> life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
>>> life[0]
['Canada', 76.5]
>>> life[1]
['United States', 75.5]
>>> life[2]
['Mexico', 72.0]

``` 



```python 
>>> life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
>>> life[1]
['United States', 75.5]
>>> life[1][0]
'United States'
>>> life[1][1]
75.5

``` 



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

```python 
>>> life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
>>> canada = life[0]
>>> canada[1] = 80.0
>>> canada
['Canada', 80.0]
>>> life
[['Canada', 80.0], ['United States', 75.5], ['Mexico', 72.0]]

``` 



## Exercises







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
>>> nobles[1] = 'neon'
>>> nobles
['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']

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
