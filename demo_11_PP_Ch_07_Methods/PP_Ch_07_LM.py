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
# January 9, 2021
# 
##################################################
#
# Demo for Chapter 7: Using Methods 
#
##################################################
"""


# A *method* is kind of function that is attached to a particular type
# of object called a class. 

##################################################
## Modules, Classes, and Methods
##################################################

# In the help function call for the str function, 
# it shows that str is a class. 

 
help(str)
# Help on class str in module builtins:

# class str(object)
#  |  str(object='') -> str
#  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
#  |
#  |  Create a new string object from the given object. If encoding or
#  |  errors is specified, then the object must expose a data buffer
#  |  that will be decoded using the given encoding and error handler.
#  |  Otherwise, returns the result of object.__str__() (if defined)
#  |  or repr(object).
#  |  encoding defaults to sys.getdefaultencoding().
#  |  errors defaults to 'strict'.
#  |
#  |  Methods defined here:
#  |
#  |  __add__(self, value, /)
#  |      Return self+value.
#  |
#  |  __contains__(self, key, /)
#  |      Return key in self.

#  [Lots of other names with leading and trailing underscores not shown here.]

#  |  capitalize(...)
#  |      S.capitalize() -> str
#  |
#  |      Return a capitalized version of S, i.e. make the first character
#  |      have upper case and the rest lower case.
#  |
#  |  casefold(...)
#  |      S.casefold() -> str
#  |
#  |      Return a version of S suitable for caseless comparisons.
#  |
#  |  center(...)
#  |      S.center(width[, fillchar]) -> str
#  |
#  |      Return S centered in a string of length width. Padding is
#  |      done using the specified fill character (default is a space)
#  |
#  |  count(...)
#  |      S.count(sub[, start[, end]]) -> int
#  |
#  |      Return the number of non-overlapping occurrences of substring sub in
#  |      string S[start:end].  Optional arguments start and end are
#  |      interpreted as in slice notation.

# [There are many more of these as well.]

 

# Near the top line is the following:

 
#  |  str(object[, encoding[, errors]]) -> str
#  |
#  |  Create a new string object from the given object.

 

# It says that we can use the str function to produce a string. 

# The "str" class includes the method "capitalize".

 
# This looks exactly like the way you would use a function
# if you had run, say, "import str" first.

str.capitalize('browning')
# 'Browning'

 
# Other methods can center a string within a string of a certain length. 

 
str.center('Sonnet 43', 26)
# '        Sonnet 43         '
str.count('How do I love thee?  Let me count the ways.', 'the')
# 2

# Do you care about the difference between "the" and "thee"?
# If so, run this instead:
str.count('How do I love thee?  Let me count the ways.', ' the ')

 
# or count the number of times that the string 'the' appears in
# the first string. 


# Let's make this more compact:
my_string = 'How do I love thee?  Let me count the ways.'
string_to_find = ' the '    
str.count(my_string, string_to_find)

# Instead, you can write:
my_string.count(string_to_find)



##################################################
## Calling Methods the Object-Oriented Way
##################################################

# Every method in class str takes a string as the first argument. 
# Another way to use these methods is to list the object first, then call the string method after a dot, in the form
# name_of_string.name_of_string_method(arguments).
# Instead of assigning the string to a variable, you can place 
# the actual string before the method. 

 
'browning'.capitalize()
# 'Browning'
'Sonnet 43'.center(26)
# '        Sonnet 43         '
'How do I love thee?  Let me count the ways.'.count('the')
# 2

 

# The help documentation for methods uses this form. 

 
help(str.lower)
# Help on method_descriptor:

# lower(...)
#     S.lower() -> str

#     Return a copy of the string S converted to lowercase.

 

# Compare this with the doumentation for the sqrt function
# in the math module. 

# Example
'Browning'.lower()

# You can chain these method calls:
'browning'.capitalize().lower().center(26)

# Compare to functions:
str.center(str.lower(str.capitalize('browning')), 26)


 
import math
help(math.sqrt)
# Help on built-in function sqrt in module math:

# sqrt(...)
#     sqrt(x)

#     Return the square root of x.

 
# Notice that there is no prefix before the function name sqrt, 
# where the S.lower function has the prefix S., 
# to represent the particular string. 

# A string method can be called with an expression that evaluates to a string:

 
('TTA' + 'G' * 3).count('T')
# 2

 


##################################################
## Exploring String Methods
##################################################

# Here are some examples of string methods from Table 8 on page 119--20. 


 
'species'.startswith('a')
# False
'species'.startswith('spe')
# True

 

 
'species'.endswith('a')
# False
'species'.endswith('es')
# True

 
# Those methods are self explanatory. 
# The method lstrip strips the whiespace on the left of a string. 

 
compound = '     \n  Methyl \n butanol   \n'

print(compound)

compound.lstrip()
# 'Methyl \n butanol   \n'
compound.rstrip()
# '     \n  Methyl \n butanol'
compound.strip()
# 'Methyl \n butanol'


print(compound.strip())
 

# The swapcase method exchanges upper case for lower case
# characters, and vice versa.

 
'Computer Science'.swapcase()
# 'cOMPUTER sCIENCE'

# Chain some method calls:
'Computer Science'.lower().swapcase()

# In one step:
'Computer Science'.upper()

 
# The format method substitutes a series of strings into another string. 

 
'"{0}" is derived from "{1}"'.format('none', 'no one')
# '"none" is derived from "no one"'
'"{0}" is derived from the {1} "{2}"'.format('Etymology', 'Greek',
                                             'ethos')
# '"Etymology" is derived from the Greek "ethos"'
'"{0}" is derived from the {2} "{1}"'.format('December', 'decem', 'Latin')
# '"December" is derived from the Latin "decem"'

 
# Instead of just the index number in the curly braces, 
# you can also indicate the format of the numbers. 

 
my_pi = 3.14159                                         
'Pi rounded to {0} decimal places is {1:.2f}.'.format(2, my_pi)
# 'Pi rounded to 2 decimal places is 3.14.'
'Pi rounded to {0} decimal places is {1:.3f}.'.format(3, my_pi)
# 'Pi rounded to 3 decimal places is 3.142.'
 
# If the index numbers are omitted, the strings are passed
# in order from left to right. 

 
'Pi rounded to {} decimal places is {:.3f}.'.format(3, my_pi)
# 'Pi rounded to 3 decimal places is 3.142.'
 
# You can chain method calls, as long as the previous methods in the chain
# also return strings. 

 
'Computer Science'.swapcase().endswith('ENCE')
# True

 

# The numeric types int and float are also classes. 
# You can access the help by calling help on the name of the type, 
# as in help(int) or by calling help on a member of 
# the class: 

 
help(0)
# Help on int object:

# class int(object)
#  |  int(x=0) -> integer
#  |  int(x, base=10) -> integer
#  |
#  |  Convert a number or string to an integer, or return 0 if no arguments
#  |  are given.  If x is a number, return x.__int__().  For floating point
#  |  numbers, this truncates towards zero.
#  |
#  |  If x is not a number or if base is given, then x must be a string,
#  |  bytes, or bytearray instance representing an integer literal in the
#  |  given base.  The literal can be preceded by '+' or '-' and be surrounded
#  |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
#  |  Base 0 means to interpret the base from the string as an integer literal.
#  |  int('0b100', base=0)
#  |  4
#  |
#  |  Methods defined here:
#  |
#  |  __abs__(self, /)
#  |      abs(self)
#  |
#  |  __add__(self, value, /)
#  |      Return self+value.
#  ...

 




##################################################
## What Are Those Underscores?
##################################################

# Any method bordered by two pairs of underscores is special.
# For example, the string method __add__ is called whenever
# anything is added to a string. 

 
'TTA' + 'GGG'
# 'TTAGGG'
'TTA'.__add__('GGG')
# 'TTAGGG'

 

# Python programmers almost *never* call these special methods directly
# but it helps to understand how Python works.

# Here are some methods for class int:

 
# Help on class int in module builtins:

# class int(object)
# ...
#  |  Methods defined here:
#  |
#  |  __abs__(self, /)
#  |      abs(self)
#  |
#  |  __add__(self, value, /)
#  |      Return self+value.
#  |
#  |  __gt__(self, value, /)
#  |      Return self>value.

 

# Here are several versions of calculating the absolute value of a number, 
# along with a number of other calcualtions. 

 
abs(-3)
# 3
(-3).__abs__()
# 3
-3 .__abs__()
# -3
-(3 .__abs__())
# -3
(-3) .__abs__()
# 3
3 + 5
# 8
3 .__add__(5)
# 8
3 > 5
# False
3 .__gt__(5)
# False
5 > 3
# True
5 .__gt__(3)
# True

 

# Notice the space after 3 between the dot in 3 . when we want to call
# an int method on the integer 3. 
# If the dot were immediately after the 3, Python would mistakenly
# identify 3. as the float 3.0, instead of the int 3.  

 
import math
math.sqrt.__doc__
# 'sqrt(x)\n\nReturn the square root of x.'


# The documentation for functions is stored in a variable called __doc. 


print(math.sqrt.__doc__)
# sqrt(x)

# Return the square root of x.
help(math.sqrt)
# Help on built-in function sqrt in module math:

# sqrt(...)
#     sqrt(x)

#     Return the square root of x.

 










#-------------------------------------------------
### Exercise 12
#-------------------------------------------------

 
def total_occurrences(s1: str, s2: str, ch: str) -> int:
    """Precondition: len(ch) == 1

    Return the total number of times that ch occurs in s1 and s2.

    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')

    >>> total_occurrences('green', 'purple', 'b')

    """

 



##################################################
# End
##################################################




