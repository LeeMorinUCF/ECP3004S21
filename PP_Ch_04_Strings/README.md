# PP_Ch_4_Strings

## Creating Strings of Characters


```python 
>>> 'Aristotle'
'Aristotle'
>>> "Isaac Newton"
'Isaac Newton'

``` 

```python 
>>> 'Charles Darwin"
  File "<stdin>", line 1
    'Charles Darwin"
                   ^
SyntaxError: EOL while scanning string literal

``` 



```python 
>>> ''
''
>>> ""
''

``` 

### Operations on Strings



```python 
>>> len('Albert Einstein')
15
>>> len('123!')
4
>>> len(' ')
1
>>> len('')
0

``` 



```python 
>>> 'Albert' + ' Einstein'
'Albert Einstein'

``` 

```python 
>>> "Alan Turing" + ''
'Alan Turing'
>>> "" + 'Grace Hopper'
'Grace Hopper'

``` 


```python 
>>> 'NH' + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly

``` 

```python 
>>> 9 + ' planets'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

``` 

```python 
>>> 'Four score and ' + str(7) + ' years ago'
'Four score and 7 years ago'

``` 

```python 
>>> int('0')
0
>>> int("11")
11
>>> int('-324')
-324
>>> float('-324')
-324.0
>>> float("56.34")
56.34

``` 

```python 
>>> int('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'a'
>>> float('b')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'b'
``` 


```python 
>>> 'AT' * 5
'ATATATATAT'
>>> 4 * '-'
'----'

``` 

```python 
>>> 'GC' * 0
''
>>> 'TATATATA' * -3
''

``` 


```python 
>>> sequence = 'ATTGTCCCCC'
>>> len(sequence)
10
>>> new_sequence = sequence + 'GGCCTCCTGC'
>>> new_sequence
'ATTGTCCCCCGGCCTCCTGC'
>>> new_sequence * 2
'ATTGTCCCCCGGCCTCCTGCATTGTCCCCCGGCCTCCTGC'
``` 



## using Special Characters in Strings


```python 
>>> 'that's not going to work'
  File "<stdin>", line 1
    'that's not going to work'
          ^
SyntaxError: invalid syntax

``` 


```python 
>>> "that's better"
"that's better"
>>> 'She said, "That is better."'
'She said, "That is better."'

``` 




```python 
>>> 'She said, "That' + "'" + 's hard to read."'
'She said, "That\'s hard to read."'

``` 



```python 
>>> len('\'')
1
>>> len('it\'s')
4

``` 

## Creating a Multiline String



```python 
>>> 'one
  File "<stdin>", line 1
    'one
       ^
SyntaxError: EOL while scanning string literal
``` 

```python 
>>> '''one
... two
... three'''
'one\ntwo\nthree'
``` 


## Printing Information


```python 
>>> print(1 + 1)
2
>>> print("The Latin 'Oryctolagus cuniculus' means 'domestic rabbit'.")
The Latin 'Oryctolagus cuniculus' means 'domestic rabbit'.

``` 

```python 
>>> print('In 1859, Charles Darwin revolutionized biology')      
In 1859, Charles Darwin revolutionized biology
>>> print('and our understanding of ourselves')      
and our understanding of ourselves
>>> print('by publishing "On the Origin of Species".')
by publishing "On the Origin of Species".

``` 

```python 
>>> print('one\ttwo\nthree\tfour')
one	two
three	four

``` 


```python 
>>> numbers = '''one
... two
... three'''
>>> numbers
'one\ntwo\nthree'
>>> print(numbers)
one
two
three

``` 



```python 
'''Should you want a string
that crosses multiple lines,
Use matched triple quotes.'''

``` 

```python 
>>> print(1, 2, 3)
1 2 3
>>>
``` 

```python 
>>> print()

>>> 
``` 

```python 
>>> print(1, 'two', 'three', 4.0)
1 two three 4.0
``` 


```python 
>>> radius = 5
>>> print("The diameter of the circle is", radius * 2, "cm.")
The diameter of the circle is 10 cm.

``` 



```python 
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
>>> print('a', 'b', 'c')  # The separator is a space by default
a b c
>>> print('a', 'b', 'c', sep=', ')
a, b, c
>>> print('a', 'b', 'c', sep=', ', end='')
a, b, c
>>>

``` 

```python 
def convert_to_celsius(fahrenheit: float) -> float:
    """ Return the number of Celsius degrees equivalent to fahrenheit degrees.

    >>> convert_to_celsius(75)
    23.88888888888889
    """

    return (fahrenheit - 32.0) * 5.0 / 9.0

print('80, 78.8, and 10.4 degrees Fahrenheit are equal to ', end='')
print(convert_to_celsius(80), end=', \n')
print(convert_to_celsius(78.8), end=', and ')
print(convert_to_celsius(10.4), end=' Celsius.\n')

``` 


## Getting Information from the Keyboard



```python 
>>> species = input()
Homo sapiens
>>> species
'Homo sapiens'
>>> population = input()
6973738433
>>> population
'6973738433'
>>> type(population)
<class 'str'>

``` 

```python 
>>> population = input()
6973738433
>>> population
'6973738433'
>>> population = int(population)
>>> population
6973738433
>>> population = population + 1
>>> population
6973738434

``` 

```python 
>>> population = int(input())
6973738433
>>> population = population + 1
6973738434

``` 

```python 
>>> species = input("Please enter a species: ") 
Please enter a species: Python curtus
>>> print(species)
Python curtus

``` 




## Exercises



```python 
>>> first = 'John'
>>> last = 'Doe'
>>> print(last + ', ' + first)
``` 

```python 
def repeat(s: str, n: int) -> str:
    """ Return s repeated n times; if n is negative, return the empty string.

    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)

    >>> repeat('no', -2)

    >>> repeat('yesnomaybe', 3)

    """

``` 

```python 
def total_length(s1: str, s2: str) -> int:
    """ Return the sum of the lengths of s1 and s2.

    >>> total_length('yes', 'no')
    5
    >>> total_length('yes', '')

    >>> total_length('YES!!!!', 'Noooooo')

    """

``` 




