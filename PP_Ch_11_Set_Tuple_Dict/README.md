# PP_Ch_11_Set_Tuple_Dict



```python 
>>> bird_to_observations['canada goose']
3
>>> bird_to_observations['long-tailed jaeger']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'long-tailed jaeger'

``` 

```python 
>>> observations_file = open('observations.txt')
>>> birds_observed = set()
>>> for line in observations_file:              
...     bird = line.strip()                     
...     birds_observed.add(bird)                
... 
>>> birds_observed
{'long-tailed jaeger', 'canada goose', 'northern fulmar', 'snow goose'}

``` 

```python 
from typing import Set, TextIO
from io import StringIO

def observe_birds(observations_file: TextIO) -> Set[str]:
    """Return a set of the bird species listed in observations_file, which has
    one bird species per line.

    >>> infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
    >>> birds = observe_birds(infile)
    >>> 'bird 1' in birds
    True
    >>> 'bird 2' in birds
    True
    >>> len(birds) == 2
    True
    """
    birds_observed = set()
    for line in observations_file:
        bird = line.strip()
        birds_observed.add(bird)

    return birds_observed

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    with open('observations.txt') as observations_file:
        print(observe_birds(observations_file))

``` 

```python 
>>> for species in birds_observed:
...     print(species)
... 
long-tailed jaeger
canada goose
northern fulmar
snow goose
``` 

```python 
>>> observations_file = open('observations.txt')
>>> bird_to_observations = {}
>>> for line in observations_file:
...     bird = line.strip()
...     if bird in bird_to_observations:
...         bird_to_observations[bird] = bird_to_observations[bird] + 1
...     else:
...         bird_to_observations[bird] = 1
... 
>>> observations_file.close()
>>> 
>>> # Print each bird and the number of times it was seen.
... for bird, observations in bird_to_observations.items():
...     print(bird, observations)
... 
snow goose 1
long-tailed jaeger 2
canada goose 5
northern fulmar 1

``` 

```python 
>>> observations_file = open('observations.txt')
>>> bird_to_observations = {}
>>> for line in observations_file:
...     bird = line.strip()
...     bird_to_observations[bird] = bird_to_observations.get(bird, 0) + 1
... 
>>> observations_file.close()
``` 

```python 
>>> sorted_birds = sorted(bird_to_observations.keys())
>>> for bird in sorted_birds:
...     print(bird, bird_to_observations[bird])
...
canada goose 5
long-tailed jaeger 2
northern fulmar 1
snow goose 1

``` 

```python 
>>> bird_to_observations
{'canada goose': 5, 'northern fulmar': 1, 'long-tailed jaeger': 2, 
'snow goose': 1}
>>>
>>> # Invert the dictionary
>>> observations_to_birds_list = {}
>>> for bird, observations in bird_to_observations.items():
...     if observations in observations_to_birds_list:
...         observations_to_birds_list[observations].append(bird)
...     else:
...         observations_to_birds_list[observations] = [bird]
... 
>>> observations_to_birds_list
{1: ['northern fulmar', 'snow goose'], 2: ['long-tailed jaeger'], 
5: ['canada goose']}
``` 

```python 
>>> # Print the inverted dictionary
... observations_sorted = sorted(observations_to_birds_list.keys())
>>> for observations in observations_sorted:
...     print(observations, ':', end=" ")
...     for bird in observations_to_birds_list[observations]:
...         print(' ', bird, end=" ")
...     print()
...
1 :   northern fulmar   snow goose
2 :   long-tailed jaeger
5 :   canada goose

``` 

```python 
from typing import TextIO, Dict
from io import StringIO

def count_birds(observations_file: TextIO) -> Dict[str, int]:
    """Return a set of the bird species listed in observations_file, which has
    one bird species per line.

    >>> infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
    >>> count_birds(infile)
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

``` 

```python 
from typing import TextIO, Dict
from io import StringIO

def count_birds(observations_file: TextIO) -> Dict[str, int]:
    """Return a set of the bird species listed in observations_file, which has
    one bird species per line.

    >>> infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
    >>> count_birds(infile)
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

``` 

```python 
from typing import TextIO, List, Any
from io import StringIO

def count_birds(observations_file: TextIO) -> List[List[Any]]:
    """Return a set of the bird species listed in observations_file, which has
    one bird species per line.

    >>> infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
    >>> count_birds(infile)
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

``` 

```python 
canada goose 5
long-tailed jaeger 2
snow goose 1
northern fulmar 1

``` 

```python 
>>> bird_to_observations = {'snow goose': 33, 'eagle': 9}
>>> del bird_to_observations['snow goose']
>>> bird_to_observations
{'eagle': 9}
>>> del bird_to_observations['gannet']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'gannet'

``` 

```python 
>>> bird_to_observations = {'eagle': 999, 'snow goose': 33}
>>> 'eagle' in bird_to_observations
True
>>> if 'eagle' in bird_to_observations:
...   print('eagles have been seen')
...
eagles have been seen
>>> del bird_to_observations['eagle']
>>> 'eagle' in bird_to_observations
False
>>> if 'eagle' in bird_to_observations:
...   print('eagles have been seen')
...
>>>

``` 

```python 
>>> scientist_to_birthdate = {'Newton' : 1642, 'Darwin' : 1809,
...                           'Turing' : 1912}
>>> scientist_to_birthdate.keys()
dict_keys(['Darwin', 'Newton', 'Turing'])
>>> scientist_to_birthdate.values()
dict_values([1809, 1642, 1912])
>>> scientist_to_birthdate.items()
dict_items([('Darwin', 1809), ('Newton', 1642), ('Turing', 1912)])
>>> scientist_to_birthdate.get('Newton')
1642
>>> scientist_to_birthdate.get('Curie', 1867)
1867
>>> scientist_to_birthdate                  
{'Darwin': 1809, 'Newton': 1642, 'Turing': 1912}
>>> researcher_to_birthdate = {'Curie' : 1867, 'Hopper' : 1906,
...                            'Franklin' : 1920} 
>>> scientist_to_birthdate.update(researcher_to_birthdate)                                    
>>> scientist_to_birthdate
{'Hopper': 1906, 'Darwin': 1809, 'Turing': 1912, 'Newton': 1642,
 'Franklin': 1920, 'Curie': 1867}
>>> researcher_to_birthdate
{'Franklin': 1920, 'Hopper': 1906, 'Curie': 1867}
>>> researcher_to_birthdate.clear()
>>> researcher_to_birthdate
{}

``` 

```python 
keys: dict_keys(['Turing', 'Newton', 'Darwin'])
values: dict_values([1912, 1642, 1809])
items: dict_items([('Turing', 1912), ('Newton', 1642), ('Darwin', 1809)])
get: 1867
after update: {'Curie': 1867, 'Darwin': 1809, 'Franklin': 1920,
'Turing': 1912, 'Newton': 1642, 'Hopper': 1906}
after clear: {}
``` 

```python 
>>> bird_to_observations = {}
>>>
>>> # Add a new key/value pair, 'snow goose': 33.
>>> bird_to_observations['snow goose'] = 33
>>>
>>> # Add a new key/value pair, 'eagle': 999.
>>> bird_to_observations['eagle'] = 999 
>>> bird_to_observations
{'eagle': 999, 'snow goose': 33}
>>>
>>> # Change the value associated with key 'eagle' to 9.
>>> bird_to_observations['eagle'] = 9   
>>> bird_to_observations
{'eagle': 9, 'snow goose': 33}

``` 

```python 
>>> dict1 = {'canada goose': 3, 'northern fulmar': 1}
>>> dict2 = {'northern fulmar': 1, 'canada goose': 3}
>>> dict1 == dict2
True

``` 

```python 
>>> bird_to_observations = {'canada goose': 183, 'long-tailed jaeger': 71,
...     'snow goose': 63, 'northern fulmar': 1}
>>> 'snow goose' in bird_to_observations
True
>>> 183 in bird_to_observations
False

``` 

```python 
>>> scientist_to_birthdate = {'Newton' : 1642, 'Darwin' : 1809,
...                           'Turing' : 1912}
>>> for scientist, birthdate in scientist_to_birthdate.items():
...     print(scientist, 'was born in', birthdate)
... 
Turing was born in 1912
Darwin was born in 1809
Newton was born in 1642

``` 

```python 
{
  'jgoodall'  : {'surname'  : 'Goodall',
                 'forename' : 'Jane',
                 'born'     : 1934,
                 'died'     : None,
                 'notes'    : 'primate researcher',
                 'author'   : ['In the Shadow of Man',
                               'The Chimpanzees of Gombe']},				 
  'rfranklin' : {'surname'  : 'Franklin',
                 'forename' : 'Rosalind',
                 'born'     : 1920,
                 'died'     : 1957,
                 'notes'    : 'contributed to discovery of DNA'},
	
	
   'rcarson'  : {'surname'  : 'Carson',
                 'forename' : 'Rachel',
                 'born'     : 1907,
                 'died'     : 1964,
                 'notes'    : 'raised awareness of effects of DDT',
                 'author'   : ['Silent Spring']}
}

``` 

```python 
>>> set()
set()
``` 

```python 
>>> set([3, 5, 2])
{2, 3, 5}
>>> set([2, 3, 5, 5, 2, 3])    
{2, 3, 5}
``` 

```python 
>>> set([2, 3, 2, 5])
{2, 3, 5}
``` 

```python 
>>> help(hash)
Help on built-in function hash in module builtins:

hash(...)
    hash(object) -> integer

    Return a hash value for the object.  Two objects with the same
    value have the same hash value.  The reverse is not necessarily
    true, but likely.

>>> hash(123)
123
>>> hash('123') # a string
163512108404620371

``` 

```python 
>>> hash(29.45)    
107370935
>>> hash(True) 
1
>>> hash([1, 2, 3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
``` 

```python 
>>> life = (['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0])
>>> life[0] = life[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: object does not support item assignment

``` 

```python 
>>> life = (['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0])
>>> life[0][1] = 80.0
>>> life
(['Canada', 80.0], ['United States', 75.5], ['Mexico', 72.0])

``` 

```python 
>>> observations_file = open('observations.txt')
>>> bird_counts = []                            
>>> for line in observations_file:              
...     bird = line.strip()                     
...     found = False
...     # Find bird in the list of bird counts.
...     for entry in bird_counts:
...         if entry[0] == bird:
...             entry[1] = entry[1] + 1
...             found = True
...     if not found:
...         bird_counts.append([bird, 1])
... 
>>> observations_file.close()
>>> for entry in bird_counts:
...     print(entry[0], entry[1])
... 
canada goose 5
long-tailed jaeger 2
snow goose 1
northern fulmar 1

``` 

```python 
>>> bird_to_observations = {'canada goose': 183, 'long-tailed jaeger': 71,
... 'snow goose': 63, 'northern fulmar': 1}
>>> for bird in bird_to_observations:
...     print(bird, bird_to_observations[bird])
...
canada goose 183
long-tailed jaeger 71
snow goose 63
northern fulmar 1

``` 

```python 
>>> (x, y) = (10, 20)
>>> x
10
>>> y
20
>>> 10, 20
(10, 20)
>>> x, y = 10, 20
>>> x
10
>>> y
20
>>> [[w, x], [[y], z]] = [{10, 20}, [(30,), 40]]
>>> w
10
>>> x
20
>>> y
30
>>> z
40
>>> s1 = 'first'
>>> s2 = 'second'
>>> s1, s2 = s2, s1
>>> s1
'second'
>>> s2
'first'

``` 

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
from typing import TextIO, Tuple, List, Dict
from io import StringIO

Atom = Tuple[str, Tuple[str, str, str]]
CompoundDict = Dict[str, Atom]


def read_molecule(reader: TextIO) -> CompoundDict:
    """Read a single molecule from reader and return it, or return None to
    signal end of file.  The returned dictionary has one key/value pair where
    the key is the name of the compound and the value is a list of Atoms.

    >>> instring = 'COMPND TEST\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> infile = StringIO(instring)
    >>> read_molecule(infile)
    {'TEST': [('N', ('0.1', '0.2', '0.3')), ('N', ('0.2', '0.1', '0.0'))]}
    """

    # If there isn't another line, we're at the end of the file.
    line = reader.readline()
    if not line:
        return None

    # Name of the molecule: "COMPND   name"
    key, name = line.split()

    # Other lines are either "END" or "ATOM num atom_type x y z"
    molecule = {name: []}

    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        else:
            key, num, atom_type, x, y, z = line.split()
            molecule[name].append((atom_type, (x, y, z)))

    return molecule


def read_all_molecules(reader: TextIO) -> CompoundDict:
    """Read zero or more molecules from reader, returning a list of the
    molecule information.

    >>> cmpnd1 = 'COMPND T1\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> cmpnd2 = 'COMPND T2\\nATOM 1 A 0.1 0.2 0.3\\nATOM 2 A 0.2 0.1 0.0\\nEND\\n'
    >>> infile = StringIO(cmpnd1 + cmpnd2)
    >>> result = read_all_molecules(infile)
    >>> result['T1']
    [('N', ('0.1', '0.2', '0.3')), ('N', ('0.2', '0.1', '0.0'))]
    >>> result['T2']
    [('A', ('0.1', '0.2', '0.3')), ('A', ('0.2', '0.1', '0.0'))]
    """

    # The dictionary of molecule information.
    result = {}

    reading = True
    while reading:
        next_molecule = read_molecule(reader)
        if next_molecule:  # None is treated as False in an if statement
            result.update(next_molecule)
        else:
            reading = False
    return result


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    molecule_file = open('multimol.pdb', 'r')
    molecules = read_all_molecules(molecule_file)
    molecule_file.close()
    print(molecules)

``` 

```python 
canada goose
canada goose
long-tailed jaeger
canada goose
snow goose
canada goose
long-tailed jaeger
canada goose
northern fulmar

``` 

```python 
>>> (8)   
8
>>> type((8))
<class 'int'>
>>> (8,)
(8,)
>>> type((8,))
<class 'tuple'>
>>> (5 + 3)
8
>>> (5 + 3,)
(8,)

``` 

```python 
items = {'first': 1, 'second': 2, 'third': 3}
for key, value in items.items():
    print(key, value)

``` 

```python 
first 1
third 3
second 2

``` 

```python 
second 2
third 3
first 1

``` 

```python 
third 3
first 1
second 2

``` 

```python 
>>> set(range(5))
{0, 1, 2, 3, 4}
``` 

```python 
>>> ten = set(range(10))
>>> lows = {0, 1, 2, 3, 4}
>>> odds = {1, 3, 5, 7, 9}
>>> lows.add(9)
>>> lows
{0, 1, 2, 3, 4, 9}
>>> lows.difference(odds)
{0, 2, 4}
>>> lows.intersection(odds)
{1, 3, 9}
>>> lows.issubset(ten)
True
>>> lows.issuperset(odds)
False
>>> lows.remove(0)
>>> lows
{1, 2, 3, 4, 9}
>>> lows.symmetric_difference(odds)
{2, 4, 5, 7}
>>> lows.union(odds)
{1, 2, 3, 4, 5, 7, 9}
>>> lows.clear()
>>> lows
set()

``` 

```python 
>>> odds = set([1, 3, 5, 7, 9])
>>> 9 in odds
True
>>> 8 in odds
False
>>> '9' in odds
False
>>> evens = (0, 2, 4, 6, 8)
>>> 4 in evens
True
>>> 11 in evens
False

``` 

```python 
>>> vowels = {'a', 'e', 'i', 'o', 'u'}
>>> vowels
{'o', 'u', 'a', 'e', 'i'}
>>> vowels.add('y')
>>> vowels
{'u', 'y', 'e', 'a', 'o', 'i'}

``` 

```python 
>>> {'a', 'e', 'i', 'o', 'u'} == {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
True

``` 

```python 
>>> vowels = {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
>>> vowels
{'u', 'o', 'i', 'e', 'a'}

``` 

```python 
>>> set(2, 3, 5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set expected at most 1 arguments, got 3

``` 

```python 
>>> vowels = {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
>>> vowels
{'i', 'a', 'u', 'e', 'o'}
>>> set(vowels)
{'i', 'a', 'u', 'e', 'o'}
>>> set({5, 3, 1})
{1, 3, 5}

``` 

```python 
>>> lows = set([0, 1, 2, 3, 4])
>>> odds = set([1, 3, 5, 7, 9])
>>> lows - odds            # Equivalent to lows.difference(odds)
{0, 2, 4}
>>> lows & odds            # Equivalent to lows.intersection(odds)
{1, 3}
>>> lows <= odds           # Equivalent to lows.issubset(odds)
False
>>> lows >= odds           # Equivalent to lows.issuperset(odds)
False
>>> lows | odds            # Equivalent to lows.union(odds)
{0, 1, 2, 3, 4, 5, 7, 9}
>>> lows ^ odds            # Equivalent to lows.symmetric_difference(odds)
{0, 2, 4, 5, 7, 9}

``` 

```python 
>>> vowels = {'a', 'e', 'i', 'o', 'u'}
>>> vowels
{'a', 'u', 'o', 'i', 'e'}

``` 

```python 
>>> type(vowels)
<class 'set'>
>>> type({1, 2, 3})
<class 'set'>
>>> type({})
<class 'dict'>
>>> set()
set()
>>> type(set())
<class 'set'>

``` 

```python 
>>> S = set()
>>> L = [1, 2, 3]
>>> S.add(L)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'

``` 

```python 
>>> bird_to_observations = {'canada goose': 3, 'northern fulmar': 1}
>>> bird_to_observations
{'northern fulmar': 1, 'canada goose': 3}
>>> bird_to_observations['northern fulmar']
1

``` 

```python 
>>> rock = 'anthracite'
>>> rock[9]
'e'
>>> rock[0:3]
'ant'
>>> rock[-5:]
'acite'
>>> for character in rock[:5]:
...     print(character)
...

a
n
t
h
r

``` 

```python 
>>> bases = ('A', 'C', 'G', 'T')
>>> for base in bases:
...     print(base)
... 
A
C
G
T
``` 

```python 
>>> canada = ['Canada', 76.5]
>>> usa = ['United States', 75.5]
>>> mexico = ['Mexico', 72.0]
>>> life = (canada, usa, mexico)
>>> mexico = ['Mexico', 72.5]
>>> life
(['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0])
>>> life[0][1] = 80.0
>>> canada
['Canada', 80.0]

``` 

