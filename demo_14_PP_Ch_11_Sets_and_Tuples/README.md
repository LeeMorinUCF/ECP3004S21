# PP_Ch_11_Set_Tuple_Dict

# Storing Data Using Other Collection Types

## Storing Data Using Sets


```python 
>>> vowels = {'a', 'e', 'i', 'o', 'u'}
>>> vowels
{'a', 'u', 'o', 'i', 'e'}

``` 

```python 
>>> vowels = {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
>>> vowels
{'u', 'o', 'i', 'e', 'a'}

``` 


```python 
>>> {'a', 'e', 'i', 'o', 'u'} == {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
True

``` 









```python 
>>> type(vowels)
<class 'set'>
>>> type({1, 2, 3})
<class 'set'>
>>> type({})
<class 'dict'>
>>> set()
set()
>>> type(set())
<class 'set'>

``` 

```python 
>>> set()
set()
``` 


```python 
>>> set([2, 3, 2, 5])
{2, 3, 5}
``` 


```python 
>>> set(2, 3, 5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set expected at most 1 arguments, got 3

``` 



```python 
>>> set([3, 5, 2])
{2, 3, 5}
>>> set([2, 3, 5, 5, 2, 3])    
{2, 3, 5}
``` 

```python 
>>> vowels = {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
>>> vowels
{'i', 'a', 'u', 'e', 'o'}
>>> set(vowels)
{'i', 'a', 'u', 'e', 'o'}
>>> set({5, 3, 1})
{1, 3, 5}

``` 


```python 
>>> set(range(5))
{0, 1, 2, 3, 4}
``` 


### Set Operations




```python 
>>> vowels = {'a', 'e', 'i', 'o', 'u'}
>>> vowels
{'o', 'u', 'a', 'e', 'i'}
>>> vowels.add('y')
>>> vowels
{'u', 'y', 'e', 'a', 'o', 'i'}

``` 




```python 
>>> ten = set(range(10))
>>> lows = {0, 1, 2, 3, 4}
>>> odds = {1, 3, 5, 7, 9}
>>> lows.add(9)
>>> lows
{0, 1, 2, 3, 4, 9}
>>> lows.difference(odds)
{0, 2, 4}
>>> lows.intersection(odds)
{1, 3, 9}
>>> lows.issubset(ten)
True
>>> lows.issuperset(odds)
False
>>> lows.remove(0)
>>> lows
{1, 2, 3, 4, 9}
>>> lows.symmetric_difference(odds)
{2, 4, 5, 7}
>>> lows.union(odds)
{1, 2, 3, 4, 5, 7, 9}
>>> lows.clear()
>>> lows
set()

``` 

```python 
>>> lows = set([0, 1, 2, 3, 4])
>>> odds = set([1, 3, 5, 7, 9])
>>> lows - odds            # Equivalent to lows.difference(odds)
{0, 2, 4}
>>> lows & odds            # Equivalent to lows.intersection(odds)
{1, 3}
>>> lows <= odds           # Equivalent to lows.issubset(odds)
False
>>> lows >= odds           # Equivalent to lows.issuperset(odds)
False
>>> lows | odds            # Equivalent to lows.union(odds)
{0, 1, 2, 3, 4, 5, 7, 9}
>>> lows ^ odds            # Equivalent to lows.symmetric_difference(odds)
{0, 2, 4, 5, 7, 9}

``` 

### Set Example: Arctic Birds



```python 
canada goose
canada goose
long-tailed jaeger
canada goose
snow goose
canada goose
long-tailed jaeger
canada goose
northern fulmar

``` 


```python 
from typing import Set, TextIO
from io import StringIO

def observe_birds(observations_file: TextIO) -> Set[str]:
    """Return a set of the bird species listed in observations_file, which has
    one bird species per line.

    >>> infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
    >>> birds = observe_birds(infile)
    >>> 'bird 1' in birds
    True
    >>> 'bird 2' in birds
    True
    >>> len(birds) == 2
    True
    """
    birds_observed = set()
    for line in observations_file:
        bird = line.strip()
        birds_observed.add(bird)

    return birds_observed

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    with open('observations.txt') as observations_file:
        print(observe_birds(observations_file))

``` 


```python 
>>> for species in birds_observed:
...     print(species)
... 
long-tailed jaeger
canada goose
northern fulmar
snow goose
``` 

### Set Contents Must Be Immutable


```python 
>>> S = set()
>>> L = [1, 2, 3]
>>> S.add(L)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'

``` 


## Storing Data Using Tuples


```python 
>>> rock = 'anthracite'
>>> rock[9]
'e'
>>> rock[0:3]
'ant'
>>> rock[-5:]
'acite'
>>> for character in rock[:5]:
...     print(character)
...

a
n
t
h
r

``` 

```python 
>>> bases = ('A', 'C', 'G', 'T')
>>> for base in bases:
...     print(base)
... 
A
C
G
T
``` 


```python 
>>> (8)   
8
>>> type((8))
<class 'int'>
>>> (8,)
(8,)
>>> type((8,))
<class 'tuple'>
>>> (5 + 3)
8
>>> (5 + 3,)
(8,)

``` 




```python 
>>> life = (['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0])
>>> life[0] = life[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: object does not support item assignment

``` 

```python 
>>> life = (['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0])
>>> life[0][1] = 80.0
>>> life
(['Canada', 80.0], ['United States', 75.5], ['Mexico', 72.0])

``` 


```python 
>>> canada = ['Canada', 76.5]
>>> usa = ['United States', 75.5]
>>> mexico = ['Mexico', 72.0]
>>> life = (canada, usa, mexico)
>>> mexico = ['Mexico', 72.5]
>>> life
(['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0])
>>> life[0][1] = 80.0
>>> canada
['Canada', 80.0]

``` 


### Assigning to Multiple Values Using Tuples


```python 
>>> (x, y) = (10, 20)
>>> x
10
>>> y
20
>>> 10, 20
(10, 20)
>>> x, y = 10, 20
>>> x
10
>>> y
20
>>> [[w, x], [[y], z]] = [{10, 20}, [(30,), 40]]
>>> w
10
>>> x
20
>>> y
30
>>> z
40
>>> s1 = 'first'
>>> s2 = 'second'
>>> s1, s2 = s2, s1
>>> s1
'second'
>>> s2
'first'

``` 




## Using the ```in``` Operator on Tuples and Sets



```python 
>>> odds = set([1, 3, 5, 7, 9])
>>> 9 in odds
True
>>> 8 in odds
False
>>> '9' in odds
False
>>> evens = (0, 2, 4, 6, 8)
>>> 4 in evens
True
>>> 11 in evens
False

``` 
