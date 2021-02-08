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
# January 19, 2021
# 
##################################################
#
# Demo for Chapter 6: A Modular Approach 
# to Program Organization
# Part A: Using Modules
#
##################################################
"""


# You can often solve problems by using programs 
# and functions designed by others, rather than solving these 
# problems on your own. 
# A great advantage of Python is that there is a large community 
# of programmers who contribute their own functions.
# The typical unit for a set of functions and programs is a *module*. 


##################################################
## Importing Modules
##################################################

# To gain access to the functions in a module, you *import* it.

 
import math

# The math module contains a set of mathematical operations. 
# A module has type module.
 
type(math)
# <class 'module'>
 
# You can acces the help for all the functions in a module just as you
# would for a single function, with the help function. 

 
help(math)
# Help on module math:

# NAME
#     math

# MODULE REFERENCE
#     https://docs.python.org/3.6/library/math

#     The following documentation is automatically generated from the Python
#     source files.  It may be incomplete, incorrect or include features that
#     are considered implementation detail and may vary between Python
#     implementations.  When in doubt, consult the module reference at the
#     location listed above.

# DESCRIPTION
#     This module is always available.  It provides access to the
#     mathematical functions defined by the C standard.

# FUNCTIONS
#     acos(...)
#         acos(x)
#         Return the arc cosine (measured in radians) of x.

#     acosh(...)
#         acosh(x)
#         Return the inverse hyperbolic cosine of x.

# [Lots of other functions not shown here.]

 

# Many common functions--many functions that you might expect would come 
# standard with Python--are not available unless you import them
# in a module,

 
sqrt(9)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'sqrt' is not defined

 
# After the import math statement, these functions are available
# using the prefix math. 

 
math.sqrt(9)
# 3.0

 
# Even the number pi requires the math module, 
# along with other constants. 

 
import math
math.pi
# 3.141592653589793
radius = 5
print('area is', math.pi * radius ** 2)
# area is 78.53981633974483

 

# You *could* overwrite these values, since they are variables 
# like any other, but that is a bad idea, since users would not expect this. 


 
import math
math.pi = 3 # DON'T do this!
radius = 5
print('area is', math.pi * radius ** 2)
# area is 75

 
# You don't need to import the entire module. 
# You could import only the particular functions and constants that you need. 
# When you use the from statement, it pulls certain elements
# by name. 

 
from math import sqrt, pi
sqrt(9)
# 3.0
radius = 5
print('circumference is', 2 * pi * radius)
# circumference is 31.41592653589793

 
# Now these can be referenced as they are named. 
# Since they have different names, there are no functions under the
# usual name that would be assigned if the entire module were imported. 

 
from math import sqrt, pi
math.sqrt(9)
# Traceback (most recent call last):
#   File "<pyshell#12>", line 1, in <module>
#     math.sqrt(9)
# NameError: name 'math' is not defined
sqrt(9)
# 3.0
 

# You can name functions or constants with 
# different names than they are called in the modules.
# Use the "as" keyword to assign new names.
from math import pi as other_pi
print(other_pi)




# A good practice is to select only the functions you need. 
# Otherwise, if you select all the functions (using the *wildcard* *)
# many functions will be imported into the namespace, 
# which could cause conflicts with other variables. 


 
from math import *
print(sqrt(8))
# 2.8284271247461903

# Now you can use all of the functions in module math.
print(exp(0))

print(exp(1))
 


#-------------------------------------------------
#### Module __builtins__
#-------------------------------------------------

# Many functions are built into Python. 
# These are collected within the __builtins__ module. 
# You might recognize some of the functions that we have used already. 

 
dir(__builtins__)
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
# 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
# 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
# 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
# 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
# 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning',
# 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError',
# 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError',
# 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError',
# 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
# 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning',
# 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError',
# 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration',
# 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit',
# 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
# 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
# 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError',
# 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__',
# '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all',
# 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr',
# 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict',
# 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float',
# 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex',
# 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license',
# 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct',
# 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed',
# 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum',
# 'super', 'tuple', 'type', 'vars', 'zip']

 

# You should avoid naming any variable using the names of functions in 
# the __builtins__ module. 








##################################################
# End
##################################################

