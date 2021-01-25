# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business 
# University of Central Florida
#
# January 7, 2021
# 
##################################################
#
# Demo for Chapter 4: Working with Text
#
##################################################
"""


##################################################
## Creating Strings of Characters
##################################################

# In Python, text is represented as a string when a sequence
# of characters is enclosed in single or double quotes. 

 
'Aristotle'
# 'Aristotle'
"Isaac Newton"
# 'Isaac Newton'

 
# The quotes have to match or the statement will be unfinished. 

 
'Charles Darwin"
#   File "<stdin>", line 1
#     'Charles Darwin"
#                    ^
# SyntaxError: EOL while scanning string literal

 
# An empty string is created when the quotes contain no characters.


 
''
# ''
""
# ''

 

#-------------------------------------------------
### Operations on Strings
#-------------------------------------------------

# Some functions are designed to operate on strings. 
# The len function returns the length of the string
# (and can be used on other data types, as well).

 
len('Albert Einstein')
# 15
len('123!')
# 4
len(' ')
# 1
len('')
# 0

 
# Several binary operators are also defined on strings. 
# The + operator *concatenates* strings

 
'Albert' + ' Einstein'
# 'Albert Einstein'

 
# Empty strings act like the number zero under addition. 
 
"Alan Turing" + ''
# 'Alan Turing'
"" + 'Grace Hopper'
# 'Grace Hopper'

 
# But you can't add a number to a string:

 
'NH' + 3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Can't convert 'int' object to str implicitly

 
# Likewise in the other order:
 
9 + ' planets'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

 

# The particular error depends on the type of the first argument. 

# You can convert a number to a string by using the str
# function first. 
 
'Four score and ' + str(7) + ' years ago'
'Four score and 7 years ago'

 
# Some strings can be converted to numbers:
 
int('0')
# 0
int("11")
# 11
int('-324')
# -324
float('-324')
# -324.0
float("56.34")
# 56.34

 
# but not all strings:
 
int('a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'a'
float('b')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: could not convert string to float: 'b'
 

# The multiplication operator works as you might guess
# when used on strings,
 
'AT' * 5
# 'ATATATATAT'
4 * '-'
# '----'

 
# and multiplication of a string by zero gives the empty string, 
 
'GC' * 0
# ''

# but so does multiplication by a negative number 
# (strings of negative length are not defined).


'TATATATA' * -3
# ''

 
# Strings are values, so you can assign strings to variables

 
sequence = 'ATTGTCCCCC'
len(sequence)
# 10
new_sequence = sequence + 'GGCCTCCTGC'
new_sequence
# 'ATTGTCCCCCGGCCTCCTGC'
new_sequence * 2
# 'ATTGTCCCCCGGCCTCCTGCATTGTCCCCCGGCCTCCTGC'
 
# and you can perform string operations on these variables. 


##################################################
## Using Special Characters in Strings
##################################################

# Quotes within strings can prematurely end the definition of a string,

 
'that's not going to work'
#   File "<stdin>", line 1
#     'that's not going to work'
#           ^
# SyntaxError: invalid syntax

 
# and cause an error. 
# Fix it by using different types of quotes. 


 
"that's better"
# "that's better"
'She said, "That is better."'
# 'She said, "That is better."'

 

# It works regardless of whether the string begins
# with single or double quotes.

 
'She said, "That' + "'" + 's hard to read."'
# 'She said, "That\'s hard to read."'

 
# Notice the backslash combined with the single qoute: \', 
# which is an *escape sequence* for the single quote. 
# You can also use this to define a string containing quotes. 

 
len('\'')
# 1
len('it\'s')
# 4
 


##################################################
## Creating a Multiline String
##################################################

# As with other commands, the string definition should complete on one line.


 
'one
#   File "<stdin>", line 1
#     'one
#        ^
# SyntaxError: EOL while scanning string literal
 

# Otherwise, you can use triple double-quotes to span multiple lines.


 
'''one
... two
... three'''
# 'one\ntwo\nthree'
 
# Notice the \n escape sequence for *newline*. 



 
'''Should you want a string
that crosses multiple lines,
Use matched triple quotes.'''
 



##################################################
## Printing Information
##################################################

# The print function does just what is advertised. 
# It works for numbers as well as strings. 

 
print(1 + 1)
# 2
print("The Latin 'Oryctolagus cuniculus' means 'domestic rabbit'.")
# The Latin 'Oryctolagus cuniculus' means 'domestic rabbit'.

 



 
print('In 1859, Charles Darwin revolutionized biology')      
# In 1859, Charles Darwin revolutionized biology
print('and our understanding of ourselves')      
# and our understanding of ourselves
print('by publishing "On the Origin of Species".')
# by publishing "On the Origin of Species".

 
# Notice that the outer quotes are not printed.
# It is understood that you want to print the contents of the string.

# The \t escape sequence is equivalent to pressing the "Tab" key.

 
print('one\ttwo\nthree\tfour')
# one	two
# three	four

 

# When you define a multi-line string with triple-quotes,
# the newline characters are automatically added, 
 
numbers = '''one
... two
... three'''
numbers
# 'one\ntwo\nthree'


# but the print function executes the instruction, 
# rather than printing the escape sequence.


print(numbers)
# one
# two
# three

 

# The print function takes multiple arguments and ...prints them.
 
print(1, 2, 3)
# 1 2 3

 
# If there are no arguments passed to print, 
# it prints the empty string.
 
print()


 

# You can pass arguments of different types,
 
print(1, 'two', 'three', 4.0)
# 1 two three 4.0
 
# and perform calculations within those arguments.

 
radius = 5
print("The diameter of the circle is", radius * 2, "cm.")
# The diameter of the circle is 10 cm.

 

# By default, the arguments are separated by a space, 
# as in the sep argument and ends with a newline, 
# as in the end argument. 
# If you want to change these, supply different values
# to those arguments. 

 
help(print)
# Help on built-in function print in module builtins:

# print(...)
#     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

#     Prints the values to a stream, or to sys.stdout by default.
#     Optional keyword arguments:
#     file:  a file-like object (stream); defaults to the current sys.stdout.
#     sep:   string inserted between values, default a space.
#     end:   string appended after the last value, default a newline.
#     flush: whether to forcibly flush the stream.
# print('a', 'b', 'c')  # The separator is a space by default
# a b c
# print('a', 'b', 'c', sep=', ')
# a, b, c
# print('a', 'b', 'c', sep=', ', end='')
# a, b, c

 

# You can use the print function to print 
# formatted statements from the values returned from your functions. 

 
def convert_to_celsius(fahrenheit: float) -> float:
    """ Return the number of Celsius degrees equivalent to fahrenheit degrees.

    convert_to_celsius(75)
    23.88888888888889
    """

    return (fahrenheit - 32.0) * 5.0 / 9.0

print('80, 78.8, and 10.4 degrees Fahrenheit are equal to ', end='')
print(convert_to_celsius(80), end=', \n')
print(convert_to_celsius(78.8), end=', and ')
print(convert_to_celsius(10.4), end=' Celsius.\n')

 


##################################################
## Getting Information from the Keyboard
##################################################

# The input function takes input from the keyboard.

 
species = input()
# Homo sapiens

# It assigns the value to the variable as if any expression
# were passed to the assignment operator.


species
# 'Homo sapiens'


# Regardless of the type, input always returns a string.

population = input()
# 6973738433
population
# '6973738433'
type(population)
# <class 'str'>

 
# Once assigned to a variable, the value can be used like any other, 
# except that you might convert it to a numeric type. 
 
population = input()
# 6973738433
population
# '6973738433'
population = int(population)
population
# 6973738433
population = population + 1
population
# 6973738434

 
# To shorten the code, you can chain the input function
# within the int function, which converts the number 
# to integer format right away. 
 
population = int(input())
# 6973738433
population = population + 1
# 6973738434

 

# The argument to the input function is a string that will appear
# at the screen, prompting the user to enter something at the keyboard. 
 
species = input("Please enter a species: ") 
# Please enter a species: Python curtus
print(species)
# Python curtus
 





##################################################
## End
##################################################
