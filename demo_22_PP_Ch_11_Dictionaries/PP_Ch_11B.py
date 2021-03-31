# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Dictionaries in Python
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business Administration
# University of Central Florida
#
# March 31, 2021
# 
# Chapter 11: Storing Data Using Other Collection Types
# Part B: Dictionaries
# 
##################################################
"""

##################################################
# Import Modules.
##################################################


import os # To set working directory

##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
git_path = 'C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\'
os.chdir(git_path + 'demo_22_PP_Ch_11_Dictionaries')
# Check that the change was successful.
os.getcwd()




##################################################
# Example: Organizing Tabulated Data
##################################################

# Before studying databases, let's talk about dictionaries. 
# Recall this example of the following birds observed in the Arctic.


# canada goose
# canada goose
# long-tailed jaeger
# canada goose
# snow goose
# canada goose
# long-tailed jaeger
# canada goose
# northern fulmar


# The biologists have listed these observations
# in the file observations.txt. 
# Now we want to know how often a specimen of each species was seen. 
# We could use a list of lists: for each item in the lists, 
# item 0 is the species of bird
# and item 1 is the number of sightings of that species of bird. 
# You could record this list as follows:
# - Start with an empty list.
# - Loop over the species names in the list.
# - If the next name does not appear in the list, create a new entry with count 1.
# - If the next name appears in the list, increment the count for that species.


from typing import TextIO, List, Any
from io import StringIO

def count_birds(observations_file: TextIO) -> List[List[Any]]:
    """Return a set of the bird species listed in observations_file, which has
    one bird species per line.

    infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
    count_birds(infile)
    [['bird 1', 2], ['bird 2', 1]]
    """
    bird_counts = []
    for line in observations_file:
        bird = line.strip()
        found = False
        # Find bird in the list of bird counts.
        for entry in bird_counts:
            if entry[0] == bird:
                entry[1] = entry[1] + 1
                found = True
        if not found:
            bird_counts.append([bird, 1])

    return bird_counts

if __name__ == '__main__':
    with open('observations.txt') as observations_file:
        bird_counts = count_birds(observations_file)

        # Print each bird and the number of times it was seen
        for entry in bird_counts:
            print(entry[0], entry[1])



# The above program did just that and produced the following list: 


# canada goose 5
# long-tailed jaeger 2
# snow goose 1
# northern fulmar 1



# The algorithm uses a boolean variable found, 
# which is originally set to False. 
# It then searches through the list and if it does not change 
# to True, as it increments one of the counts, 
# it appends the new record with count 1. 

# This is fine for a simple problem but there are two things wrong with it:
# 1. For the simplicity of the problem, the program is fairly complex. 
#   The more loops and if statements involved, the greater the chance that you make a mistake. 
# 2. This solution does not scale well: 
#   for each addition it has to search over the entire list.
#   There are only thousands of species of birds but if we were studying beetles,
#   there would be millions of species to loop over. 
#   This algorithm gets slower and slower as the list grows. 

# A dictionary is the right tool for the job. 
# In some languages it is known as a *map*. 
# Whatever you call it, it is an 
# *unordered, mutable collection of key/value pairs*. 
# The keys form a set: any key can appear at most once in the dictionary.
# Like the elements in sets, the keys are immutable,
# although the values that are associated with the keys don't have to be. 

# In Python, you define a dictionary by putting key:value pairs inside braces, 
# with the pairs separated by a comma. 


bird_to_observations = {'canada goose': 3, 'northern fulmar': 1}
bird_to_observations
# {'northern fulmar': 1, 'canada goose': 3}


# Notice the naming convention for the dictionary itself.
# It is common to use a name of the form keyname_to_valuename.

# To get the value associated with a key, 
# we put the key in square brackets, 
# much like indexing into a list. 


bird_to_observations['northern fulmar']
# 1



# You might remember this sort of notation when referring 
# to columns of data in a data frame. 
# Note that indexing a dictionary with a key that doesn't exist 
# will produce an error much like that from an out-of-range index for a list. 



bird_to_observations['canada goose']
# 3

bird_to_observations['long-tailed jaeger']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'long-tailed jaeger'


# The empty dictionary is written {}
# and this is why we can't use this notation for empty sets, 
# which we did with the set()function. 

# As with sets, dictionaries are unordered:


dict1 = {'canada goose': 3, 'northern fulmar': 1}
dict2 = {'northern fulmar': 1, 'canada goose': 3}
dict1 == dict2
# True



# Dictionaries can be compared much like any other pair of data types. 


##################################################
### Updating and Checking Membership
##################################################

# Typically, dictionaries are accumulated over several operations, 
# rather than defined in one command.
# You can add key:value pairs or check that they exist. 

# To update the value associated with a key, 
# you update it as you would for a list, 
# except you use a key instead of an index. 
# If the key is already in the dictionary, 
# this assignment statement changes the value associated 
# with that key. 
# If the key is not present in the dictionary, 
# the key:value pair is added. 



bird_to_observations = {}

# Add a new key/value pair, 'snow goose': 33.
bird_to_observations['snow goose'] = 33

# Add a new key/value pair, 'eagle': 999.
bird_to_observations['eagle'] = 999
bird_to_observations
# {'eagle': 999, 'snow goose': 33}

# Change the value associated with key 'eagle' to 9.
bird_to_observations['eagle'] = 9
bird_to_observations
# {'eagle': 9, 'snow goose': 33}


# To delete an entry from a dictionary, 
# use the del d[k] command, 
# where d is the name of the dictionary 
# and k is the name of the key of the entry to be deleted. 
# This operation also works just as it does on data frames. 


bird_to_observations = {'snow goose': 33, 'eagle': 9}
del bird_to_observations['snow goose']
bird_to_observations
# {'eagle': 9}

del bird_to_observations['gannet']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'gannet'



# To test whether a key is in a dictionary, 
# we can use the in operator.


bird_to_observations = {'eagle': 999, 'snow goose': 33}
'eagle' in bird_to_observations
# True


if 'eagle' in bird_to_observations:
  print('eagles have been seen')

# eagles have been seen


del bird_to_observations['eagle']
'eagle' in bird_to_observations
# False

if 'eagle' in bird_to_observations:
  print('eagles have been seen')

# (Nothing prints out.)



# The in operator only checks the keys of the dictionary. 


33 in bird_to_observations
# False

# The number 33 is a value, not a key. 


##################################################
### Looping Over Dictionaries
##################################################

# Like other collections of data, 
# you can loop over the entries in a dictionary.
# In the loop, the iterator is assigned each key 
# from the dictionary in turn. 


bird_to_observations = {'canada goose': 183, 'long-tailed jaeger': 71, 
                        'snow goose': 63, 'northern fulmar': 1}

for bird in bird_to_observations:
    print(bird, bird_to_observations[bird])

# canada goose 183
# long-tailed jaeger 71
# snow goose 63
# northern fulmar 1


# Within the loop, you can access the asociated values
# easily using the key. 


##################################################
### Dictionary Operations
##################################################

# Like lists, tuples and sets, dictionaries are objects
# endowed with operations and methods.
# Here are some examples. 


scientist_to_birthdate = {'Newton' : 1642, 'Darwin' : 1809,
                          'Turing' : 1912}
scientist_to_birthdate.keys()
# dict_keys(['Darwin', 'Newton', 'Turing'])


scientist_to_birthdate.values()
# dict_values([1809, 1642, 1912])


scientist_to_birthdate.items()
# dict_items([('Darwin', 1809), ('Newton', 1642), ('Turing', 1912)])

scientist_to_birthdate.get('Newton')
# 1642

scientist_to_birthdate.get('Curie', 1867)
# 1867

scientist_to_birthdate
# {'Darwin': 1809, 'Newton': 1642, 'Turing': 1912}






researcher_to_birthdate = {'Curie' : 1867, 'Hopper' : 1906,
                           'Franklin' : 1920}
scientist_to_birthdate.update(researcher_to_birthdate)
scientist_to_birthdate
# {'Hopper': 1906, 'Darwin': 1809, 'Turing': 1912, 'Newton': 1642,
#  'Franklin': 1920, 'Curie': 1867}

researcher_to_birthdate
# {'Franklin': 1920, 'Hopper': 1906, 'Curie': 1867}

researcher_to_birthdate.clear()
researcher_to_birthdate
# {}


# See Table 16 on page 219 of *Practical Programming*
# for more options. 


# One common operation is to loop on both the keys 
# and the values at the same time.



scientist_to_birthdate = {'Newton' : 1642, 'Darwin' : 1809,
                          'Turing' : 1912}
for scientist, birthdate in scientist_to_birthdate.items():
    print(scientist, 'was born in', birthdate)

# Turing was born in 1912
# Darwin was born in 1809
# Newton was born in 1642


# In this loop there are two iterators moving in parallel
# through the entries of the dictionary. 


##################################################
#### Dictionaries, Key Order, and Versions of Python
##################################################

# Prior to Python 3.6, 
# when iterating over the keys of a dictionary, 
# the keys were unordered. 
# Consider this program:


items = {'first': 1, 'second': 2, 'third': 3}
for key, value in items.items():
    print(key, value)


# Running it three times in Python 3.5
# obtained the following results.

# Run 1:

# first 1
# third 3
# second 2


# Run 2:

# second 2
# third 3
# first 1



# Run 3:

# third 3
# first 1
# second 2


# In versions of Python 3.6 and beyond, 
# the way in which dictionaries are stored has a side effect:
# the keys always come out in the same order. 
# As of right now, the language designers have warned
# that we should not rely on this ordering, 
# although it may become a guaranteed feature in future versions. 

# In keeping with this advice, none of the examples 
# in the book *Practical Programming* rely on the key order in a dictionary. 
# I think that this is good advice because it would be incredibly difficult 
# to troubleshoot a problem based on a surprise change in ordering.


##################################################
### Dictionary Example
##################################################

# We started this section with a crude approach
# to cataloguing our bird-watching research using lists.
# Now let's revisit this example using a dictionary. 

# We start with an empty dictionary. 
# Each time we read an observation in the file, 
# we check if we have seen that species before, 
# i.e. if the bird already has a key in the dictionary.
# If so, we increment the count for that species. 
# If the bird species is not already recorded in the dictionary, 
# we add a new entry with a 1 for the value. 

# Here is a program that does the job 
# (notice the type annotation for dictionaries):


from typing import TextIO, Dict
from io import StringIO

def count_birds(observations_file: TextIO) -> Dict[str, int]:
    """Return a set of the bird species listed in observations_file, which has
    one bird species per line.

    infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
    count_birds(infile)
    {'bird 1': 2, 'bird 2': 1}
    """
    bird_to_observations = {}
    for line in observations_file:
        bird = line.strip()
        if bird in bird_to_observations:
            bird_to_observations[bird] = bird_to_observations[bird] + 1
        else:
            bird_to_observations[bird] = 1

    return bird_to_observations

if __name__ == '__main__':
    with open('observations.txt') as observations_file:
        bird_to_observations = count_birds(observations_file)
        for bird, observations in bird_to_observations.items():
            print(bird, observations)


# Note that this is much more concise than the version with lists. 
# It is also easy to understand. Recall the description before the program:

# "We start with an empty dictionary. 
# Each time we read an observation in the file, 
# we check if we have seen that species before, 
# i.e. if the bird already has a key in the dictionary.
# If so, we increment the count for that species. 
# If the bird species is not already recorded in the dictionary, 
# we add a new entry with a 1 for the value."

# The lines of the program exactly correspond 
# to the English-language description of the algorithm. 

# We can shorten it further by using the method dict.get, 
# saving three more lines.


from typing import TextIO, Dict
from io import StringIO

def count_birds(observations_file: TextIO) -> Dict[str, int]:
    """Return a set of the bird species listed in observations_file, which has
    one bird species per line.

    infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
    count_birds(infile)
    {'bird 1': 2, 'bird 2': 1}
    """
    bird_to_observations = {}
    for line in observations_file:
        bird = line.strip()
        bird_to_observations[bird] = bird_to_observations.get(bird, 0) + 1

    return bird_to_observations

if __name__ == '__main__':
    with open('observations.txt') as observations_file:
        bird_to_observations = count_birds(observations_file)
        for bird, observations in bird_to_observations.items():
            print(bird, observations)


# Using the get method does make the program shorter but 
# to go this far is a matter of taste. 
# Some programmers find it harder to understand at a glance and
# would prefer a program that is more clear, if only a few lines longer. 
# In business, this is usually a more important consideration. 
# You want your code to work in the hands of another junior analyst, 
# so that you can work on another project. 
# Your employer wants your code to survive long after you have left the company. 


##################################################
### Inverting a Dictionary
##################################################

# Maybe you want to print the values of a dictionary in another order:
# in the order of the values.
# This is what it means to *invert* the dictionary. 
# You can create a new dictionary in which you use
# the values as keys
# and the keys as values. 

# This is tricky because there is no guarantee that the values are unique.
# When there are duplicate values in the inversion, 
# these are known as *collisions*. 
# For example, if you invert the dictionary 
# {'a': 1, 'b': 1, 'c' 1}, a key would be 1
# but it's not clear what value ('a', 'b', or 'c') would be associated with it. 

# Since you'd like to preserve all of the data from the original dictionary, 
# you may need to use another type of collection, 
# such as a list, 
# to keep track of the values associated with a key. 
# In the short example above, you might record the key:value pair
# {1: ['a', 'b', 'c']}. 
# Here is a program to convert the dictionary of birds to 
# a dictionary of observation numbers and the birds observed in those numbers. 


bird_to_observations
# {'canada goose': 5, 'northern fulmar': 1, 'long-tailed jaeger': 2,
# 'snow goose': 1}


# Invert the dictionary
observations_to_birds_list = {}
for bird, observations in bird_to_observations.items():
    if observations in observations_to_birds_list:
        observations_to_birds_list[observations].append(bird)
    else:
        observations_to_birds_list[observations] = [bird]

observations_to_birds_list
# {1: ['northern fulmar', 'snow goose'], 2: ['long-tailed jaeger'],
# 5: ['canada goose']}


# This program loops over the key:value pairs.
# If that value is not yet a key in the dictionary, 
# it is added to the new dictionary with a single-element list
# with the new species name. 
# If the value is already a key, the new value of the inverted dictionary
# will be a list with one more element, the new species. 

# Now that the dictionary is inverted, 
# you can print each key and all the items in its value list. 


# Print the inverted dictionary
observations_sorted = sorted(observations_to_birds_list.keys())
for observations in observations_sorted:
    print(observations, ':', end=" ")
    for bird in observations_to_birds_list[observations]:
        print(' ', bird, end=" ")
    print()

# 1 :   northern fulmar   snow goose
# 2 :   long-tailed jaeger
# 5 :   canada goose


# The outer loop passes over each key in the inverted dictionary
# and the inner loop passes over the list of the items in the values list 
# associated with that key. 




##################################################
# End
##################################################
