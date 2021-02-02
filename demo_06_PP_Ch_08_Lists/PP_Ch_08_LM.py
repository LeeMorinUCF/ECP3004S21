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
# Demo for Chapter 8: Storing Collections 
# of Data Using Lists
#
##################################################
"""


##################################################
## Storing and Accessing Data in Lists
##################################################

# A list is an ordered collection of zero or more objects. 

# For example, this is a list of the number of whales seen per day
# near the Coal Oil Point Natural Reserve in the two
# weeks starting on February 24, 2008.

whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
whales


# You can select a particular element of the list using square brackets. 
 
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
whales[0]

whales[1]

whales[12]

whales[13]

 
# Notice the relationship between the index numbers 0 to 13
# and the corresponding values from the list. 

# You can't select a value out of range...

whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
whales[1001]

 
# ...unless you reach in the negative direction...
 
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
whales[-1]

whales[-2]

whales[-14]


# ...but don't go too far backwards, either: 
 
whales[-15]

 
# Like any other variable, you can assign individual elements to 
# other variables. 
 
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
third = whales[2]
print('Third day:', third)


#-------------------------------------------------
### The Empty List
#-------------------------------------------------

# Like the empty string, the empty list contains no elements, 

whales = []
 
# so all index numbers are out of range. 
 
whales[0]

whales[-1]



#-------------------------------------------------
### Lists Are Heterogeneous
#-------------------------------------------------

# A list does not have to contain the same type of variables. 

krypton = ['Krypton', 'Kr', -157.2, -153.4]
krypton[1]

krypton[2]

 
# For some programmers with experience in other languages, 
# this is a strange possibility. 
# The user has to be careful to rememeber or check for the types of elements
# to avoid errors. 


##################################################
## Type Annotations for Lists
##################################################

# In type contracts for functions, you can specify that the argument is a list.
 
def average(L: list) -> float:
    """Return the average of the values in L.
...
    >>> average([1.4, 1.6, 1.8, 2.0])
    1.7
    """
    return sum(L)/len(L)

average([1.4, 1.6, 1.8, 2.0])


# You can also explicitly state that the argument is a list *of floats*, 
# using the *capital-L* List from the typing module.
 
from typing import List
def average(L: List[float]) -> float:
    """Return the average of the values in L.
...
    >>> average([1.4, 1.6, 1.8, 2.0])
    1.7
    """
    return sum(L)/len(L)




average([1.4, 1.6, 1.8, 2.0])

average(['1.4', 1.6, 1.8, 2.0])



sum(['1.4', 1.6, 1.8, 2.0])
help(sum)




##################################################
## Modifying Lists
##################################################

# You change the values of lists. That is, lists are *mutable*. 

nobles = ['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']

 
# Notice that 'neon' is spelled incorrectly. 
# You can change it by assigning a new value to that element. 

nobles[1] = 'neon'
nobles

 

# The fact that you can do this illustrates that each element is assigned 
# its own location in memory. 

# Compare this to numbers and strings, which are *immutable*. 

name = 'darwin'
name[0] = 'D'


# Methods that appear to change strings, actually create new ones. 
 
name = 'Darwin'
capitalized = name.upper()
print(capitalized)

print(name)

 
# Methods are similar to functions but are related to a cetain data type. 
# We will loop back to them in Chapter 7. 


##################################################
## Operations on Lists
##################################################

# Some operations, such as len apply to many data types.
# Here are some others that apply to lists. 

 
half_lives = [887.7, 24100.0, 6563.0, 14, 373300.0]
len(half_lives)

max(half_lives)

min(half_lives)

sum(half_lives)

sorted(half_lives)

half_lives


 
# Some operators can be applied to lists:

original = ['H', 'He', 'Li']
final = original + ['Be']
final

 
# Notice that the binary operator + only works when the operands are of the same type.
# A single string is not the same as a list with one element that is a single string.
# That is why the extra element was contained in square brackets.

['H', 'He', 'Li'] + 'Be'   

 
# The * operator works similarly, when compared to strings. 
 
metals = ['Fe', 'Ni']
metals * 3

# You can use the del operator to *delete*
# an element from a list. 

metals = ['Fe', 'Ni']
del metals[0]
metals



#-------------------------------------------------
### The in Operator on Lists
#-------------------------------------------------

# The in operator checks whether an object is an element of the list.
# It returns a Boolean variable that can be used to execute conditional staements. 

nobles = ['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']

gas = input('Enter a gas: ')
# Enter a gas: argon
if gas in nobles:
    print('{} is noble.'.format(gas))



gas = input('Enter a gas: ')
# Enter a gas: nitrogen
if gas in nobles:
    print('{} is noble.'.format(gas))

# It only checks for a single item. For example,

[1, 2] in [0, 1, 2, 3]

# but
 
[1, 2] in [0, [1, 2], 3]


# in which the smaller list [1, 2] is an element of the full list.


##################################################
## Slicing Lists
##################################################

# Some geneticists study types of worm, C. elegans, and refer to 
# them with 3-letter abbreviations. 

 
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
celegans_phenotypes

 
# We can take a *slice* of the list to retain selected values in a smaller list. 
 
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
useful_markers = celegans_phenotypes[0:4]
useful_markers

 
# If you leave out the leading or trailing index number, 
# it will slice either from the beginning or to the end of the list. 

 
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
celegans_phenotypes[:4]
# Same as:
celegans_phenotypes[0:4]

celegans_phenotypes[4:]
celegans_phenotypes[4:len(celegans_phenotypes)]

 
# Leaving both limits blank slices the entire list. 
 
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
celegans_copy = celegans_phenotypes[:]
celegans_phenotypes[5] = 'Lvl'
celegans_phenotypes

celegans_copy

 
# Notice that the command celegans_phenotypes[5] = 'Lvl' command
# did not change celegans_copy, which is a *clone* of the list. 
# Since there is a copy, Python changes the location in memory 
# for celegans_phenotypes[5] once it is changed. 
# Meanwhile, celegans_phenotypes[5] still refers to the original location in memory. 



##################################################
## Aliasing: What's in a Name?
##################################################

# Instead of slicing, you can create an *alias*, which is an alternative name for something. 
# The outcome is different than above. 

 
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
celegans_alias = celegans_phenotypes
celegans_phenotypes[5] = 'Lvl'
celegans_phenotypes

celegans_alias
 

# Note that we dropped the slice [:] when we assigned the alias celegans_alias. 
# As a result, changes made to the original list are also made to the alias.
# The index numbers of the alias still point to the same places in memory as the 
# elements of the original list. 



#-------------------------------------------------
### Mutable Parameters
#-------------------------------------------------


# Consider this example:
# a function that returns a list after removing the last element. 

 
def remove_last_item(L: list) -> list:
    """Return list L with the last item removed.
...
    Precondition: len(L) >= 0
...
    >>> remove_last_item([1, 3, 2, 4])
    [1, 3, 2]
    """
    del L[-1]
    return L


remove_last_item([1, 3, 2, 4])


# Now use it with the following list. 

 
celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
remove_last_item(celegans_markers)

celegans_markers

 
# Notice that the original list was altered:
# the modifications applied to the same places in memory. 

# In fact, for this function, you don't need the return statement to create the
# alias. 
# The function will change the list by accessing the memory locations directly. 

 
def remove_last_item(L: list) -> None:
    """Remove the last item from L.
...
    Precondition: len(L) >= 0
...
    >>> remove_last_item([1, 3, 2, 4])
    """
    del L[-1]



celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
remove_last_item(celegans_markers)
celegans_markers


# If we want to restrict the type of the list, we could use the 
# typing module to specify the type as, say, float. 
# Since this function will work the same for lists of any type, 
# we can explicity state that it applies to lists of Any type.
 
from typing import List, Any
def remove_last_item(L: List[Any]) -> None:
    """Remove the last item from L.
...
    Precondition: len(L) >= 0
...
    >>> remove_last_item([1, 3, 2, 4])
    """
    del L[-1]


celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
remove_last_item(celegans_markers)
celegans_markers

help(remove_last_item)


##################################################
## List Methods
##################################################

# Methods are like functions that operate on 
# specific kinds of objects (see Chapter 6). 
# Here are some examples.
 
colors = ['red', 'orange', 'green']                 
colors.extend(['black', 'blue'])
colors

# Same as:
colors = ['red', 'orange', 'green']                 
colors = colors + ['black', 'blue']
colors
# but that is more work for the computer.
          

colors.append('purple')            
colors

# Not the same as:
# colors.append(['black', 'blue'])     
# colors



colors.insert(2, 'yellow')         
colors

# Same as:
# colors = colors[0:2] + ['yellow'] + colors[2:]


colors.remove('black')                              
colors


# notice that these methods modify the list, instead of creating new lists. 
# See the list on page 142 for a menu of methods to choose from. 
 

##################################################
## Working in a List of Lists
##################################################

# An element of a list can be...another list. 

life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]

# Notice that each single element of the full list is a list in its own right. 
 
life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
life[0]

life[1]

life[2]


# To select elements of the individual lists within the full list, 
# use a second pair of square brackets. 

life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
life[1]

life[1][0]

life[1][1]


# Each of the sublists can be assigned to new variables. 

life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
canada = life[0]
canada

canada[0]

canada[1]


# As for a single list, this creates an alias for that list, 
# unless you take a slice with [:].

life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
canada = life[0]
canada[1] = 80.0
canada

life


# Take a slice instead, if you want them them to be different.
 
life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
canada = life[0][:]
canada[1] = 80.0
canada

life


#-------------------------------------------------
### Where Did My List Go?
#-------------------------------------------------

# It is easy to forget that many list methods return None
# rather than creating and returning a new list. 

colors = 'red orange yellow green blue purple'.split()
colors

sorted_colors = colors.sort()
print(sorted_colors)

colors


# The new variable sorted_colors contains only the value None, 
# returned by the list method sort. 
# The sort operation is performed on the original list, 
# on which the method is applied. 



##################################################
## Exercises
##################################################


#-------------------------------------------------
### Exercise 7
#-------------------------------------------------
 
def same_first_last(L: list) -> bool:
    """Precondition: len(L) >= 2

    Return True if and only if first item of the list is the same as the
    last.

    >>> same_first_last([3, 4, 2, 8, 3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])

    >>> same_first_last([4.0, 4.5])

    """

 

#-------------------------------------------------
### Exercise 8
#-------------------------------------------------
 
def is_longer(L1: list, L2: list) -> bool:
    """Return True if and only if the length of L1 is longer than the length
    of L2.

    >>> is_longer([1, 2, 3], [4, 5])
    True
    >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])

    >>> is_longer(['a', 'b', 'c'], [1, 2, 3]

    """

 
#-------------------------------------------------
### Exercise 10
#-------------------------------------------------


units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]




##################################################
# End
##################################################

