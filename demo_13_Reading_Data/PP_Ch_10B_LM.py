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
# February 22, 2021
# 
##################################################
#
# Demo for Chapter 10: 
# Part B: Reading Files to Obtain Data
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
os.chdir(git_path + 'demo_13_Reading_Data')
# Check that the change was successful.
os.getcwd()




##################################################
## Writing Algorithms That Use the File-Reading Techniques
##################################################

# The main reason to use python File I/O techniques in business analytics
# is to read unstructured datasets and organize them 
# in a form suitable for statistical analysis. 

# Although it is nice when your data come in the form of a balanced csv file, 
# this is often not the case: 
# many forms of data are not organized with your application in mind. 

##################################################
### Skipping the Header
##################################################

# Many data files begin with a header. 
# As shown in the last demo, some files 
# begin with a one-line description, 
# followed by a header with lines denoted by the # symbol, 
# then the data follows. 

# This is an algorithm we might want to follow to read this type of file:

# 1. Skip the first line in the file.
# 2. Skip over the comment lines in the file.
# 3. For each of the remaining lines in the file:
#     - Read and process the data on that line. 

# The problem with this approach is that we cannot determine whether a line is a comment until we've read it. 
# Furthermore, we can read a line only once--
# we can't move back, other than starting again from the top. 
# We can skip processing the lines while the line 
# begins with # and process the first one that does not
# begin with #. 


# This is a better algorithm that we can follow:

# 1. Skip the first line in the file.
# 2. For each of the next set of lines in the file:
#     - If the line begins with a #, skip to the next line.
#     - If the line does not begin with a #, end this loop.
# 3. For each of the remaining lines in the file:
#     - Read and process the data on that line. 

# This algorithm essentially works in two stages: 
# it first skips over the "boring" lines, 
# then it processes the "interesting" lines. 



import time_series

with open('hopedale.txt', 'r') as input_file:
    time_series.process_file(input_file)

# It outputs the contents of hopedale.txt:
# 22
# 29
# 2
# 16
# 12
# 35
# 8
# 83
# 166




# The functions are in a file time_series.py to call these
# functions in other programs using import time_series
# (the functions use files in the *T*ime *S*eries *D*ata *L*ibrary).

# The above file only prints out the relevant lines in the file. 
# That is a fine first step to make sure that the algorithm
# is processing the files you expect. 

# Now let's modify it to perform a simple task. 
# The next script, called read_smallest.py, finds the smallest value
# in any line in the dataset. 
# In this case, it finds the smallest number of pelts colected in any single year. 

# Note that it starts with the first line as the initial candidate:
# it needs one value to make a comparison with the remaining values. 


import read_smallest

with open('hopedale.txt', 'r') as input_file:
    print(read_smallest.smallest_value(input_file))

# This is the smallest value in the file:
# 2



# Notice that the if statement can be replaced with something
# simpler. 
# That is, 


# if value < smallest:
#     smallest = value

# can be replaced with

# smallest = min(smallest, value)


# The value of smallest only changes when value < smallest. 


##################################################
### Dealing with Missing Values in Data
##################################################

# Sometimes the number you are interested in is simply not recorded. 
# That is, there may be *missing values* in your dataset. 
# The file hebron.txt contains such an example. 


# Coloured fox fur production, Hebron, Labrador, 1834-1839
# #Source: C. Elton (1942) "Voles, Mice and Lemmings", Oxford Univ. Press
# #Table 17, p.265--266
# #remark: missing value for 1836
#     55 
#    262 
#    -   
#    102 
#    178 
#    227 


# If you attempt to process this file with the 
# read_smallest.smallest_value function, this is what happens:


import read_smallest
read_smallest.smallest_value(open('hebron.txt', 'r'))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "./read_smallest.py", line 16, in smallest_value
#     value = int(line.strip())
# ValueError: invalid literal for int() with base 10: '-'


# Python throws a ValueError when it tries to change 
# the missing value '-' to type int. 

# The following program read_smallest_w_missing.py corrects for this condition. 


import read_smallest_w_missing

with open('hebron.txt', 'r') as input_file:
    print(read_smallest_w_missing.smallest_value_skip(input_file))

# In this file, the smallest value is:
# 55



# This program still works on the original
# dataset with no missing values.


with open('hopedale.txt', 'r') as input_file:
    print(read_smallest_w_missing.smallest_value_skip(input_file))





##################################################
### Processing Whitepace-Delimited Data
##################################################

# So far, our files have had only one number per line. 
# Most useful files contain several numbers organized into columns. 
# Files differ in terms of the particular way that values 
# are separated within a single row. 
# Once you know the pattern, you can separate the values within each line. 

# Consider the following dataset lynx.dat, 
# in which the values are separated by whitespace and 
# each value ends with a period. 


# Annual Number of Lynx Trapped, MacKenzie River, 1821-1934
# #Original Source: Elton, C. and Nicholson, M. (1942)
# #"The ten year cycle in numbers of Canadian lynx",
# #J. Animal Ecology, Vol. 11, 215--244.
# #This is the famous data set which has been listed before in
# #various publications:
# #Cambell, M.J. and Walker, A.M. (1977) "A survey of statistical work on
# #the MacKenzie River series of annual Canadian lynx trappings for the years
# #1821-1934 with a new analysis", J.Roy.Statistical Soc. A 140, 432--436.
#   269.  321.  585.  871. 1475. 2821. 3928. 5943. 4950. 2577.  523.   98.        
#   184.  279.  409. 2285. 2685. 3409. 1824.  409.  151.   45.   68.  213.        
#   546. 1033. 2129. 2536.  957.  361.  377.  225.  360.  731. 1638. 2725.        
#  2871. 2119.  684.  299.  236.  245.  552. 1623. 3311. 6721. 4245.  687.        
#   255.  473.  358.  784. 1594. 1676. 2251. 1426.  756.  299.  201.  229.        
#   469.  736. 2042. 2811. 4431. 2511.  389.   73.   39.   49.   59.  188.        
#   377. 1292. 4031. 3495.  587.  105.  153.  387.  758. 1307. 3465. 6991.        
#  6313. 3794. 1836.  345.  382.  808. 1388. 2713. 3800. 3091. 2985. 3790.        
#   674.   81.   80.  108.  229.  399. 1132. 2432. 3574. 2935. 1537.  529.        
#   485.  662. 1000. 1590. 2657. 3396.                                            


# Let's write a program that finds the largest value in this dataset. 

# Our algorithm is more complicated than the one that we used to 
# read the fox pelt data, which had only one number per line. 
# This time, we need an additional loop:


# 1. Skip the first line in the file.
# 2. For each of the next set of lines in the file:
#     - If the line begins with a #, skip to the next line.
#     - If the line does not begin with a #:
#         - For each piece of data on the line:
#             - Process that piece.
#             - Break this loop.
# 3. For each of the remaining lines in the file:
#     - Read the data on that line. 
#     - For each piece of data on the line:
#         - Process that piece.
    
# Because we are performing a similar operation in two places, 
# we should write a helper function that processes each line. 

# To find the largest value in a dataset, 
# we can write a function that finds the largest value in a single line. 


import read_largest_modular

read_largest_modular.find_largest('1. 3. 2. 5. 2.')



# This function fits within the following algorithm. 

# 1. Skip the first line in the file.
# 2. For each of the next set of lines in the file:
#     - If the line begins with a #, skip to the next line.
#     - If the line does not begin with a #:
#         - For each piece of data on the line:
#             - *Find the largest value in that line.* 
#             - Break this loop.
# 3. For each of the remaining lines in the file:
#     - Read the data on that line. 
#     - *Find the largest value in that line.* 
#     - Compare it to the largest value so far and replace if it is larger. 


# The following program is saved in the script
# read_largest_modular.py and the reason for the naming convention
# we be more clearly stated below.


import read_largest_modular

with open('lynx.dat', 'r') as input_file:
    print(read_largest_modular.process_file(input_file))



# Check for yourself:
# The largest number in the dataset is
# 6991


# With this approach, the code in the function process_file 
# is much more simple--
# and simpler functions usually mean fewer errors. 
# The script read_largest_modular.py illustrates 
# the modular approach to programming: divide problems into smaller,
# well-defined problems and solve them one at a time. 

# To illustrate the point, compare this to a single function
# that processes the entire file in
# read_largest_single_fn.py. 


import read_largest_single_fn

with open('lynx.dat', 'r') as input_file:
    print(read_largest_single_fn.process_file(input_file))

# More complicated but the answer is the same. 




# Maybe now you are convinced that the first one is simple. 


##################################################
### Multiline Records
##################################################

# Let's push the dimensions of the file one step further. 
# Sometimes there is too much data to fit using a single line for each measurement. 
# With *multiline records*, you can use an additional loop 
# to process related values over several lines.

# The following is a sample of a file pdb_1.txt in a Protein Data Bank (PDB) format
# that describes the arrangements of atoms in ammonia. 



# COMPND      AMMONIA
# ATOM      1  N  0.257  -0.363   0.000
# ATOM      2  H  0.257   0.727   0.000
# ATOM      3  H  0.771  -0.727   0.890
# ATOM      4  H  0.771  -0.727  -0.890
# END

# The first line has the name of the molecule. 
# The next lines list the ID, type, and XYZ coordinates
# of the atoms in the molecule.

# Reading this file, for one molecule, is a simple
# application of the techniques we have used so far. 
# If there are more molecules listed, the file
# (pdb_2.txt)
# becomes more complicated:


# COMPND      AMMONIA
# ATOM      1  N  0.257  -0.363   0.000
# ATOM      2  H  0.257   0.727   0.000
# ATOM      3  H  0.771  -0.727   0.890
# ATOM      4  H  0.771  -0.727  -0.890
# END
# COMPND      METHANOL
# ATOM      1  C  -0.748  -0.015   0.024
# ATOM      2  O  0.558   0.420  -0.278
# ATOM      3  H  -1.293  -0.202  -0.901
# ATOM      4  H  -1.263   0.754   0.600
# ATOM      5  H  -0.699  -0.934   0.609
# ATOM      6  H  0.716   1.404   0.137
# END


# Again, we will tackle this problem by dividing it into smaller problems
# and solving each of those in turn. 
# Our algorithm takes this form:

# 1. While there are more molecules in the file:
#     - Read a molecule from the file
#     - Append it to the list of molecules read so far.

# Simnple enough, except that we need to read from the file 
# to know if there are more molecules left to process.
# Modify the algorithm as follows:



# reading = True
# while reading:
#     Try to read a molecule from the file
#     if there is one:
#         Append it to the list of molecules read so far
#     else: 
#         # Nothing left, so end the loop
#         reading = False



# This algorithm is written into the script read_pdb.py
# (so named because it reads molecules from the *P*rotein *D*ata *B*ase).

import read_pdb

molecule_file = open('pdb_1.txt', 'r')
molecules = read_pdb.read_all_molecules(molecule_file)
molecule_file.close()
print(molecules)

# [['AMMONIA', ['N', '0.257', '-0.363', '0.000'], ['H', '0.257', '0.727', '0.000'], ['H', '0.771', '-0.727', '0.890'], ['H', '0.771', '-0.727', '-0.890']]]



# In this program, the work of reading a single molecule
# has been put in a function of its own that must return False
# if it can't find another molecule in the file.
# To do this, the function checks the first line it tries to read
# to see if there is any data left in the file. 
# If not, it tells read_all_molecules that the end of the file has been reached. 
# Otherwise, it pulls the name of the molecule out of the first line
# and proceeds to read the list of atoms until it reaches the END. 



from typing import TextIO

def read_molecule(reader: TextIO) -> list:
    """Read a single molecule from reader and return it, or return None to
    signal end of file.  The first item in the result is the name of the
    compound; each list contains an atom type and the X, Y, and Z coordinates
    of that atom.
    """

    # If there isn't another line, we're at the end of the file.
    line = reader.readline()
    if not line:
        return None

    # Name of the molecule: "COMPND   name"
    parts = line.split()
    name = parts[1]

    # Other lines are either "END" or "ATOM num atom_type x y z"
    molecule = [name]
    reading = True

    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        else:
            parts = line.split()
            molecule.append(parts[2:])

    return molecule




##################################################
## Looking Ahead
##################################################


# Suppose the the file were slightly more complex:
# the molules are not conveniently separated by the word END. 
# After all, these lines carry no data and, over a large number of molecules, 
# these would take up a large amount of storage space. 

# The next file format simply lists the next molecule with a new 
# COMPND line (in the file pdb_3.txt). 


# COMPND      AMMONIA
# ATOM      1  N  0.257  -0.363   0.000
# ATOM      2  H  0.257   0.727   0.000
# ATOM      3  H  0.771  -0.727   0.890
# ATOM      4  H  0.771  -0.727  -0.890
# COMPND      METHANOL
# ATOM      1  C  -0.748  -0.015   0.024
# ATOM      2  O  0.558   0.420  -0.278
# ATOM      3  H  -1.293  -0.202  -0.901
# ATOM      4  H  -1.263   0.754   0.600
# ATOM      5  H  -0.699  -0.934   0.609
# ATOM      6  H  0.716   1.404   0.137




# At first glance, this may not seem like such a difficulty, 
# but when the program reads the COMPND line insterad of an END line, 
# it is too late to record the name of the next molecule (and all the rest). 




from look_ahead_pdb import read_molecule
from typing import TextIO

def read_all_molecules(reader: TextIO) -> list:
    """Read zero or more molecules from reader,
    returning a list of the molecules read.
    """

    result = []
    line = reader.readline()
    while line:
        molecule, line = read_molecule(reader, line)
        result.append(molecule)

    return result



# This new version of read_all_molecules begins by 
# reading the first line of the file. 
# If the string is not empty (that is, if the file is not empty)
# it passes both the file and the4 line into read_molecule. 
# The new version of read_molecule then has to return two things:
# the next molecule in the file and 
# the first line immediately after the end of that molecule
# (or an empty string if it reaches the end of the file). 


# Now we can modify the read_molecule function. 
# First, it has to check that line is actually the start of a molecule. 
# Then, it reads lines from reader one at a time, 
# looking for one of three situations:
#   - The end of the file, which signals the end of both the molecule and the file.
#   - Another CMPND line, which signals the end of this molecule 
#   and the start of the next one. 
#   - An ATOM, which is to be added to the current molecule. 
  
# The key feature of this revised function is that
# it returns *both* the molecule *and* the next line, 
# so that the caller can keep processing. 



from typing import TextIO

def read_molecule(reader: TextIO, line: str) -> list:
    """Read a molecule from reader, where line refers to the first line of
    the molecule to be read. Return the molecule and the first line after
    it (or the empty string if the end of file has been reached).
    """

    fields = line.split()
    molecule = [fields[1]]


    line = reader.readline()
    while line and not line.startswith('COMPND'):
        fields = line.split()
        if fields[0] == 'ATOM':
            key, num, atom_type, x, y, z = fields
            molecule.append([atom_type, x, y, z])
        line = reader.readline()

    return molecule, line


# Let's place this function in the module look_ahead_pdb
# and test it. 

import look_ahead_pdb


# File 1: AMMONIA only.
molecule_file = open('pdb_1.txt', 'r')
molecules = look_ahead_pdb.read_all_molecules(molecule_file)
molecule_file.close()
print(molecules)

# File 2: AMMONIA and METHANOL.
molecule_file = open('pdb_2.txt', 'r')
molecules = look_ahead_pdb.read_all_molecules(molecule_file)
molecule_file.close()
print(molecules)


# File 3: AMMONIA and METHANOL without END lines.
molecule_file = open('pdb_3.txt', 'r')
molecules = look_ahead_pdb.read_all_molecules(molecule_file)
molecule_file.close()
print(molecules)

# Now our module handles all the cases. 









##################################################
## End
##################################################

