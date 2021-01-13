# Chapter 3, Part B: Designing Functions



## Designing New Functions: A Recipe



In this demo, we will study the process of designing functions. 
We will follow the 5-step process in our textbook *Practical Programming*, 
Chapter 3, called the **Function Design Recipe**. 
It is called a recipe because it guides you to follow a systematic approach to designing your function. 
Every time you write a function, you need to answer the following questions:

* What do you name the function? 
* What are the argumants, and what types of information do they represent?
* What calculations are you doing with that information?
* What does the function return?
* Does it work as expected?

You will address these questions by following the recipe shown next. 

## The Function Design Recipe

The five steps are as follows:

1. **Examples** Type a few example calls and determine what it should return for those values. 
The name of your function should indicate what is being calculated in your examples. 
1. **Description** Write a few sentences to describe what your function does. 
1. **Header** Type some documentation relating to your function. 
It should be clear to the reader what arguments it takes as input and what value is returned and the types of each variable. 
1. **Body** By now, you should be clear about how your function will work. 
Now type the code to perform the calculations. 
1. **Test** Run the examples from step 1 to verify that your function works as expected. 


## Function Design Example


Consider the simple example of the function ```add_two_numbers``` that, well, adds two numbers.

```python
# Define a function without documentation.
>>> def add_two_numbers(first_number, second_number):
...    
...    total = first_number + second_number
...    
...    return total
...
...
```

The function is fine but how does the user know how it works. 
Guessing is only reasonable if the function is simple. 

```python
>>> add_two_numbers(3,4)
7
```

That makes sense and it appears to work. 
If your user wants to know for sure, they can
search for documentation, as you would for any other function.

```python
>>> help(add_two_numbers)
Help on function add_two_numbers in module __main__:

add_two_numbers(first_number, second_number)
```
There's nothing there yet.

You could print the entire function object but that
is not very convenient for long and complex functions.
```python
>>> add_two_numbers
<function __main__.add_two_numbers(first_number, second_number)>
```

Instead, add documentation to the function in a docstring.


```python
>>> def add_two_numbers(first_number, second_number):
...    """ Add two numbers together and return the sum.
...    
...    """
...    
...    total = first_number + second_number
...    
...    return total
...
```



Now test the documentation by calling for help:
```python
>>> help(add_two_numbers)
Help on function add_two_numbers in module __main__:

add_two_numbers(first_number, second_number)
    Add two numbers together and return the sum.
```

Notice the content from the description in the docstring.

We can improve the docstring by including examples,
so now let's cover all of these step by following
the *function design recipe*.



## Function Design Recipe

Now apply the function design recipe to the ```add_two_numbers``` example.

### Examples

Try to think of some examples that will test the limit of your function.
Note that we can run the tests only because we have already defined the
function in the examples above.

```python
>>> add_two_numbers(3,4)
7
>>> add_two_numbers(0,4)
4
>>> add_two_numbers(-3,3)
0

```

Now you know that your function will have a form like this.

```python
>>> def add_two_numbers(first_number, second_number):
...    
...    
...    
...    return total
...
...
```


### Header

Write a header to contain information about the
the types of variables in your function.

```python
>>> def add_two_numbers(first_number: float, second_number: float) -> float:
...    
...    
...    
...    return total
...
...
```

### Description

Add a description of what your function does, in words.
Include the list of your examples.

```python
>>> def add_two_numbers(first_number: float, second_number: float) -> float:
...    """ Add two numbers together and return the sum.
...    >>> add_two_numbers(3,4)
...    7
...    >>> add_two_numbers(0,4)
...    4
...    >>> add_two_numbers(-3,3)
...    0
...    """
...    
...    
...    return total
...
...
```

### Body

In this case, the body is simple but this is often the most work. 

```python
>>> def add_two_numbers(first_number: float, second_number: float) -> float:
...    """ Add two numbers together and return the sum.
...    >>> add_two_numbers(3,4)
...    7
...    >>> add_two_numbers(0,4)
...    4
...    >>> add_two_numbers(-3,3)
...    0
...    """
...    
...    total = first_number + second_number
...    
...    return total
...
...
```

It seems like a lot of work to do to prepare to write one line of code.
With more elaborate functions, having clearly stated the 
examples, header and description, 
you should be clear about what it is you will compute and the planning will pay off. 



### Test

Finally, test your functions to confirm accuracy. 

```python
>>> add_two_numbers(3,4)
7
>>> add_two_numbers(0,4)
4
>>> add_two_numbers(-3,3)
0

```

If all goes well, these examples should all return
the values you expect.
If not, be sure that your examples are correct
or modify your function definition.
Most of the work in coding is correcting your mistakes.


## Tips

You will get better at writing functions as you gain more experience but the following tips can help you improve more quickly. 
* Start off with a simple case. 
  * Save the corner cases for after your base cases work. 
* Start off with a simple approach.
  * You can adjust the code for faster computation once it is working. 
* Type the comments first.
  * Describe to the first user (you!) how the calculations will be performed. 
  * Split the calculation into checkpoints where you can determine the format 
  of intermediate calculations.
  * Type in the code one block at a time. 
  * Assign values to the arguments (but hide them in comments, so as not to interfere) 
  and run blocks of code in the IDE to test one section at a time.
* If you find it is getting too complicated, consider breaking up the calculation 
into separate parts.  
  * Is there a natural checkpoint where you can test with examples? 
* Choose examples that provide good testing cases. 
  * Does your function work with negative values? 
  * Does it work with missing values? 
  * Does it work with the wrong data types? 
  * Are there any knife-edge cases when the procedure will change? 
  * Are there any obvious boundaries?
* After making any significant changes to a partially-working function, 
re-run all of your test cases to make sure they are still correct.
  * Did you break any of the test cases that were working before?
  * Did you fix any that were not working? 
  * Keeping score is good motivation.
  * With regular testing, you can make changes with more confidence. 





## Designing More Functions: Practice with the Recipe

Let's run through the function design recipe with a few examples
to practice the 5 steps:
1. **Examples** Type example calls and what you expect it to return.
Choose appropriate names for your function and it's arguments. 
1. **Description** Write a short description to describe what your function does. 
1. **Header** Type some documentation to describe the arguments and return value. 
1. **Body** Type the code to perform the calculations. 
1. **Test** Run the examples to verify that your function works as expected. 


## Designing Three Birthday-Related Functions

#### 1. **Examples** 
Type example calls and what you expect it to return.
Choose appropriate names for your function and it's arguments. 
#### 2. **Description** 
Write a short description to describe what your function does. 
#### 3. **Header** 
Type some documentation to describe the arguments and return value. 
#### 4. **Body** 
Type the code to perform the calculations. 
#### 5. **Test** 
Run the examples to verify that your function works as expected. 



### How Many Days Difference?


```python 
>>> help(days_difference)
Help on function days_difference in module __main__:

days_difference(day1:int, day2:int) -> int
    Return the number of days between day1 and day2, which are both
    in the range 1-365 (thus indicating the day of the year).

    >>> days_difference(200, 224)
    24
    >>> days_difference(50, 50)
    0
    >>> days_difference(100, 99)
    -1

``` 


```python 
>>> days_difference(200, 224)
24
>>> days_difference(50, 50)
0
>>> days_difference(100, 99)
-1

``` 




### What Weekday Will It be in the Future?


```python 
>>> get_weekday(3, 1)
4
>>> get_weekday(6, 1)
7
>>> get_weekday(7, 1)
1
>>> get_weekday(1, 0)
1
>>> get_weekday(4, 7)
4
>>> get_weekday(7, 72)
2

``` 



```python 
>>> get_weekday(3, 1)
4
>>> get_weekday(6, 1)
7
>>> get_weekday(7, 1)
8

``` 

```python 
>>> get_weekday(3, 1)
4
>>> get_weekday(6, 1)
0
>>> get_weekday(7, 1)
1

``` 



### What Day Is My Birthday On?




```python 
>>> get_birthday_weekday(5, 3, 4)
6
>>> get_birthday_weekday(5, 3, 116)
6
>>> get_birthday_weekday(6, 116, 3)
5

``` 














```python 
def weeks_elapsed(day1, day2):
    """ (int, int) -> int

    day1 and day2 are days in the same year. Return the number of full weeks
    that have elapsed between the two days.

    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)

    >>> weeks_elapsed(40, 61)

    """

``` 


```python 
>>> def get_weekday(current_weekday: int, days_ahead: int) -> int:
...     """Return which day of the week it will be days_ahead days
...     from current_weekday.
...
...     current_weekday is the current day of the week and is in
...     the range 1-7, indicating whether today is Sunday (1),
...     Monday (2), ..., Saturday (7).
...
...     days_ahead is the number of days after today.
...
...     >>> get_weekday(3, 1)
...     4
...     >>> get_weekday(6, 1)
...     7
...     >>> get_weekday(7, 1)
...     1
...     >>> get_weekday(1, 0)
...     1
...     >>> get_weekday(4, 7)
...     4
...     >>> get_weekday(7, 72)
...     2
...     """
...     return (current_weekday + days_ahead) % 7
...

>>> def days_difference(day1: int, day2: int) -> int:
...     """Return the number of days between day1 and day2, which are
...     both in the range 1-365 (thus indicating the day of the
...     year).
...
...     >>> days_difference(200, 224)
...     24
...     >>> days_difference(50, 50)
...     0
...     >>> days_difference(100, 99)
...     -1
...     """
...     return day2 - day1
...
>>> days_difference(200, 224)
24
>>> days_difference(50, 50)
0
>>> days_difference(100, 99)
-1

>>> def get_birthday_weekday(current_weekday: int, current_day: int,
...                          birthday_day: int) -> int:
...     """Return the day of the week it will be on birthday_day,
...     given that the day of the week is current_weekday and the
...     day of the year is current_day.
...
...     current_weekday is the current day of the week and is in
...     the range 1-7, indicating whether today is Sunday (1),
...     Monday (2), ..., Saturday (7).
...
...     current_day and birthday_day are both in the range 1-365.
...
...     >>> get_birthday_weekday(5, 3, 4)
...     6
...     >>> get_birthday_weekday(5, 3, 116)
...     6
...     >>> get_birthday_weekday(6, 116, 3)
...     5
...     """
...     days_diff = days_difference(current_day, birthday_day)
...     return get_weekday(current_weekday, days_diff)
...

``` 

```python 
def get_weekday(current_weekday: int, days_ahead: int) -> int:
    """Return which day of the week it will be days_ahead days from
    current_weekday.

    current_weekday is the current day of the week and is in the range 1-7,
    indicating whether today is Sunday (1), Monday (2), ..., Saturday (7).

    days_ahead is the number of days after today.

    >>> get_weekday(3, 1)
    4
    >>> get_weekday(6, 1)
    7
    >>> get_weekday(7, 1)
    1
    >>> get_weekday(1, 0)
    1
    >>> get_weekday(4, 7)
    4
    >>> get_weekday(7, 72)
    2
    """

    return (current_weekday + days_ahead) % 7

def days_difference(day1: int, day2: int) -> int:
    """Return the number of days between day1 and day2, which are both
    in the range 1-365 (thus indicating the day of the year).

    >>> days_difference(200, 224)
    24
    >>> days_difference(50, 50)
    0
    >>> days_difference(100, 99)
    -1
    """

    return day2 - day1


def get_birthday_weekday(current_weekday: int, current_day: int, birthday_day: int):
    """Return the day of the week it will be on birthday_day, given that
    the day of the week is current_weekday and the day of the year is
    current_day.

    current_weekday is the current day of the week and is in the range 1-7,
    indicating whether today is Sunday (1), Monday (2), ..., Saturday (7).

    current_day and birthday_day are both in the range 1-365.

    >>> get_birthday_weekday(5, 3, 4)
    6
    >>> get_birthday_weekday(5, 3, 116)
    6
    >>> get_birthday_weekday(6, 116, 3)
    5
    """

    days_diff = days_difference(current_day, birthday_day)
    return get_weekday(current_weekday, days_diff)

``` 

```python 
>>> def get_weekday(current_weekday: int, days_ahead: int) -> int:
...     """Return which day of the week it will be days_ahead days from
...     current_weekday.
...
...     current_weekday is the current day of the week and is in the
...     range 1-7, indicating whether today is Sunday (1), Monday (2),
...     ..., Saturday (7).
...
...     days_ahead is the number of days after today.
...
...     >>> get_weekday(3, 1)
...     4
...     >>> get_weekday(6, 1)
...     7
...     >>> get_weekday(7, 1)
...     1
...     >>> get_weekday(1, 0)
...     1
...     >>> get_weekday(4, 7)
...     4
...     >>> get_weekday(7, 72)
...     2
...     """
...     return current_weekday + days_ahead % 7
...

>>> def days_difference(day1: int, day2: int) -> int:
...     """Return the number of days between day1 and day2, which are both
...     in the range 1-365 (thus indicating the day of the year).
...
...     >>> days_difference(200, 224)
...     24
...     >>> days_difference(50, 50)
...     0
...     >>> days_difference(100, 99)
...     -1
...     """
...     return day2 - day1
...


>>> def get_birthday_weekday(current_weekday: int, current_day: int,
...                          birthday_day: int) -> int:
...     """Return the day of the week it will be on birthday_day, given that
...     the day of the week is current_weekday and the day of the year is
...     current_day.
...
...     current_weekday is the current day of the week and is in the range 1-7,
...     indicating whether today is Sunday (1), Monday (2), ..., Saturday (7).
...
...     current_day and birthday_day are both in the range 1-365.
...
...     >>> get_birthday_weekday(5, 3, 4)
...     6
...     >>> get_birthday_weekday(5, 3, 116)
...     6
...     >>> get_birthday_weekday(6, 116, 3)
...     5
...     """
...     days_diff = days_difference(current_day, birthday_day)
...     return get_weekday(current_weekday, days_diff)
...

``` 

```python 
def get_weekday(current_weekday: int, days_ahead: int) -> int:
    """Return which day of the week it will be days_ahead days from
    current_weekday.

    current_weekday is the current day of the week and is in the range 1-7,
    indicating whether today is Sunday (1), Monday (2), ..., Saturday (7).

    days_ahead is the number of days after today.

    >>> get_weekday(3, 1)
    4
    >>> get_weekday(6, 1)
    7
    >>> get_weekday(7, 1)
    1
    >>> get_weekday(1, 0)
    1
    >>> get_weekday(4, 7)
    4
    >>> get_weekday(7, 72)
    2
    """

    return current_weekday + days_ahead % 7

def days_difference(day1: int, day2: int) -> int:
    """Return the number of days between day1 and day2, which are both
    in the range 1-365 (thus indicating the day of the year).

    >>> days_difference(200, 224)
    24
    >>> days_difference(50, 50)
    0
    >>> days_difference(100, 99)
    -1
    """

    return day2 - day1


def get_birthday_weekday(current_weekday: int, current_day: int,
                         birthday_day: int) -> int:
    """Return the day of the week it will be on birthday_day, given that
    the day of the week is current_weekday and the day of the year is
    current_day.

    current_weekday is the current day of the week and is in the range 1-7,
    indicating whether today is Sunday (1), Monday (2), ..., Saturday (7).

    current_day and birthday_day are both in the range 1-365.

    >>> get_birthday_weekday(5, 3, 4)
    6
    >>> get_birthday_weekday(5, 3, 116)
    6
    >>> get_birthday_weekday(6, 116, 3)
    5
    """

    days_diff = days_difference(current_day, birthday_day)
    return get_weekday(current_weekday, days_diff)

``` 

```python 
def get_weekday(current_weekday, days_ahead):
    """ (int, int) -> int

    Return which day of the week it will be days_ahead days from
    current_weekday.

    current_weekday is the current day of the week and is in the range 1-7,
    indicating whether today is Sunday (1), Monday (2), ..., Saturday (7).

    days_ahead is the number of days after today.

    >>> get_weekday(3, 1)
    4
    >>> get_weekday(6, 1)
    7
    >>> get_weekday(7, 1)
    1
    >>> get_weekday(1, 0)
    1
    >>> get_weekday(4, 7)
    4
    >>> get_weekday(7, 72)
    2
    """

    return (current_weekday + days_ahead) % 7

def days_difference(day1, day2):
    """ (int, int) -> int

    Return the number of days between day1 and day2, which are both
    in the range 1-365 (thus indicating the day of the year).

    >>> days_difference(200, 224)
    24
    >>> days_difference(50, 50)
    0
    >>> days_difference(100, 99)
    -1
    """

    return day2 - day1


def get_birthday_weekday(current_weekday, current_day, birthday_day):
    """ (int, int, int) -> int

    Return the day of the week it will be on birthday_day, given that
    the day of the week is current_weekday and the day of the year is
    current_day.

    current_weekday is the current day of the week and is in the range 1-7,
    indicating whether today is Sunday (1), Monday (2), ..., Saturday (7).

    current_day and birthday_day are both in the range 1-365.

    >>> get_birthday_weekday(5, 3, 4)
    6
    >>> get_birthday_weekday(5, 3, 116)
    6
    >>> get_birthday_weekday(6, 116, 3)
    5
    """

    days_diff = days_difference(current_day, birthday_day)
    return get_weekday(current_weekday, days_diff)

``` 

```python 
def get_weekday(current_weekday, days_ahead):
    """ (int, int) -> int

    Return which day of the week it will be days_ahead days from
    current_weekday.

    current_weekday is the current day of the week and is in the range 1-7,
    indicating whether today is Sunday (1), Monday (2), ..., Saturday (7).

    days_ahead is the number of days after today.

    >>> get_weekday(3, 1)
    4
    >>> get_weekday(6, 1)
    7
    >>> get_weekday(7, 1)
    1
    >>> get_weekday(1, 0)
    1
    >>> get_weekday(4, 7)
    4
    >>> get_weekday(7, 72)
    2
    """
    return (current_weekday + days_ahead - 1) % 7 + 1

def days_difference(day1, day2):
    """ (int, int) -> int

    Return the number of days between day1 and day2, which are both
    in the range 1-365 (thus indicating the day of the year).

    >>> days_difference(200, 224)
    24
    >>> days_difference(50, 50)
    0
    >>> days_difference(100, 99)
    -1
    """

    return day2 - day1


def get_birthday_weekday(current_weekday, current_day, birthday_day):
    """ (int, int, int) -> int

    Return the day of the week it will be on birthday_day, given that
    the day of the week is current_weekday and the day of the year is
    current_day.

    current_weekday is the current day of the week and is in the range 1-7,
    indicating whether today is Sunday (1), Monday (2), ..., Saturday (7).

    current_day and birthday_day are both in the range 1-365.

    >>> get_birthday_weekday(5, 3, 4)
    6
    >>> get_birthday_weekday(5, 3, 116)
    6
    >>> get_birthday_weekday(6, 116, 3)
    5
    """

    days_diff = days_difference(current_day, birthday_day)
    return get_weekday(current_weekday, days_diff)

``` 



## Omitting a Return Statement: ```None```


```python 
>>> def f(x):
...     x = 2 * x
...
>>> res = f(3)
>>> res
>>>
```


```python
>>> print(res)
None
>>> id(res)
1756120
>>> type(res)
<class 'NoneType'>
```

```python
>>> def f(x):
...     x = 2 * x
...     return None
...
>>> print(f(3))
None
```




## Dealing with Situations That Your Code Doesn't Handle

```python 
def pie_percent(n: int) -> int:
    """Assuming there are n people who want to eat a pie, return the
    percentage of the pie that each person gets to eat.

    >>> pie_percent(5)
    20
    >>> pie_percent(2)
    50
    >>> pie_percent(1)
    100
    """

    return int(100 / n)
```

```python
def pie_percent(n: int) -> int:
    """Precondition: n > 0

    Assuming there are n people who want to eat a pie, return the percentage
    of the pie that each person gets to eat.

    >>> pie_percent(5)
    20
    >>> pie_percent(2)
    50
    >>> pie_percent(1)
    100
    """

    return int(100 / n)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

``` 




## Exercises

### Exercise 9



```python 
def square(num):
    """ (number) -> number
    
    Return the square of num.

    >>> square(3)
    9
    """

``` 



```python
>>> def print_intro(name):
...     """ (str) -> NoneType
...     Print a personalized greeting using name.
...     >>> print_intro('Jason')
...     Hello, Jason.
...     """
...     print('Hello,', name, end='.\n')
...
>>> print_intro('Jen')
Hello, Jen.

``` 

