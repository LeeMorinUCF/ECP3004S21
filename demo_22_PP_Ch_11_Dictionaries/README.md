

# Chapter 12: Dictionaries

## Storing Data Using Dictionaries

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
>>> bird_to_observations = {'canada goose': 3, 'northern fulmar': 1}
>>> bird_to_observations
{'northern fulmar': 1, 'canada goose': 3}
```

```
>>> bird_to_observations['northern fulmar']
1

```


```python
>>> bird_to_observations['canada goose']
3
>>> bird_to_observations['long-tailed jaeger']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'long-tailed jaeger'

```



```python
>>> dict1 = {'canada goose': 3, 'northern fulmar': 1}
>>> dict2 = {'northern fulmar': 1, 'canada goose': 3}
>>> dict1 == dict2
True

```

### Updating and Checking Membership



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

### Looping Over Dictionaries


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


### Dictionary Operations


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
>>> scientist_to_birthdate = {'Newton' : 1642, 'Darwin' : 1809,
...                           'Turing' : 1912}
>>> for scientist, birthdate in scientist_to_birthdate.items():
...     print(scientist, 'was born in', birthdate)
...
Turing was born in 1912
Darwin was born in 1809
Newton was born in 1642

```

#### Dictionaries, Key Order, and Versions of Python


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



### Dictionary Example


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


### Inverting a Dictionary


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


## Using the ```in``` Operator on Dictionaries




```python
>>> bird_to_observations = {'canada goose': 183, 'long-tailed jaeger': 71,
...     'snow goose': 63, 'northern fulmar': 1}
>>> 'snow goose' in bird_to_observations
True
>>> 183 in bird_to_observations
False

```

## Creating New Type Annotations



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





