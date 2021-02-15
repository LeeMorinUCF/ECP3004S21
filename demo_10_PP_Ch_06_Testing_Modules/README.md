# Chapter 6: A Modular Approach to Program Organization


## Defining Your Own Modules

In Chapter 3, we defined this function. 

```python 
>>> def convert_to_celsius(fahrenheit: float) -> float:
...     """Return the number of Celsius degrees equivalent to fahrenheit
...     degrees.
...
...     >>> convert_to_celsius(75)
...     23.88888888888889
...     """
...     return (fahrenheit - 32.0) * 5.0 / 9.0
...

``` 

If you save this function definition into a file named
```temperature.py```, you can import it as a module. 

```python 
>>> import temperature
>>> celsius = temperature.convert_to_celsius(33.3)
>>> temperature.above_freezing(celsius)
True

``` 



### What Happens During Import

Let's try an experiment: save the following command in a file 
called ```experiment.py```. 

```python 
print("The panda's scientific name is 'Ailuropoda melanoleuca'")

``` 

Then ```import``` it as a module and see what happens:


```python 
>>> import experiment
The panda's scientific name is 'Ailuropoda melanoleuca'

``` 
It executed the ```print``` statement in the file. 
This shows that Python *executes the commands in a module*
when it imports. 

Now try to import it a second time in the same script.

```python 
>>> import experiment
The panda's scientific name is 'Ailuropoda melanoleuca'
>>> import experiment
>>>

``` 

The message wasn't printed the second time. 
Python keeps track of modules that have already been loaded
and does not execute the scripts twice. 
This saves time if you import modules that import other modules.
Sometimes several modules would otherwise import the same module
multiple times. 

If you need to edit the commands in a module, the changes would not be updated
automatically. 
You can use the ```imp``` module to ```reload``` the module with your changes. 


In between the next set of commands, change the ```print``` command
to the following (switching pandas for koalas).

```python 
print("The koala's scientific name is 'Phascolarctos cinereus'")

``` 

Afterward, ```reload``` the module with this change.


```python 
>>> import experiment
The panda's scientific name is 'Ailuropoda melanoleuca'
>>> import experiment
>>> import imp
>>> imp.reload(experiment)
The koala's scientific name is 'Phascolarctos cinereus'
<module 'experiment' from '/Users/campbell/Documents/experiment.py'>
``` 
Notice the new version is effective after the ```reload``` command. 


#### Restoring a Module

If you want to reload a module, you could restart Python but the 
```importlib``` module avoids restarting. 

```python 
>>> import example
>>> example.x
2
>>> example.x = 7
>>> example.x
7
>>> import importlib
>>> example = importlib.reload(example)
>>> example.x
2
``` 

This doesn't work, however, for systems modules, like ```math```. 

```python 
>>> import math
>>> math.pi
3.141592653589793
>>> math.pi = 3
>>> math.pi
3
>>> math = importlib.reload(math)
>>> math.pi
3
``` 

It's better to simply avoid overwriting functions or values in modules. 


### Selecting Which Code Gets Run on Import: ```__main__```

Sometimes you want some commands to run only when the module 
is run directly but not when it is imported. 
Python defines a special variable named ```__name__``` to help
us figure this out. 

Place this command in the file ```echo.py```:

```python 
print("__name__ is", __name__)

``` 
If we run this file it outputs this: 
```python 
__name__ is __main__

``` 

When we import the script as a module, the following output is produced. 

```python 
>>> import echo
__name__ is echo

``` 
Now follow this with an additional command:
```python 
import echo

print("After import, __name__ is", __name__, 
	"and echo.__name__ is", echo.__name__)

``` 


```python 
__name__ is echo
After import, __name__ is __main__ and echo.__name__ is echo

``` 

When Python imports this module, the ```__name__``` variable
stores the special string ```__main__``` but the variable within the module, 
```echo.__name__``` stores the name of the module.



This means that a module can tell whether it is being run by the main program. 

Now create another file called ```main_example.py``` with the following code. 

```python 
if __name__ == "__main__":
    print("I am the main program.")
else:
    print("Another module is importing me.")

``` 

Try running this script by running the script and by importing the module. 


Some modules contain only function modules but others contain programs. 
The file ```temperature_program.py``` contains the following. 

```python 
def convert_to_celsius(fahrenheit: float) -> float:
    """Return the number of Celsius degrees equivalent to fahrenheit
    degrees.

    >>> convert_to_celsius(75)
    23.88888888888889
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0


def above_freezing(celsius: float) -> bool:
    """Return True iff temperature celsius degrees is above freezing.

    >>> above_freezing(5.2)
    True
    >>> above_freezing(-2)
    False
    """
    return celsius > 0


fahrenheit = float(input('Enter the temperature in degrees Fahrenheit: '))
celsius = convert_to_celsius(fahrenheit)
if above_freezing(celsius):
    print('It is above freezing.')
else:
    print('It is below freezing.')

``` 
When this module is run, it runs the block of code at the bottom and
asks the user for input. 

Now create another module, ```baking.py``` that imports the 
above ```temperature_program``` module. 


```python 
import temperature_program

def get_preheating_instructions(fahrenheit: float) -> str:
    """Return instructions for preheating the oven in fahreneheit degrees and
    Celsius degrees.

    >>> get_preheating_instructions(500)
    'Preheat oven to 500 degrees F (260.0 degrees C).'
    """

    cels = str(temperature_program.convert_to_celsius(fahrenheit))
    fahr = str(fahrenheit)
    return 'Preheat oven to ' + fahr + ' degrees F ('+ cels +' degrees C).'


fahr = float(input('Enter the baking temperature in degrees Fahrenheit: '))
print(get_preheating_instructions(fahr))

``` 

When ```baking.py``` is run, it imports the code at the bottom of
the ```temperature_program.py``` script. 
If we don't care about running that block of code, then we can place it 
within an ```if``` statement of the form 
```if __name__ == '__main__':```.

```python 

<function definitions copied from above>

if __name__ == '__main__':
  fahrenheit = float(input('Enter the temperature in degrees Fahrenheit: '))
  celsius = convert_to_celsius(fahrenheit)
  if above_freezing(celsius):
      print('It is above freezing.')
  else:
      print('It is below freezing.')

``` 







## Testing Your Code Semiautomatically

The last step after designing the functions in your module is to test them. 



The ```doctest``` module allows us to run the tests that are included 
in the function docstrings. 


```python 
>>> import doctest
>>> doctest.testmod()
TestResults(failed=0, attempted=3)
``` 

This message tells us that three tests were attempted and none failed. 

As an experiment, suppose that we had made an error in our calculation.
Suppose that instead of ```(fahrenheit - 32.0) * 5.0 / 9.0``` we 
calculate ```fahrenheit - 32.0 * 5.0 / 9.0```. 
That is, we forgot to include the parentheses.

To test this, replace the definition of the ```convert_to_celsius```
function with this:

```python 
def convert_to_celsius(fahrenheit):
    """ (number) -> float

    Return the number of Celsius degrees equivalent to fahrenheit degrees.

    >>> convert_to_celsius(75)
    23.88888888888889
    """
                        
    return fahrenheit - 32.0 * 5.0 / 9.0

``` 


Then, when we run ```doctest``` on that module.


```python 
>>> import testmod
>>> doctest.testmod()
**********************************************************************
File "__main__", line 6, in __main__.convert_to_celsius
Failed example:
    convert_to_celsius(75)
Expected:
    23.88888888888889
Got:
    57.22222222222222
**********************************************************************
1 items had failures:
   1 of   1 in __main__.convert_to_celsius
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=3)
``` 

This test failed. That is finds that the calculation returned an error.
When calculating ```convert_to_celsius(75)```, 
the expected answer is ```23.88888888888889``` 
but instead the calculation returns ```57.22222222222222```. 


## Exercises


Recall the examples of the birthday functions we covered to practice
the function design recipe in Chapter 3.
We had to make some adjustments to the code to get all the examples to work.
These versions are stored in python modules 
```birthday_v1.py```, ```birthday_v2.py```, and ```birthday_v3.py```.

Now we have the tools to test these examples automatically. 
Use the ```doctest.testmod()``` function in the ```doctest``` module 
to test these and observe the results. 
A sample script for these tests is provided in ```birthday_tests.py```.



