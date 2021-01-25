# Chapter 4: Working with Text

## Characters

In a language like Python, values are represented in binary digits, or "bits".

For each individual character or element of a ```string``` of characters, the values are actually stored in a sequence of, for example, 8 adjacent locations in memory. 
Characters are stored with 8 bits to generate the integers 0 to 127, which correspond to the characters in the following ASCII table:

<img src="Images/ASCII-Table.png" width="500"/>

These numbers 0-127 are represented in memory by an 8-bit binary sequence. 
In binary, numbers are represented as the sum of (either 1 or 0 times) 2 raised to the exponent in the positions 0-7. 
For example, the binary number 65, corresponding to the ASCII character "A" is ```10000010```. 
Note that the eight bits can generate numbers from 0-255. 
The character set is called UTF-8 contains all the ASCII characters plus another 128. 


## Creating Strings of Characters

In Python, text is represented as a string when a sequence
of characters is enclosed in single or double quotes. 

```python 
>>> 'Aristotle'
'Aristotle'
>>> "Isaac Newton"
'Isaac Newton'

``` 
The quotes have to match or the statement will be unfinished. 

```python 
>>> 'Charles Darwin"
  File "<stdin>", line 1
    'Charles Darwin"
                   ^
SyntaxError: EOL while scanning string literal

``` 
An empty string is created when the quotes contain no characters.


```python 
>>> ''
''
>>> ""
''

``` 

### Operations on Strings

Some functions are designed to operate on strings. 
The ```len``` function returns the length of the string
(and can be used on other data types, as well).

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
Several binary operators are also defined on strings. 
The ```+``` operator *concatenates* strings

```python 
>>> 'Albert' + ' Einstein'
'Albert Einstein'

``` 
Empty strings act like the number zero under addition. 
```python 
>>> "Alan Turing" + ''
'Alan Turing'
>>> "" + 'Grace Hopper'
'Grace Hopper'

``` 
But you can't add a number to a string:

```python 
>>> 'NH' + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly

``` 
Likewise in the other order:
```python 
>>> 9 + ' planets'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

``` 

The particular error depends on the type of the first argument. 

You can convert a number to a string by using the ```str```
function first. 
```python 
>>> 'Four score and ' + str(7) + ' years ago'
'Four score and 7 years ago'

``` 
Some strings can be converted to numbers:
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
but not all strings:
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

The multiplication operator works as you might guess
when used on strings,
```python 
>>> 'AT' * 5
'ATATATATAT'
>>> 4 * '-'
'----'

``` 
and multiplication of a string by zero gives the empty string, 
```python 
>>> 'GC' * 0
''
```
but so does multiplication by a negative number 
(strings of negative length are not defined).

```python
>>> 'TATATATA' * -3
''

``` 
Strings are values, so you can assign strings to variables

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
and you can perform string operations on these variables. 


## Using Special Characters in Strings

Quotes within strings can prematurely end the definition of a string,

```python 
>>> 'that's not going to work'
  File "<stdin>", line 1
    'that's not going to work'
          ^
SyntaxError: invalid syntax

``` 
and cause an error. 
Fix it by using different types of quotes. 


```python 
>>> "that's better"
"that's better"
>>> 'She said, "That is better."'
'She said, "That is better."'

``` 

It works regardless of whether the string begins
with single or double quotes.

```python 
>>> 'She said, "That' + "'" + 's hard to read."'
'She said, "That\'s hard to read."'

``` 
Notice the backslash combined with the single qoute: ```\'```, 
which is an *escape sequence* for the single quote. 
You can also use this to define a string containing quotes. 

```python 
>>> len('\'')
1
>>> len('it\'s')
4
``` 



## Creating a Multiline String

As with other commands, the string definition should complete on one line.


```python 
>>> 'one
  File "<stdin>", line 1
    'one
       ^
SyntaxError: EOL while scanning string literal
``` 

Otherwise, you can use triple double-quotes to span multiple lines.


```python 
>>> '''one
... two
... three'''
'one\ntwo\nthree'
``` 
Notice the ```\n``` escape sequence for *newline*. 



```python 
'''Should you want a string
that crosses multiple lines,
Use matched triple quotes.'''
``` 



## Printing Information

The ```print``` function does just what is advertised. 
It works for numbers as well as strings. 

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
Notice that the outer quotes are not printed.
It is understood that you want to print the contents of the string.

The ```\t``` escape sequence is equivalent to pressing the "Tab" key.

```python 
>>> print('one\ttwo\nthree\tfour')
one	two
three	four

``` 

When you define a multi-line string with triple-quotes,
the newline characters are automatically added, 
```python 
>>> numbers = '''one
... two
... three'''
>>> numbers
'one\ntwo\nthree'
```

but the ```print``` function executes the instruction, 
rather than printing the escape sequence.

```python
>>> print(numbers)
one
two
three

``` 

The ```print``` function takes multiple arguments and ... prints them.
```python 
>>> print(1, 2, 3)
1 2 3
>>>
``` 
If there are no arguments passed to ```print```, 
it prints the empty string.
```python 
>>> print()

>>> 
``` 

You can pass arguments of different types,
```python 
>>> print(1, 'two', 'three', 4.0)
1 two three 4.0
``` 
and perform calculations within those arguments.

```python 
>>> radius = 5
>>> print("The diameter of the circle is", radius * 2, "cm.")
The diameter of the circle is 10 cm.

``` 

By default, the arguments are separated by a space, 
as in the ```sep``` argument and ends with a newline, 
as in the ```end``` argument. 
If you want to change these, supply different values
to those arguments. 

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

You can use the ```print``` function to print 
formatted statements from the values returned from your functions. 

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

The ```input``` function takes input from the keyboard.

```python 
>>> species = input()
Homo sapiens
```
It assigns the value to the variable as if any expression
were passed to the assignment operator.

```python
>>> species
'Homo sapiens'
```

Regardless of the type, ```input``` always returns a string.
```python
>>> population = input()
6973738433
>>> population
'6973738433'
>>> type(population)
<class 'str'>

``` 
Once assigned to a variable, the value can be used like any other, 
except that you might convert it to a numeric type. 
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
To shorten the code, you can chain the ```input``` function
within the ```int``` function, which converts the number 
to integer format right away. 
```python 
>>> population = int(input())
6973738433
>>> population = population + 1
6973738434

``` 

The argument to the ```input``` function is a string that will appear
at the screen, prompting the user to enter something at the keyboard. 
```python 
>>> species = input("Please enter a species: ") 
Please enter a species: Python curtus
>>> print(species)
Python curtus
``` 




## Exercises

### Exercise 6

What is printed by this code?

```python 
>>> first = 'John'
>>> last = 'Doe'
>>> print(last + ', ' + first)
``` 

### Exercise 8

Complete the examples in the docstring and then write the body of the following function. 

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
### Exercise 9

Complete the examples in the docstring and then write the body of the following function. 


```python 
def total_length(s1: str, s2: str) -> int:
    """ Return the sum of the lengths of s1 and s2.

    >>> total_length('yes', 'no')
    5
    >>> total_length('yes', '')

    >>> total_length('YES!!!!', 'Noooooo')

    """

``` 


## Application: Text Analytics

Text analytics is one application of string manipulation to produce data for business analytics. 
In the supplementary textbook *Business Data Science* by Matt Taddy, Chapter 8 outlines the use of *Text as Data*. 
Although those examples are written in R, the explanation still applies. 

I supplement this with tools in Python by working through a set of examples written by 
Dhilip Subramanian, a Data Scientist and AI Enthusiast: 

[Text Mining in Python: Steps and Examples on the KDNuggets website](https://www.kdnuggets.com/2020/05/text-mining-python-steps-examples.html)
and 
[Text Mining in Python: Steps and Examples on Medium.com](https://www.medium.com/towards-artificial-intelligence/text-mining-in-python-steps-and-examples-78b3f8fd913b). 



A deeper analysis is conducted by 
Avinash Navlani on a training site called Datacamp: 

[Text Analytics for Beginners using NLTK]
(https://medium.com/towards-artificial-intelligence/text-mining-in-python-steps-and-examples-78b3f8fd913b)

There are many other examples, as this the capabilities have expanded significantly over the last several years. 

This form of analysis goes well beyond the toolkit we have so far. 
We will have to learn more about list of data and reading and writing files containing the data.
We will have to learn to use Python modules, such as the ```nltk``` module used here. 
Then we will have to learn to use modules that conduct statistical analysis of the form you would do in a course on econometrics. 

