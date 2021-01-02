# PP_Ch_5_Boolean

## A Boolean Type

### Boolean Operators


```python 
>>> not True
False
>>> not False
True

``` 

```python 
>>> True and True
True
>>> False and False
False
>>> True and False
False
>>> False and True
False

``` 

```python 
>>> True or True
True
>>> False or False
False
>>> True or False
True
>>> False or True
True

``` 

```python 
>>> cold = True
>>> windy = False
>>> (not cold) and windy
False
>>> not (cold and windy)
True

``` 



#### Building an Exclusive ```or``` Expression


```python 
>>> b1 = False
>>> b2 = False
>>> (b1 and not b2) or (b2 and not b1)
False
>>> b1 = False
>>> b2 = True
>>> (b1 and not b2) or (b2 and not b1)
True
>>> b1 = True
>>> b2 = False
>>> (b1 and not b2) or (b2 and not b1)
True
>>> b1 = True
>>> b2 = True
>>> (b1 and not b2) or (b2 and not b1)
False

``` 


### Relational Operators


```python 
>>> 45 > 34
True
>>> 45 > 79
False
>>> 45 < 79
True
>>> 45 < 34
False
``` 

```python 
>>> 23.1 >= 23
True
>>> 23.1 >= 23.1
True
>>> 23.1 <= 23.1
True
>>> 23.1 <= 23
False

``` 

```python 
>>> 67.3 == 87
False
>>> 67.3 == 67
False
>>> 67.0 == 67
True
>>> 67.0 != 67
False
>>> 67.0 != 23
True
``` 

```python 
>>> def is_positive(x: float) -> bool:
...     """Return True iff x is positive.
...
...     >>> is_positive(3)
...     True
...     >>> is_positive(-4.6)
...     False
...     """
...     return x > 0
...
>>> is_positive(3)
True
>>> is_positive(-4.6)
False
>>> is_positive(0)
False

``` 


### Combining Comparisons


```python 
>>> x = 2
>>> y = 5
>>> z = 7
>>> x < y and y < z
True

``` 

```python 
>>> x = 5
>>> y = 10
>>> z = 20
>>> (x < y) and (y < z)
True

``` 

```python 
>>> x = 3
>>> (1 < x) and (x <= 5)
True
>>> x = 7
>>> (1 < x) and (x <= 5)
False

``` 


```python 
>>> x = 3
>>> 1 < x <= 5
True

``` 

```python 
>>> 3 < 5 != True
True
>>> 3 < 5 != False
True

``` 

#### Using Numbers and Strings with Boolean Operators

```python 
>>> not 0
True
>>> not 1
False
>>> not 34.2
False
>>> not -87
False

``` 

```python 
>>> not ''
True
>>> not 'bad'
False

``` 



### Short Circuit Evaluation


```python 
>>> 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

``` 

```python 
>>> (2 < 3) or (1 / 0)
True

``` 




### Comparing Strings


```python 
>>> 'A' < 'a'
True
>>> 'A' > 'z'
False
>>> 'abc' < 'abd'
True
>>> 'abc' < 'abcd'
True

``` 

```python 
>>> 'Jan' in '01 Jan 1838'
True
>>> 'Feb' in '01 Jan 1838'
False
>>> date = input('Enter a date in the format DD MTH YYYY: ')
Enter a date in the format DD MTH YYYY: 24 Feb 2013
>>> 'Jan' in date
False
>>> date = input('Enter a date in the format DD MTH YYYY: ')
Enter a date in the format DD MTH YYYY: 03 Jan 2002
>>> 'Jan' in date
True
>>> 'a' in 'abc'
True
>>> 'A' in 'abc'
False
>>> '' in 'abc'
True
>>> '' in ''
True

``` 




## Choosing Which Statements to Execute


```python 
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 6.0
>>> if ph < 7.0: 
...     print(ph, "is acidic.")
... 
6.0 is acidic.

``` 


```python 
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 8.0
>>> if ph < 7.0:
...     print(ph, "is acidic.")
...
>>>

``` 




```python 
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 6
>>> if ph < 7.0:
... print(ph, "is acidic.")
  File "<stdin>", line 2
    print(ph, "is acidic.")
        ^
IndentationError: expected an indented block
``` 



```python 
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 6.0
>>> if ph < 7.0:
...     print(ph, "is acidic.")
...     print("You should be careful with that!")
... 
6.0 is acidic.
You should be careful with that!

``` 

```python 
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 8.0
>>> if ph < 7.0:
...     print(ph, "is acidic.")
... 
>>> print("You should be careful with that!")
You should be careful with that!
``` 

```python 
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 8.0
>>> if ph < 7.0:
...     print(ph, "is acidic.")
... print("You should be careful with that!")
  File "<stdin>", line 3
    print("You should be careful with that!")
        ^
SyntaxError: invalid syntax
``` 


```python 
ph = 8.0
if ph < 7.0:
    print(ph, "is acidic.")
print("You should be careful with that!")

``` 




```python 
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 8.5
>>> if ph < 7.0:
...     print(ph, "is acidic.")
...
>>> if ph > 7.0:
...     print(ph, "is basic.")
...
8.5 is basic.
>>>

``` 



```python 
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 8.5
>>> if ph < 7.0:
...     print(ph, "is acidic.")
... elif ph > 7.0:
...     print(ph, "is basic.")
...
8.5 is basic.
>>>

``` 


```python 
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 7.0
>>> if ph < 7.0:
...     print(ph, "is acidic.")
... elif ph > 7.0:
...     print(ph, "is basic.")
...
>>>

``` 



```python 
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 6.0
>>> if ph < 7.0:
...     ph = 8.0
...
>>> if ph > 7.0:
...     print(ph, "is acidic.")
...
8.0 is acidic.
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 6.0
>>> if ph < 7.0:
...     ph = 8.0
>>> elif ph > 7.0:
...     print(ph, "is acidic.")
...
>>>

``` 






```python 
>>> compound = input('Enter the compound: ')
Enter the compound: CH4
>>> if compound == "H2O":
...     print("Water")
... elif compound == "NH3":
...     print("Ammonia")
... elif compound == "CH4":
...     print("Methane")
...
Methane
>>>

``` 

```python 
>>> compound = input('Enter the compound: ')
Enter the compound: H2SO4
>>> if compound == "H2O":
...     print("Water")
... elif compound == "NH3":
...     print("Ammonia")
... elif compound == "CH4":
...     print("Methane")
... else:
...     print("Unknown compound")
...
Unknown compound
>>>

``` 


## Nested ```if``` Statements



```python 
value = input('Enter the pH level: ')
if len(value) > 0:
    ph = float(value)
    if ph < 7.0:
        print(ph, "is acidic.")
    elif ph > 7.0:
        print(ph, "is basic.")
    else:
        print(ph, "is neutral.")
else:
    print("No pH value was given!")

``` 



## Remembering Results of a Boolean Expression Evaluation



```python 
>>> x = 15 > 5


``` 




## Exercises




```python 
ph = float(input("Enter the ph level: "))
if ph < 7.0:
    print("It's acidic!")
elif ph < 4.0:
    print("It's a strong acid!")
``` 


```python 
>>> ph = 2
>>> if ph < 7.0:
...     print(ph, "is acidic.")
... elif ph < 3.0:
...     print(ph, "is VERY acidic! Be careful.")
...
2 is acidic.
``` 


