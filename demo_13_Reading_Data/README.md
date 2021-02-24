# Chapter 10: Reading Files to Obtain  Data

## Writing Algorithms That Use the File-Reading Techniques

The main reason to use python File I/O techniques in business analytics
is to read unstructured datasets and organize them 
in a form suitable for statistical analysis. 

Although it is nice when your data come in the form of a balanced csv file, 
this is often not the case: 
many forms of data are not organized with your application in mind. 

### Skipping the Header

Many data files begin with a header. 
As shown in the last demo, some files 
begin with a one-line description, 
followed by a header with lines denoted by the ```#``` symbol, 
then the data follows. 

This is an algorithm we might want to follow to read this type of file:

1. Skip the first line in the file.
1. Skip over the comment lines in the file.
1. For each of the remaining lines in the file:
    - Read and process the data on that line. 

The problem with this approach is that we cannot determine whether a line is a comment until we've read it. 
Furthermore, we can read a line only once--
we can't move back, other than starting again from the top. 
We can skip processing the lines ```while``` the line 
begins with ```#``` and process the first one that does not
begin with ```#```. 


This is a better algorithm that we can follow:

1. Skip the first line in the file.
1. For each of the next set of lines in the file:
  - If the line begins with a ```#```, skip to the next line.
  - If the line does not begin with a ```#```, end this loop.
1. For each of the remaining lines in the file:
  - Read and process the data on that line. 

This algorithm essentially works in two stages: 
it first skips over the "boring" lines, 
then it processes the "interesting" lines. 

```python 
from typing import TextIO
from io import StringIO

def skip_header(reader: TextIO) -> str:
    """Skip the header in reader and return the first real piece of data.

    >>> infile = StringIO('Example\\n# Comment\\n# Comment\\nData line\\n')
    >>> skip_header(infile)
    'Data line\\n'
    """

    # Read the description line
    line = reader.readline()

    # Find the first non-comment line
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()

    # Now line contains the first real piece of data
    return line

def process_file(reader: TextIO) -> None:
    """Read and print the data from reader, which must start with a single
    description line, then a sequence of lines beginning with '#', then a
    sequence of data.

    >>> infile = StringIO('Example\\n# Comment\\nLine 1\\nLine 2\\n')
    >>> process_file(infile)
    Line 1
    Line 2
    """

    # Find and print the first piece of data
    line = skip_header(reader).strip()
    print(line)

    # Read the rest of the data
    for line in reader:
        line = line.strip()
        print(line)

if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        process_file(input_file)

``` 

The above file only prints out the relevant lines in the file. 
That is a fine first step to make sure that the algorithm
is processing the files you expect. 

Now let's modify it to perform a simple task. 
The next script finds the smallest value
in any line in the dataset. 
In this case, it finds the smallest number of pelts colected in any single year. 

Note that it starts with the first line as the initial candidate:
it needs one value to make a comparison with the remaining values. 

```python 
from typing import TextIO
import time_series

def smallest_value(reader: TextIO) -> int:
    """Read and process reader and return the smallest value after the
    time_series header.

    >>> infile = StringIO('Example\\n1\\n2\\n3\\n')
    >>> smallest_value(infile)
    1
    >>> infile = StringIO('Example\\n3\\n1\\n2\\n')
    >>> smallest_value(infile)
    1
    """

    line = time_series.skip_header(reader).strip()

    # Now line contains the first data value; this is also the smallest value
    # found so far, because it is the only one we have seen.
    smallest = int(line)

    for line in reader:
        value = int(line.strip())

        # If we find a smaller value, remember it.
        if value < smallest:
            smallest = value

    return smallest

if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        print(smallest_value(input_file))

``` 

Notice that the ```if``` statement can be replaced with something
simpler. 
That is, 

```python
>>> if value < smallest:
...     smallest = value
```

can be replaced with

```python
>>> smallest = min(smallest, value)
```
The value of ```smallest``` only changes when ```value < smallest```. 


### Dealing with Missing Values in Data

Sometimes the number you are interested in is simply not recorded. 
That is, there may be *missing values* in your dataset. 
The file ```hebron.txt``` contains such an example. 

```python 
Coloured fox fur production, Hebron, Labrador, 1834-1839
#Source: C. Elton (1942) "Voles, Mice and Lemmings", Oxford Univ. Press
#Table 17, p.265--266
#remark: missing value for 1836
    55 
   262 
   -   
   102 
   178 
   227 

``` 

If you attempt to process this file with the 
```read_smallest.smallest_value``` function, this is what happens:

```python 
>>> import read_smallest
>>> read_smallest.smallest_value(open('hebron.txt', 'r'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./read_smallest.py", line 16, in smallest_value
    value = int(line.strip())
ValueError: invalid literal for int() with base 10: '-'

``` 
Python throws a ```ValueError``` when it tries to change 
the missing value ```'-'``` to type ```int```. 

The following program corrects for this condition. 



```python 
from typing import TextIO
from io import StringIO
import time_series

def smallest_value_skip(reader: TextIO) -> int:
    """Read and process reader, which must start with a time_series header.
    Return the smallest value after the header.  Skip missing values, which
    are indicated with a hyphen.

    >>> infile = StringIO('Example\\n1\\n-\\n3\\n')
    >>> smallest_value_skip(infile)
    1
    """

    line = time_series.skip_header(reader).strip()
    # Now line contains the first data value; this is also the smallest value
    # found so far, because it is the only one we have seen.
    smallest = int(line)

    for line in reader:
        line = line.strip()
        if line != '-':
            value = int(line)
            smallest = min(smallest, value)

    return smallest

if __name__ == '__main__':
    with open('hebron.txt', 'r') as input_file:
        print(smallest_value_skip(input_file))

``` 


### Processing Whitepace-Delimited Data

So far, our files have had only one number per line. 
Most useful files contain several numbers organized into columns. 
Files differ in terms of the particular way that values 
are separated within a single row. 
Once you know the pattern, you can separate the values within each line. 

Consider the following dataset ```lynx.dat```, 
in which the values are separated by whitespace and 
each value ends with a period. 

```python 
Annual Number of Lynx Trapped, MacKenzie River, 1821-1934
#Original Source: Elton, C. and Nicholson, M. (1942)
#"The ten year cycle in numbers of Canadian lynx",
#J. Animal Ecology, Vol. 11, 215--244.
#This is the famous data set which has been listed before in
#various publications:
#Cambell, M.J. and Walker, A.M. (1977) "A survey of statistical work on
#the MacKenzie River series of annual Canadian lynx trappings for the years
#1821-1934 with a new analysis", J.Roy.Statistical Soc. A 140, 432--436.
  269.  321.  585.  871. 1475. 2821. 3928. 5943. 4950. 2577.  523.   98.        
  184.  279.  409. 2285. 2685. 3409. 1824.  409.  151.   45.   68.  213.        
  546. 1033. 2129. 2536.  957.  361.  377.  225.  360.  731. 1638. 2725.        
 2871. 2119.  684.  299.  236.  245.  552. 1623. 3311. 6721. 4245.  687.        
  255.  473.  358.  784. 1594. 1676. 2251. 1426.  756.  299.  201.  229.        
  469.  736. 2042. 2811. 4431. 2511.  389.   73.   39.   49.   59.  188.        
  377. 1292. 4031. 3495.  587.  105.  153.  387.  758. 1307. 3465. 6991.        
 6313. 3794. 1836.  345.  382.  808. 1388. 2713. 3800. 3091. 2985. 3790.        
  674.   81.   80.  108.  229.  399. 1132. 2432. 3574. 2935. 1537.  529.        
  485.  662. 1000. 1590. 2657. 3396.                                            

``` 
Let's write a program that finds the largest value in this dataset. 

Our algorithm is more complicated than the one that we used to 
read the fox pelt data, which had only one number per line. 
This time, we need an additional loop:


1. Skip the first line in the file.
1. For each of the next set of lines in the file:
  - If the line begins with a ```#```, skip to the next line.
  - If the line does not begin with a ```#```:
    - For each piece of data on the line:
      - Process that piece.
    - Break this loop.
1. For each of the remaining lines in the file:
  - Read the data on that line. 
  - For each piece of data on the line:
    - Process that piece.
    
Because we are performing a similar operation in two places, 
we should write a helper function that processes each line. 

To find the largest value in a dataset, 
we can write a function that finds the largest value in a single line. 

```python 
def find_largest(line):
    """ (str) -> int

    Return the largest value in line, which is a whitespace-delimited string
    of integers that each end with a '.'.

    >>> find_largest('1. 3. 2. 5. 2.')
    5
    """

    # The largest value seen so far.
    largest = -1

    for value in line.split():

        # Remove the trailing period.
        v = int(value[:-1])

        # If we find a larger value, remember it.
        if v > largest:
            largest = v

    return largest

``` 
This fits within the following algorithm. 

1. Skip the first line in the file.
1. For each of the next set of lines in the file:
  - If the line begins with a ```#```, skip to the next line.
  - If the line does not begin with a ```#```:
    - For each piece of data on the line:
      - *Find the largest value in that line.* 
    - Break this loop.
1. For each of the remaining lines in the file:
  - Read the data on that line. 
  - *Find the largest value in that line.* 
  - Compare it to the largest value so far and replace if it is larger. 


```python 
from typing import TextIO
from io import StringIO
import time_series

def find_largest(line: str) -> int:
    """Return the largest value in line, which is a whitespace-delimited string
    of integers that each end with a '.'.

    >>> find_largest('1. 3. 2. 5. 2.')
    5
    """
    # The largest value seen so far.
    largest = -1
    for value in line.split():
        # Remove the trailing period.
        v = int(value[:-1])
        # If we find a larger value, remember it.
        if v > largest:
            largest = v

    return largest

def process_file(reader: TextIO) -> int:
    """Read and process reader, which must start with a time_series header.
    Return the largest value after the header.  There may be multiple pieces
    of data on each line.

    >>> infile = StringIO('Example\\n 20. 3.\\n 100. 17. 15.\\n')
    >>> process_file(infile)
    100
    """

    line = time_series.skip_header(reader).strip()
    # The largest value so far is the largest on this first line of data.
    largest = find_largest(line)

    # Check the rest of the lines for larger values.
    for line in reader:
        large = find_largest(line)
        if large > largest:
            largest = large
    return largest

if __name__ == '__main__':
    with open('lynx.txt', 'r') as input_file:
        print(process_file(input_file))

``` 
With this approach, the code in the function ```process_file``` 
is much more simple--
and simpler functions usually mean fewer errors. 

To illustrate the point, compare this to a single function
that processes the entire file. 

```python 
from typing import TextIO
from io import StringIO

def process_file(reader: TextIO) -> int:
    """Read and process reader, which must start with a time_series header.
    Return the largest value after the header.  There may be multiple pieces
    of data on each line.

    >>> infile = StringIO('Example\\n 20. 3.\\n')
    >>> process_file(infile)
    20
    >>> infile = StringIO('Example\\n 20. 3.\\n 100. 17. 15.\\n')
    >>> process_file(infile)
    100
    """

    # Read the description line
    line = reader.readline()

    # Find the first non-comment line
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()

    # Now line contains the first real piece of data

    # The largest value seen so far in the current line
    largest = -1

    for value in line.split():

        # Remove the trailing period
        v = int(value[:-1])
        # If we find a larger value, remember it
        if v > largest:
            largest = v

    # Check the rest of the lines for larger values
    for line in reader:

        # The largest value seen so far in the current line
        largest_in_line = -1

        for value in line.split():

            # Remove the trailing period
            v = int(value[:-1])
            # If we find a larger value, remember it
            if v > largest_in_line:
                largest_in_line = v

        if largest_in_line > largest:
            largest = largest_in_line
    return largest

if __name__ == '__main__':
    with open('lynx.txt', 'r') as input_file:
        print(process_file(input_file))

``` 

Maybe now you are convinced that the first one is simple. 


### Multiline Records

Let's push the dimensions of the file one step further. 
Sometimes there is too much data to fit using a single line for each measurement. 
With *multiline records*, you can use an additional loop 
to process related values over several lines.


```python 
COMPND      AMMONIA
ATOM      1  N  0.257  -0.363   0.000
ATOM      2  H  0.257   0.727   0.000
ATOM      3  H  0.771  -0.727   0.890
ATOM      4  H  0.771  -0.727  -0.890
COMPND      METHANOL
ATOM      1  C  -0.748  -0.015   0.024
ATOM      2  O  0.558   0.420  -0.278
ATOM      3  H  -1.293  -0.202  -0.901
ATOM      4  H  -1.263   0.754   0.600
ATOM      5  H  -0.699  -0.934   0.609
ATOM      6  H  0.716   1.404   0.137

``` 



```python 
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

``` 



```python 
from typing import TextIO
from io import StringIO

def read_molecule(reader: TextIO) -> list:
    """Read a single molecule from reader and return it, or return None to
    signal end of file.  The first item in the result is the name of the
    compound; each list contains an atom type and the X, Y, and Z coordinates
    of that atom.

    >>> instring = 'COMPND TEST\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> infile = StringIO(instring)
    >>> read_molecule(infile)
    ['TEST', ['N', '0.1', '0.2', '0.3'], ['N', '0.2', '0.1', '0.0']]
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

def read_all_molecules(reader: TextIO) -> list:
    """Read zero or more molecules from reader, returning a list of the
    molecule information.

    >>> cmpnd1 = 'COMPND T1\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> cmpnd2 = 'COMPND T2\\nATOM 1 A 0.1 0.2 0.3\\nATOM 2 A 0.2 0.1 0.0\\nEND\\n'
    >>> infile = StringIO(cmpnd1 + cmpnd2)
    >>> result = read_all_molecules(infile)
    >>> result[0]
    ['T1', ['N', '0.1', '0.2', '0.3'], ['N', '0.2', '0.1', '0.0']]
    >>> result[1]
    ['T2', ['A', '0.1', '0.2', '0.3'], ['A', '0.2', '0.1', '0.0']]
    """

    # The list of molecule information.
    result = []

    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule:  # None is treated as False in an if statement
            result.append(molecule)
        else:
            reading = False
    return result

if __name__ == '__main__':
    molecule_file = open('multimol.pdb', 'r')
    molecules = read_all_molecules(molecule_file)
    molecule_file.close()
    print(molecules)

``` 



## Looking Ahead


```python 
COMPND      AMMONIA
ATOM      1  N  0.257  -0.363   0.000
ATOM      2  H  0.257   0.727   0.000
ATOM      3  H  0.771  -0.727   0.890
ATOM      4  H  0.771  -0.727  -0.890
END
COMPND      METHANOL
ATOM      1  C  -0.748  -0.015   0.024
ATOM      2  O  0.558   0.420  -0.278 
ATOM      3  H  -1.293  -0.202  -0.901
ATOM      4  H  -1.263   0.754   0.600
ATOM      5  H  -0.699  -0.934   0.609
ATOM      6  H  0.716   1.404   0.137 
END

``` 


```python 
from lookahead_2 import read_molecule
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

``` 

```python 
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

``` 









## Additional Code Snippets





```python 
>>> file = open('planets.txt', 'r')
>>> for line in file:
...     line = line.strip()
...     print(len(line))
...
7
5
5
4

``` 

```python 
>>> output_file = open('test.txt', 'w')
>>> type(output_file)
<class '_io.TextIOWrapper'>

``` 

```python 
def read_weather_data(r):
    """ (Read weather data from reader r in fixed-width format.  
    The fields are:
         1   8   YYYYMMDD (date)
         9  14   DDMMSS   (latitude)
        15  20   DDMMSS   (longitude)
        21  26   FF.FFF   (temp, deg. C)
        27  32   FF.FFF   (humidity, %)
        33  38   FF.FFF   (pressure, kPa)
    The result is a list of tuples of tuples, 
	where each tuple of tuples is of the form:
    ((Yr, Mo, Day), (Deg, Min, Sec), (Deg, Min, Sec), (Temp, Hum, Press))
    """
    result = []
    for line in r:
        year = int(line[0:4])
        month = int(line[4:6])
        day = int(line[6:8])
        lat_deg = int(line[8:10])
        lat_min = int(line[10:12])
        lat_sec = int(line[12:14])
        long_deg = int(line[14:16])
        long_min = int(line[16:18])
        long_sec = int(line[18:20])
        temp = float(line[20:26])
        hum = float(line[26:32])
        press = float(line[32:38])
        result.append(((year, month, day),
                       (lat_deg, lat_min, lat_sec),
                       (long_deg, long_min, long_sec),
                       (temp, hum, press)))
    return result

``` 

```python 
def read_weather_data(r):
    """ (Read weather data from reader r in fixed-width format.  
    The field widths are:
        4,2,2   YYYYMMDD (date)
        2,2,2   DDMMSS   (latitude)
        2,2,2   DDMMSS   (longitude)
        6,6,6   FF.FFF   (temp, deg. C; humidity, %; pressure, kPa)
    The result is a list of tuples (not tuples of tuples), 
	where each tuple is of the form:
    (YY, MM, DD, DD, MM, SS, DD, MM, SS, Temp, Hum, Press)"""
    fields = ((4, int), (2, int), (2, int),       # date
              (2, int), (2, int), (2, int),       # latitude
              (2, int), (2, int), (2, int),       # longitude
              (6, float), (6, float), (6, float)) # data
    result = []
    # For each record
    for line in r:
        start = 0
        record = []
        # for each field in the record
        for (width, target_type) in fields:
            # convert the text
            text = line[start:start+width]
            field = target_type(text)
            # add it to the record
            record.append(field)
            # move on
            start += width
        # add the completed record to the result
        result.append(record)
    return result

``` 

```python 
   91.3   11.358  13
   96.3   11.355  12.62
   134.6  16.100  12.97
   135.8  16.315  12.02
   174.9  19.205  12.21
   173.2  20.263  11.9
   161.6  16.885  12.02
   176.8  19.441  12.01
   154.9  17.379  12.08
   159.3  16.028  11.8
   136    15.401  11.82
   108.3  13.518  11.94
   109.1  14.023  11.8
   130    14.442  11.78
   137.5  17.916  11.56
   172.7  17.655  11.55
   180.7  21.990  11.68
   184    20.036  11.61
   162.1  19.224  11.91
   147.4  19.367  11.89
   148.5  16.923  12.03
   152.3  18.413  12.27
   126.2  16.616  12.27
   98.9   14.220  12.05

``` 

```python 
def housing(reader):
    """ (file open for reading) -> tuple of (float, float)

    Return a tuple containing the the differences between the housing starts
    and construction contracts in 1983 and in 1984 from reader.
    """

    # The monthly housing starts, in thousands of units.
    starts = []

    # The construction contracts, in millions of dollars.
    contracts = []

    # Read the file, populating the lists.
    for line in reader:
        start, contract, rate = line.split()
        starts.append(float(start))
        contracts.append(float(contract))

    return (sum(starts[12:24]) - sum(starts[0:12]),
            sum(contracts[12:24]) - sum(contracts[0:12]))

if __name__ == "__main__":
    with open('housing.dat', 'r') as input_file:
        print(housing(input_file))

``` 

```python 
def read_housing_data(r):
    """ Read housing data from reader r, returning lists of starts,
    contracts, and rates."""

    starts = []
    contracts = []
    rates = []

    for line in r:
        start, contract, rate = line.split()
        starts.append(float(start))
        contracts.append(float(contract))
        rates.append(rate)

    return (starts, contracts, rates)

def process_housing_data(starts, contracts):
    """ Return the difference between the housing starts and
    construction contracts in 1983 and in 1984."""

    return (sum(starts[12:24]) - sum(starts[0:12]),
            sum(contracts[12:24]) - sum(contracts[0:12]))

if __name__ == "__main__":
    with open('housing.dat', "r") as input_file:
        starts, contracts, rates = read_housing_data(input_file)

    print(process_housing_data(starts, contracts))

``` 

```python 
inception_file = open('inception.py', 'r')
contents = inception_file.read()
print(contents)

``` 

```python 
inception_file = open('inception_10.py', 'r')
first_ten_chars = inception_file.read(10)
the_rest = inception_file.read()
print("The first 10 characters:", first_ten_chars)
print("The rest of the file:", the_rest)

``` 

```python 
inception_file = open('inception.py', 'r')
inception_contents = inception_file.read()
print(inception_contents)

``` 

```python 
import os
tmp = open('tmp.py', 'r')
print os.path.realpath(tmp.name)

``` 


```python 
>>> file = open("planets.txt", "r")

``` 

```python 
1.3 3.4 4.7
2 4.2 6.2
-1 1 0.0

``` 


```python 
input_file = open("hopedale.txt", "r")

# Skip the first line.
input_file.readline()

# Skip the comments.
line = input_file.readline()
while line.startswith('#'):
	line = input_file.readline()

# Now we want to process the rest of the lines.
for line in input_file:
    line = line.strip()
    print line
input_file.close()

``` 

```python 
input_file = open('hopedale.txt', 'r')
for line in input_file:
    line = line.strip()
    print line
input_file.close()

``` 

```python 
def process_file(filename):
    """ Open, read, and print a file."""

    input_file = open(filename, "r")
    for line in input_file:
        line = line.strip()
        print line
    input_file.close()
if __name__ == "__main__":
    process_file(open('hopedale.txt', 'r'))


``` 

```python 
import sys

def process_file(reader):
    """ Read and print the contents of reader."""

    for line in reader:
        line = line.strip()
        print line

if __name__ == "__main__":
	input_file = open('hopedale.txt', 'r')
    process_file(input_file)
    input_file.close()

``` 

```python 
import sys
import urllib.request

def process_file(reader):
    """ Read and print the contents of reader."""

    for line in reader:
        line = line.strip()
        print(line)

if __name__ == "__main__":
    webpage = urllib.request.urlopen(sys.argv[1])
    process_file(webpage)
    webpage.close()

``` 

```python 
""" Display the lines of data.txt from the given starting line number to the
given end line number.

Usage: read_lines_range.py start_line end_line """

import sys

if __name__ == '__main__':
    
    # get the start and end line numbers
    start_line = int(sys.argv[1])
    end_line = int(sys.argv[2])
    
    # read the lines of the file and store them in a list
    data = open('data.txt', 'r')
    data_list = data.readlines()
    data.close()

    # display lines within start to end range    
    for line in data_list[start_line:end_line]:
        print(line.strip())
        
``` 
