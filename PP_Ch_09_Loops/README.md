# PP_Ch_9_Loops

# Repeating Code Using Loops

## Processing Items in a List

```python 
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> print('Metric:', velocities[0], 'm/sec;',
... 'Imperial:', velocities[0] * 3.28, 'ft/sec')
Metric: 0.0 m/sec; Imperial: 0.0 ft/sec
>>> print('Metric:', velocities[1], 'm/sec;',
... 'Imperial:', velocities[1] * 3.28, 'ft/sec')
Metric: 9.81 m/sec; Imperial: 32.1768 ft/sec
>>> print('Metric:', velocities[2], 'm/sec; ',
... 'Imperial:', velocities[2] * 3.28, 'ft/sec')
Metric: 19.62 m/sec; Imperial: 64.3536 ft/sec
>>> print('Metric:', velocities[3], 'm/sec; ',
... 'Imperial:', velocities[3] * 3.28, 'ft/sec')
Metric: 29.43 m/sec; Imperial: 96.5304 ft/sec

``` 



```python 
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> for velocity in velocities:
...     print('Metric:', velocity, 'm/sec;',
...     'Imperial:', velocity * 3.28, 'ft/sec')
...
Metric: 0.0 m/sec; Imperial: 0.0 ft/sec
Metric: 9.81 m/sec; Imperial: 32.1768 ft/sec
Metric: 19.62 m/sec; Imperial: 64.3536 ft/sec
Metric: 29.43 m/sec; Imperial: 96.5304 ft/sec

``` 



```python 
>>> speed = 2
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> for speed in velocities:
...     print('Metric:', speed, 'm/sec')
... 
Metric: 0.0 m/sec
Metric: 9.81 m/sec
Metric: 19.62 m/sec
Metric: 29.43 m/sec
>>> print('Final:', speed)
Final: 29.43

``` 


## Processing Characters in Strings

```python 
>>> country = 'United States of America'
>>> for ch in country:
...     if ch.isupper():
...         print(ch)
... 
U
S
A

``` 

## Looping Over a Range of Numbers


```python 
>>> range(10)
range(0, 10)
``` 

```python 
>>> for num in range(10):
...     print(num)
... 
0
1
2
3
4
5
6
7
8
9
``` 


```python 
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


``` 

```python 
>>> list(range(3))
[0, 1, 2]
>>> list(range(1))
[0]
>>> list(range(0))
[]
``` 


```python 
>>> list(range(1, 5))
[1, 2, 3, 4]
>>> list(range(1, 10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(5, 10))
[5, 6, 7, 8, 9]

``` 

```python 
>>> list(range(2000, 2050, 4))
[2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]

``` 

```python 
>>> list(range(2050, 2000, -4))
[2050, 2046, 2042, 2038, 2034, 2030, 2026, 2022, 2018, 2014, 2010, 2006, 2002]

``` 

```python 
>>> list(range(2000, 2050, -4))
[]
>>> list(range(2050, 2000, 4))
[]

``` 

```python 
>>> total = 0
>>> for i in range(1, 101):
...     total = total + i
... 
>>> total
5050

``` 


## Processing Lists Using Indices






```python 
>>> values = [4, 10, 3, 8, -6]
>>> for num in values:
...     num = num * 2
... 
>>> values
[4, 10, 3, 8, -6]
``` 

```python 
>>> values = [4, 10, 3, 8, -6]
>>> for num in values:
...     num = num * 2
...     print(num)
... 
8
20
6
16
-12
>>> print(values)
[4, 10, 3, 8, -6]

``` 






```python 
>>> values = [4, 10, 3, 8, -6]
>>> len(values)
5
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(len(values)))
[0, 1, 2, 3, 4]

``` 

```python 
>>> values = [4, 10, 3, 8, -6]
>>> for i in range(len(values)):
...     print(i)
... 
0
1
2
3
4
``` 

```python 
>>> values = [4, 10, 3, 8, -6]
>>> for i in range(len(values)):
...     print(i, values[i])
... 
0 4
1 10
2 3
3 8
4 -6

``` 

```python 
>>> values = [4, 10, 3, 8, -6]
>>> for i in range(len(values)):
...     values[i] = values[i] * 2
... 
>>> values
[8, 20, 6, 16, -12]
``` 



### Processing Parallel Lists Using Indices


```python 
>>> metals = ['Li', 'Na', 'K']
>>> weights = [6.941, 22.98976928, 39.0983]
``` 




```python 
>>> metals = ['Li', 'Na', 'K']
>>> weights = [6.941, 22.98976928, 39.0983]
>>> for i in range(len(metals)):
...     print(metals[i], weights[i])
... 
Li 6.941
Na 22.98976928
K 39.0983
``` 

## Nesting Loops in Loops



```python 
>>> outer = ['Li', 'Na', 'K']
>>> inner = ['F', 'Cl', 'Br']
>>> for metal in outer:
...     for halogen in inner:
...         print(metal + halogen)
...
...
LiF
LiCl
LiBr
NaF
NaCl
NaBr
KF
KCl
KBr

``` 




```python 
def print_table(n: int) -> None:
    """Print the multiplication table for numbers 1 through n inclusive.

    >>> print_table(5)
        1       2       3       4       5
    1   1       2       3       4       5
    2   2       4       6       8       10
    3   3       6       9       12      15
    4   4       8       12      16      20
    5   5       10      15      20      25
    """
    # The numbers to include in the table.
    numbers = list(range(1, n + 1))

    # Print the header row.
    for i in numbers:
        print('\t' + str(i), end='')

    # End the header row.
    print()

    # Print each row number and the contents of each row.
    for i in numbers:  #(1)

        print (i, end='')  #(2)
        for j in numbers:   #(3)
            print('\t' + str(i * j), end='') #(4)

        # End the current row.
        print() #(5)

``` 



### Looping Over Nested Lists


```python 
>>> elements = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]
>>> for inner_list in elements:
...     print(inner_list)
... 
['Li', 'Na', 'K']
['F', 'Cl', 'Br']

``` 

```python 
>>> elements = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]
>>> for inner_list in elements:
...     for item in inner_list:
...         print(item)
... 
Li
Na
K
F
Cl
Br
``` 





### Looping Over Ragged Lists


```python 
>>> info = [['Isaac Newton', 1643, 1727],
...         ['Charles Darwin', 1809, 1882],
...         ['Alan Turing', 1912, 1954, 'alan@bletchley.uk']]
>>> for item in info:
...     print(len(item))
...
3
3
4

``` 

```python 
>>> drinking_times_by_day = [["9:02", "10:17", "13:52", "18:23", "21:31"],
...                          ["8:45", "12:44", "14:52", "22:17"],
...                          ["8:55", "11:11", "12:34", "13:46",
...                           "15:52", "17:08", "21:15"],
...                          ["9:15", "11:44", "16:28"],
...                          ["10:01", "13:33", "16:45", "19:00"],
...                          ["9:34", "11:16", "15:52", "20:37"],
...                          ["9:01", "12:24", "18:51", "23:13"]]
>>> for day in drinking_times_by_day:
...     for drinking_time in day:
...         print(drinking_time, end=' ')
...     print()
...
9:02 10:17 13:52 18:23 21:31
8:45 12:44 14:52 22:17
8:55 11:11 12:34 13:46 15:52 17:08 21:15
9:15 11:44 16:28
10:01 13:33 16:45 19:00
9:34 11:16 15:52 20:37
9:01 12:24 18:51 23:13
``` 




## Looping Until a Condition is Reached

```python 
>>> rabbits = 3
>>> while rabbits > 0:
...     print(rabbits)
...     rabbits = rabbits - 1
...
3
2
1

``` 

```python 
time = 0
population = 1000   # 1000 bacteria to start with
growth_rate = 0.21 # 21% growth per minute
while population < 2000:
    population = population + growth_rate * population
    print(round(population))
    time = time + 1
	
print("It took", time, "minutes for the bacteria to double.")
print("The final population was", round(population), "bacteria.")

``` 

```python 
1210
1464
1772
2144
It took 4 minutes for the bacteria to double.
The final population was 2144 bacteria.
``` 


### Infinite Loops

```python 
# Use multivalued assignment to set up controls
time, population, growth_rate = 0, 1000, 0.21

# Don't stop until we're exactly double the original size
while population != 2000:
    population = population + growth_rate * population
    print(round(population))
    time = time + 1

print("It took", time, "minutes for the bacteria to double.")

``` 

```python 
1210
1464
1772
2144
...3,680 lines or so later...
inf
inf
inf
...and so on forever...
``` 


## Repetition Based on User Input

```python 
text = ""
while text != "quit":
    text = input("Please enter a chemical formula (or 'quit' to exit): ")
    if text == "quit":
        print("...exiting program")
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")

``` 


```python 
Please enter a chemical formula (or 'quit' to exit): CH4
Methane
Please enter a chemical formula (or 'quit' to exit): H2O
Water
Please enter a chemical formula (or 'quit' to exit): quit
...exiting program

``` 



## Controlling Loops Using ```beark``` and ```continue```

### The ```break``` Statement


```python 
while True:
    text = input("Please enter a chemical formula (or 'quit' to exit): ")
    if text == "quit":
        print("...exiting program")
        break
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")

``` 



```python 
>>> s = 'C3H7'
>>> digit_index = -1 # This will be -1 until we find a digit.
>>> for i in range(len(s)):
...     # If we haven't found a digit, and s[i] is a digit
...     if digit_index == -1 and s[i].isdigit():
...         digit_index = i
...
>>> digit_index
1
``` 


```python 
>>> s = 'C3H7'
>>> digit_index = -1 # This will be -1 until we find a digit.
>>> for i in range(len(s)):
...     # If we find a digit
...     if s[i].isdigit():
...         digit_index = i
...         break  # This exits the loop.
...
>>> digit_index
1
``` 


### The ```continue``` Statement



```python 
>>> s = 'C3H7'                   
>>> total = 0                    
>>> count = 0                    
>>> for i in range(len(s)):      
...     if not s[i].isalpha():
...         total = total + int(s[i])
...         count = count + 1
... 
>>> total
10
>>> count
2

``` 

```python 
>>> s = 'C3H7'
>>> total = 0 # The sum of the digits seen so far.
>>> count = 0 # The number of digits seen so far.
>>> for i in range(len(s)):
...     if s[i].isalpha():
...         continue
...     total = total + int(s[i])
...     count = count + 1
...
>>> total
10
>>> count
2

``` 

### A Warning About ```break``` and ```continue```








## Additional Code Snippets


```python 
def f(a, b, c):
  if a:
    if b:
      print('hi')
    elif c:
      print('bonjour')
    else:
      print('hola')
  else:
    print('Select a language.')

``` 

```python 
def f(a, b, c):
  if a and b:
    print('hi')
  elif a and c:
    print('bonjour')
  elif a:
    print('hola')
  else:
    print('Select a language')

``` 

```python 
Mercury
Venus
Earth
Mars

``` 

```python 
>>> count_fragments('atc', 'gttacgtggatg')
0
>>> count_fragments('gtg', 'gttacgtggatg')

``` 

```python 
def count_fragments(fragment, dna):
    """ (str, str) -> int
    
    Return the number of times fragment occurs in dna.
    
    >>> count_fragments('a', 'actg')
    1
    >>> count_fragments('c', 'cact')
    2
    """
    
    count = -1
    last_match = 0

    while last_match != -1:
        count += 1
        last_match = dna.find(fragment, last_match)
    
    return count

``` 

```python 
>>> count_fragments('gtg', 'gttacgtggatg')
1
>>> count_fragments('gtt', 'gttacgtggatg')
0

``` 

```python 
def count_fragments(fragment, dna):
    """ (string, string) -> int
        
    Return the number of times the given fragment occurs in the string, dna.
    
    >>> count_fragments('a', 'actg')
    1
    >>> count_fragments('c', 'cact')
    2
    """
    
    count = -1
    last_match = 0
    while last_match != -1:
        count += 1
        last_match = dna.find(fragment, last_match + 1)
    return count

``` 


```python 
>>> for x in enumerate('abc'):
...     print(x)
...
(0, 'a')
(1, 'b')
(2, 'c')
>>> for x in enumerate([10, 20, 30]):
...     print(x)
...
(0, 10)
(1, 20)
(2, 30)

``` 

```python 
>>> values = [1, 2, 3]
>>> for pair in enumerate(values):
...     i = pair[0]
...     v = pair[1]
...     values[i] = 2 * v
...
>>> values
[2, 4, 6]

``` 

```python 
>>> values = [1, 2, 3]
>>> for (i, v) in enumerate(values):
...     values[i] = 2 * v
...
>>> values
[2, 4, 6]

``` 

```python 
# Pluto is only 0.002 times the mass of Earth.
Pluto
Mercury
# Mars is half Earth's diameter, but only
#   0.11 times Earth's mass.
Mars
Venus
Earth
Uranus



``` 

```python 
earth_line = 1
file = open("data.txt", "r")
for line in file:
    line = line.strip()
    if line == "Earth":
        break
    earth_line = earth_line + 1
print("Earth is at line", earth_line)

``` 

```python 
entry_number = 1
file = open("planets.txt", "r")
for line in file :
    line = line.strip()
    if line.startswith("#"):
        continue
    if line == "Earth":
        break
    entry_number = entry_number + 1
print("Earth is the {}th-lightest planet.".format(entry_number))

``` 

```python 
entry_number = 1
file = open("data.txt", "r")
for line in file :
    line = line.strip()
    if not line.startswith("#"):
      if line == "Earth":
          break
      entry_number = entry_number + 1
print("Earth is the {}th-lightest planet.".format(entry_number))

``` 

```python 
current_line = 1
earth_line = 0
file = open("data.txt", "r")
for line in file:
    line = line.strip()
    if line == "Earth":
        earth_line = current_line
    current_line = current_line + 1
print("Earth is at line {}".format(earth_line))

``` 

```python 
>>> for c in 'alpha':
...     print(c)
...
a
l
p
h
a

``` 

```python 
import media
lake = media.load_picture('lake.png')
width, height = media.get_width(lake), media.get_height(lake)
for y in range(0, height, 2): # Skip odd-numbered lines
    for x in range(0, width):
        p = media.get_pixel(lake, x, y)
        media.set_color(p, media.black)
media.show(lake)

``` 

```python 
import media
baseball = media.load_picture('baseball.png')
lake = media.load_picture('lake.png')
width, height = media.get_width(baseball), media.get_height(baseball)

for y in range(0, height):
    for x in range(0, width):
        # Position the top-left of the baseball at (50, 25)
        from_p = media.get_pixel(baseball, x, y)
        to_p = media.get_pixel(lake, 50 + x, 25 + y)
        media.set_color(to_p, media.get_color(from_p))
media.show(lake)

``` 

```python 
>>> x, y = 1, 2
>>> x
1
>>> y
2

``` 

```python 
>>> first, second, third = [1, 2, 3]
>>> first
1
>>> second
2
>>> third
3
>>> first, second, third = 'abc'
>>> first
'a'
>>> second
'b'
>>> third
'c'

``` 

```python 
>>> values = [1, 2, 3]
>>> for i in range(len(values)):
...     values[i] = 2 * values[i]
...
>>> values
[2, 4, 6]

``` 

```python 
>>> values = [1, 2, 3]
>>> for i in range(len(values)):
...     values[i] *= 2
...
>>> values
[2, 4, 6]

``` 

```python 
from typing import List

def remove_neg(num_list: List[float]) -> None:
    """Remove the negative numbers from the list num_list.

    >>> numbers = [-5, 1, -3, 2]
    >>> remove_neg(numbers)
    >>> numbers
    [1, 2]
    """

    for item in num_list:
        if item < 0:
            num_list.remove(item)

``` 



```python 
while True:
    formula = input("Please enter a chemical formula: ")
    if formula == "H2O":
        print("Water")
    elif formula == "NH3":
        print("Ammonia")
    elif formula == "CH4":
        print("Methane")
    else:
        print("Unknown compound")

``` 

```python 
Please enter a chemical formula: NH3
Ammonia
Please enter a chemical formula: H2O
Water
Please enter a chemical formula: NaCl
Unknown compound
...

``` 


