# PP_Ch_7_Methods



```python 
>>> ('TTA' + 'G' * 3).count('T')
2

``` 

```python 
def total_occurrences(s1: str, s2: str, ch: str) -> int:
    """Precondition: len(ch) == 1

    Return the total number of times that ch occurs in s1 and s2.

    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')

    >>> total_occurrences('green', 'purple', 'b')

    """

``` 

```python 
>>> 'Pi rounded to {} decimal places is {:.3f}.'.format(3, my_pi)
'Pi rounded to 3 decimal places is 3.142.'
``` 

```python 
>>> my_pi = 3.14159                                         
>>> 'Pi rounded to {0} decimal places is {1:.2f}.'.format(2, my_pi)
'Pi rounded to 2 decimal places is 3.14.'
>>> 'Pi rounded to {0} decimal places is {1:.3f}.'.format(3, my_pi)
'Pi rounded to 3 decimal places is 3.142.'
``` 

```python 
>>> import math
>>> math.sqrt.__doc__
'sqrt(x)\n\nReturn the square root of x.'
>>> print(math.sqrt.__doc__)
sqrt(x)

Return the square root of x.
>>> help(math.sqrt)
Help on built-in function sqrt in module math:

sqrt(...)
    sqrt(x)

    Return the square root of x.

``` 

```python 
>>> help(0)
Help on int object:

class int(object)
 |  int(x=0) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 ...

``` 

```python 
Help on class int in module builtins:

class int(object)
...
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __gt__(self, value, /)
 |      Return self>value.

``` 

```python 
>>> abs(-3)
3
>>> (-3).__abs__()
3
>>> -3 .__abs__()
-3
>>> -(3 .__abs__())
-3
>>> (-3) .__abs__()
3
>>> 3 + 5
8
>>> 3 .__add__(5)
8
>>> 3 > 5
False
>>> 3 .__gt__(5)
False
>>> 5 > 3
True
>>> 5 .__gt__(3)
True

``` 

```python 
>>> import math
>>> help(math.sqrt)
Help on built-in function sqrt in module math:

sqrt(...)
    sqrt(x)

    Return the square root of x.

``` 

```python 
>>> 'browning'.capitalize()
'Browning'
>>> 'Sonnet 43'.center(26)
'        Sonnet 43         '
>>> 'How do I love thee?  Let me count the ways.'.count('the')
2

``` 

```python 
>>> '"{0}" is derived from "{1}"'.format('none', 'no one')
'"none" is derived from "no one"'
>>> '"{0}" is derived from the {1} "{2}"'.format('Etymology', 'Greek',
...                                              'ethos')
'"Etymology" is derived from the Greek "ethos"'
>>> '"{0}" is derived from the {2} "{1}"'.format('December', 'decem', 'Latin')
'"December" is derived from the Latin "decem"'

``` 

```python 
>>> compound = '     \n  Methyl \n butanol   \n'
>>> compound.lstrip()
'Methyl \n butanol   \n'
>>> compound.rstrip()
'     \n  Methyl \n butanol'
>>> compound.strip()
'Methyl \n butanol'

``` 

```python 
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return key in self.

 [Lots of other names with leading and trailing underscores not shown here.]

 |  capitalize(...)
 |      S.capitalize() -> str
 |
 |      Return a capitalized version of S, i.e. make the first character
 |      have upper case and the rest lower case.
 |
 |  casefold(...)
 |      S.casefold() -> str
 |
 |      Return a version of S suitable for caseless comparisons.
 |
 |  center(...)
 |      S.center(width[, fillchar]) -> str
 |
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.

[There are many more of these as well.]

``` 

```python 
 |  str(object[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object.

``` 

```python 
>>> help(str.lower)
Help on method_descriptor:

lower(...)
    S.lower() -> str

    Return a copy of the string S converted to lowercase.

``` 

```python 
>>> str.capitalize('browning')
'Browning'

``` 

```python 
>>> str.center('Sonnet 43', 26)
'        Sonnet 43         '
>>> str.count('How do I love thee?  Let me count the ways.', 'the')
2

``` 

```python 
>>> 'TTA' + 'GGG'
'TTAGGG'
>>> 'TTA'.__add__('GGG')
'TTAGGG'

``` 

