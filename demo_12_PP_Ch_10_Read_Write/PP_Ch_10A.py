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
# Part A: Reading and Writing Text Files
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
os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\demo_12_PP_Ch_10_Read_Write\\file_examples')
# Check that the change was successful.
os.getcwd()



##################################################
## Opening a File
##################################################


# First, let's create a simple file. 
# Create a folder called file_examples. 
# We created a file in a text editor with the following contents
# and save it as file_example.txt.


# First line of text.
# Second line of text.
# Third line of text.


# Now let's read this file. 


file = open('file_example.txt', 'r')
contents = file.read()
file.close()
print(contents)


# This code block makes a connection to the file file_example.txt
# and reads those contents in one string. 
# It closes the connection and prints those contents to screen. 


# First line of text.
# Second line of text.
# Third line of text.


#--------------------------------------------------
### The with Statement
#--------------------------------------------------

# The above method 
# file_1 = open('data/data1.txt', 'r') 
# works, most of the time, but when an error occurs, the program will not execute
# the file.close()command to release the file from memory. 
# If your program throws an error between the openand close
# statements, this file connection will remain in memory, 
# creating a drag on performance. 

# To avoid this problem, use the with statement. 


with open('file_example.txt', 'r') as file:
    contents = file.read()

print(contents)


# This has the format of any other kind of indented code block, 
# in which the relevant statements are indented beyond the withkeyword. 
# With this approach, if an error occurs, the block terminates and
# the file connection will automatically be released from memory.


##################################################
## Techniques for Reading Files
##################################################

# Once you have made a connection to a file, 
# there are a number of ways to read the contents. 

#--------------------------------------------------
### The read Technique
#--------------------------------------------------

# With the read technique, 
# you read the entire contents of the file into a single string. 

# We used this method above with 


with open('file_example.txt', 'r') as file:
    contents = file.read()

print(contents)


# Clearly, for very large files, this can consume a lot of memory. 
# It is often better to read the contents in smaller chunks. 
# If an integer is passed to read, 
# it will read that specified number of characters. 


with open('file_example.txt', 'r') as example_file:
    first_ten_chars = example_file.read(10)
    the_rest = example_file.read()

print("The first 10 characters:", first_ten_chars)
print("The rest of the file:", the_rest)



#--------------------------------------------------
### The readlines Technique
#--------------------------------------------------

# Instead of reading by the character, 
# which may not be a convenient unit to work with, 
# since you might not even know how many characters you need at a time, 
# you can get the contents of the file organized 
# into separate lines with the readlines function.


with open('file_example.txt', 'r') as example_file:
    lines = example_file.readlines()

print(lines)


# It gives a list of strings, each one containing a newline (\n) escape sequence. 

# Now consider the file planets.txt that contains the following text. 


# Mercury
# Venus
# Earth
# Mars

# This code block reads the file, 
# prints the contents in a list and then loops through that list 
# in reverse order using the built-in function reversed. 


with open('planets.txt', 'r') as planets_file:
    planets = planets_file.readlines()
planets



for planet in reversed(planets):
    print(planet.strip())



# You can perform other operations on this list, 
# such as sorting the lines first. 

with open('planets.txt', 'r') as planets_file:
    planets = planets_file.readlines()
planets



for planet in sorted(planets):
    print(planet.strip())



#--------------------------------------------------
### The for line in file Technique
#--------------------------------------------------

# Often, it is useful to process the contents of a file
# one line at a time. The for line in filetechnique
# lets you read a file with the functionality of a forloop
# and the efficiency of working with the contents one line at a time. 


with open('planets.txt', 'r') as data_file:
    for line in data_file:
        print(len(line))




# This allows you to perform arbitrary calculations using each line in sequence. 
# You can combine any other commands, potentially stripping away whitespace first. 


with open('planets.txt', 'r') as data_file:
    for line in data_file:
        print(len(line.strip()))



#--------------------------------------------------
### The readline Technique
#--------------------------------------------------

# Sometimes you want to perform different operations 
# depending on the characteristics of the file. 
# You could use a series of if and elif statements. 
# Instead, you can instruct the python interpreter to 
# read a single line of the file, without following a pattern, 
# using the readline technique. 

# For example, consider the following dataset, contained in
# the file hopedale.txt. 


# Coloured fox fur production, HOPEDALE, Labrador, 1834-1842
# #Source: C. Elton (1942) "Voles, Mice and Lemmings", Oxford Univ. Press
# #Table 17, p.265--266
#       22   
#       29   
#        2   
#       16   
#       12   
#       35   
#        8   
#       83   
#      166   


# Notice that the first line is a description:
# it is a record of the number of fur pelts harvested 
# in a region of Canada over a period of several years during the 1800's. 
# The next two are preceeded by a # character
# and the data begin on the fourth line.
# The following code block reads in the data
# and skips over the description in the header. 
# The following script calculates the total number of fur pelts. 


with open('hopedale.txt', 'r') as hopedale_file:

    # Read and skip the description line.
    hopedale_file.readline()

    # Keep reading and skipping comment lines until we read the first piece
    # of data.
    data = hopedale_file.readline().strip()
    while data.startswith('#'):
        data = hopedale_file.readline().strip()
        # Do nothing because these lines do not have data.

    # Now we have the first piece of data.  
    # Accumulate the total number of pelts.
    # Convert the string to an integer for the first value in the sum.
    total_pelts = int(data)

    # Read the rest of the data.
    for data in hopedale_file:
        total_pelts = total_pelts + int(data.strip())

print("Total number of pelts:", total_pelts)








# We could perform any other calculations with the lines of data, as follows.


with open('hopedale.txt', 'r') as hopedale_file:

    # Read and skip the description line.
    hopedale_file.readline()

    # Keep reading and skipping comment lines until we read the first piece
    # of data.
    data = hopedale_file.readline().rstrip()
    while data.startswith('#'):
        data = hopedale_file.readline().rstrip()

    # Now we have the first piece of data.
    print(data)

    # Read the rest of the data.
    for data in hopedale_file:
        print(data.rstrip())




# Notice the numbers are aligned
# because we stripped the whitespace only on the right side, 
# using the rstrip() function. 


##################################################
## Files Over the Internet
##################################################

# The above examples assume the file is located on our computer system. 
# You can read file located on any computer that is available on the Internet.

# The urllibmodule has tools for reading files with a given URL.
# Note that the file can be encoded in a number of ways. 
# This example shows how to read a file encoded in UTF-8. 
# This uses a function called decodeto decode the file content 
# in the form of bytes to obtain legible characters using UTF-8 encoding. 



import urllib.request
url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        print(line)





##################################################
## Writing Files
##################################################

# The with statement can also be used for writing files. 
# Let's move to another directory for writing. 

os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\demo_12_PP_Ch_10_Read_Write\\new_files')
# Check that the change was successful.
os.getcwd()



with open('topics.txt', 'w') as output_file:
    output_file.write('Computer Science')

# In the above example, the file topics.txt need not exist:
# this file will be created if it does not exist
# and it will be overwritten if it does exist. 
# The distinction from reading files is shown by the second argument. 
# The 'w' denotes *writing*, while, in the earlier examples, 
# the argument 'r' indicated that the existing file
# would be open for *reading*. 

# If the file already exists and you want to write additional content, 
# you can pass the argument 'a' to *append*. 


with open('topics.txt', 'a') as output_file:
    output_file.write('Software Engineering')



# After running this, look at the contents of the new file:
# You should see

# Computer ScienceSoftware Engineering


# Note that a new line was not automatically added;
# you have to include it manually using \n. 


# The next example is more complex: it both reads from and writes to a file.
# It also uses the typing.TextIO type annotation for the file. 
# The acronym "IO" is short for "Input/Output"

# This script defines a function that reads two numbers from an input_file
# and writes those numbers, with their sum, in output_file. 


from typing import TextIO
from io import StringIO

def sum_number_pairs(input_file: TextIO, output_file: TextIO) -> None:
    """Read the data from input_file, which contains two floats per line
    separated by a space. output_file for writing and, for each line in
    input_file, write a line to output_file that contains the two floats from
    the corresponding line of input_file plus a space and the sum of the two
    floats.
    """

    for number_pair in input_file:
        number_pair = number_pair.strip()
        operands = number_pair.split()
        total = float(operands[0]) + float(operands[1])
        new_line = '{0} {1}\n'.format(number_pair, total)
        output_file.write(new_line)



if __name__ == '__main__':
    with open('number_pairs.txt', 'r') as input_file, \
            open('number_pair_sums.txt', 'w') as output_file:
        sum_number_pairs(input_file, output_file)



# Notice that the files are already open in the main program. 
# This way, the open files are passed to the function 
# sum_number_pairs and are ready to read and write. 

# Also note that the first "line" of the __main__ program
# wraps into the second line, with two with statements.


# If the input_file called number_pairs.txt contains this content,

# 1.3 3.4
# 2 4.2
# -1 1


# then, after running sum_number_pairs,
# the output_file called number_pair_sums.txt will contain the following. 


# 1.3 3.4 4.7
# 2 4.2 6.2
# -1 1 0.0



##################################################
## Writing Example Calls Using StringIO
##################################################

# So far, we have used the function design recipe to test our files as we write them.
# This can be problematic for functions that read and write files
# because the exampple files must be passed along with the scripts, 
# in order for your user to be able to learn from the examples. 

# Python provides a class called StringIO in module io that 
# creates a *mock* open file that you can work with 
# as if it were a real file. 
# These StringIO objects can be used anywhere that TextIO
# objects are expected. 

# In the next example, we create a StringIOobject
# containing the same information as the file number_pairs.txt above. 
# The we read the first line as if it were read from the file. 

# from io import StringIO
input_string = '1.3 3.4\n2 4.2\n-1 1\n'
infile = StringIO(input_string)
infile.readline()


# We can also write to StringIOobjects as if they were files. 
# Then we can read their contents as strings using the method getvalue.


from io import StringIO
outfile = StringIO()
outfile.write('1.3 3.4 4.7\n')

outfile.write('2 4.2 6.2\n')


outfile.write('-1 1 0.0\n')

# Now get the values back from the mock file. 
outfile.getvalue()


# Now we can augment our sum_number_pairs function with some examples. 


from typing import TextIO
from io import StringIO


def sum_number_pairs(input_file: TextIO, output_file: TextIO) -> None:
    """Read the data from input_file, which contains two floats per line
    separated by a space. output_file for writing and, for each line in
    input_file, write a line to output_file that contains the two floats from
    the corresponding line of input_file plus a space and the sum of the two
    floats.

    >>> infile = StringIO('1.3 3.4\\n2 4.2\\n-1 1\\n')
    >>> outfile = StringIO()
    >>> sum_number_pairs(infile, outfile)
    >>> outfile.getvalue()
    '1.3 3.4 4.7\\n2 4.2 6.2\\n-1 1 0.0\\n'
    """

    for number_pair in input_file:
        number_pair = number_pair.strip()
        operands = number_pair.split()
        total = float(operands[0]) + float(operands[1])
        new_line = '{0} {1}\n'.format(number_pair, total)
        output_file.write(new_line)




if __name__ == '__main__':
    with open('number_pairs.txt', 'r') as input_file, \
            open('number_pair_sums.txt', 'w') as output_file:
        sum_number_pairs(input_file, output_file)




##################################################
# End
##################################################
