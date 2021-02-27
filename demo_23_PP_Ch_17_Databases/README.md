# PP_Ch_17_Databases

# Databases



```python 
>>> import sqlite3

``` 


## Creating and Populating


```python 
>>> import sqlite3
```

```python 
>>> con = sqlite3.connect('population.db')
``` 

```python 
>>> cur = con.cursor()
``` 


```python 
>>> cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')
<sqlite3.Cursor object at 0x102e3e490>

``` 


```python 
>>> cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.execute('INSERT INTO PopByRegion VALUES("Southeastern Africa", '
...             '743112)')
<sqlite3.Cursor object at 0x102e3e490>
...
>>> cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')
<sqlite3.Cursor object at 0x102e3e490>

``` 


```python 
>>> cur.execute('INSERT INTO PopByRegion VALUES ("Japan", 100562)')

``` 

### Saving Changes


```python 
>>> con.commit()

``` 

### Closing the Connection

```python 
>>> con.close()

``` 





## Retrieving Data


```python 
>>> cur.execute('SELECT Region, Population FROM PopByRegion')

``` 

```python 
>>> cur.fetchone()
('Central Africa', 330993)
``` 


```python 
>>> cur.fetchall()
[('Southeastern Africa', 743112), ('Northern Africa', 1037463), ('Southern
Asia', 2051941), ('Asia Pacific', 785468), ('Middle East', 687630), 
('Eastern Asia', 1362955), ('South America', 593121), ('Eastern Europe',
223427), ('North America', 661157), ('Western Europe', 387933), ('Japan',
100562)]
``` 

```python 
>>> cur.fetchone()
>>> cur.fetchall()
[]
``` 

```python 
>>> cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Region')
>>> cur.fetchall()
[('Asia Pacific', 785468), ('Central Africa', 330993), ('Eastern Asia',
1362955), ('Eastern Europe', 223427), ('Japan', 100562), ('Middle East',
687630), ('North America', 661157), ('Northern Africa', 1037463), ('South
America', 593121), ('Southeastern Africa', 743112), ('Southern Asia', 
2051941), ('Western Europe', 387933)]
``` 

```python 
>>> cur.execute('''SELECT Region, Population FROM PopByRegion
                   ORDER BY Population DESC''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Southern Asia', 2051941), ('Eastern Asia', 1362955), ('Northern Africa',
1037463), ('Asia Pacific', 785468), ('Southeastern Africa', 743112), 
('Middle East', 687630), ('North America', 661157), ('South America',
593121), ('Western Europe', 387933), ('Central Africa', 330993), ('Eastern
Europe', 223427), ('Japan', 100562)]

``` 


```python 
>>> cur.execute('SELECT Region FROM PopByRegion')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Central Africa',), ('Southeastern Africa',), ('Northern Africa',),
 ('Southern Asia',), ('Asia Pacific',), ('Middle East',), ('Eastern
 Asia',), ('South America',), ('Eastern Europe',), ('North America',),
 ('Western Europe',), ('Japan',)]
>>> cur.execute('SELECT * FROM PopByRegion')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Central Africa', 330993), ('Southeastern Africa', 743112), 
 ('Northern Africa', 1037463), ('Southern Asia', 2051941), ('Asia
 Pacific', 785468), ('Middle East', 687630), ('Eastern Asia', 1362955),
 ('South America', 593121), ('Eastern Europe', 223427), ('North America',
 661157), ('Western Europe', 387933), ('Japan', 100562)]

``` 


### Query Conditions

```python 
>>> cur.execute('SELECT Region FROM PopByRegion WHERE Population > 1000000')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Northern Africa',), ('Southern Asia',), ('Eastern Asia',)]

``` 


```python 
>>> cur.execute('''SELECT Region FROM PopByRegion
                   WHERE Population > 1000000 AND Region < "L"''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Eastern Asia',)]

``` 


## Updating and Deleting


```python 
>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchone()
('Japan', 100562)
>>> cur.execute('''UPDATE PopByRegion SET Population = 100600
                   WHERE Region = "Japan"''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchone()
('Japan', 100600)

``` 



```python 
>>> cur.execute('DELETE FROM PopByRegion WHERE Region < "L"')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.execute('SELECT * FROM PopByRegion')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Southeastern Africa', 743112), ('Northern Africa', 1037463),
 ('Southern Asia', 2051941), ('Middle East', 687630), ('South America',
 593121), ('North America', 661157), ('Western Europe', 387933)])]

``` 


```python 
>>> cur.execute('INSERT INTO PopByRegion VALUES (?, ?)', ("Japan", 100562))
``` 



```python 
>>> cur.execute('DROP TABLE PopByRegion')

``` 


## Using ```NULL``` for Missing Data



```python 
>>> cur.execute('INSERT INTO PopByRegion VALUES ("Mars", NULL)')

``` 

```python 
>>> cur.execute('CREATE TABLE Test (Region TEXT NOT NULL, '
...             'Population INTEGER)')

``` 


```python 
>>> cur.execute('INSERT INTO Test VALUES (NULL, 456789)')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    cur.execute('INSERT INTO Test VALUES (NULL, 456789)')
sqlite3.IntegrityError: Test.Region may not be NULL


``` 




## Using Joins to Combine Tables



```python 
>>> cur.execute('''CREATE TABLE PopByCountry(Region TEXT, Country TEXT, 
                   Population INTEGER)''')

``` 


```python 
>>> cur.execute('''INSERT INTO PopByCountry VALUES("Eastern Asia", "China", 
                   1285238)''') 

``` 


```python 
>>> countries = [("Eastern Asia", "DPR Korea", 24056), ("Eastern Asia", 
"Hong Kong (China)", 8764), ("Eastern Asia", "Mongolia", 3407), ("Eastern 
Asia", "Republic of Korea", 41491), ("Eastern Asia", "Taiwan", 1433), 
("North America", "Bahamas", 368), ("North America", "Canada", 40876), 
("North America", "Greenland", 43), ("North America", "Mexico", 126875), 
("North America", "United States", 493038)]
>>> for c in countries:
...   cur.execute('INSERT INTO PopByCountry VALUES (?, ?, ?)', (c[0], c[1], c[2]))
... 
>>> con.commit()

``` 



```python 
import sqlite3 as dbapi

con = dbapi.connect('pop.db')
cur = con.cursor()

cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')

cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')
cur.execute('INSERT INTO PopByRegion VALUES("Southeastern Africa", 743112)')
cur.execute('INSERT INTO PopByRegion VALUES("Northern Africa", 1037463)')
cur.execute('INSERT INTO PopByRegion VALUES("Southern Asia", 2051941)')
cur.execute('INSERT INTO PopByRegion VALUES("Asia Pacific", 785468)')
cur.execute('INSERT INTO PopByRegion VALUES("Middle East", 687630)')
cur.execute('INSERT INTO PopByRegion VALUES("Eastern Asia", 1362955)')
cur.execute('INSERT INTO PopByRegion VALUES("South America", 593121)')
cur.execute('INSERT INTO PopByRegion VALUES("Eastern Europe", 223427)')
cur.execute('INSERT INTO PopByRegion VALUES("North America", 661157)')
cur.execute('INSERT INTO PopByRegion VALUES("Western Europe", 387933)')
cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')

con.commit()

cur.execute('CREATE TABLE PopByCountry(Region TEXT, Country TEXT, Population INTEGER)')

countries = [("Eastern Asia", "China", 1285238), ("Eastern Asia", "DPR Korea", 24056), ("Eastern Asia", "Hong Kong (China)", 8764), ("Eastern Asia", "Mongolia", 3407), ("Eastern Asia", "Republic of Korea", 41491), ("Eastern Asia", "Taiwan", 1433), ("North America", "Bahamas", 368), ("North America", "Canada", 40876), ("North America", "Greenland", 43), ("North America", "Mexico", 126875), ("North America", "United States", 493038)]
             
for c in countries:
    cur.execute('INSERT INTO PopByCountry VALUES (?, ?, ?)', (c[0], c[1],
                c[2]))

con.commit()
``` 



```python 
>>> cur.execute('''
SELECT PopByRegion.Region, PopByCountry.Country 
FROM   PopByRegion INNER JOIN PopByCountry 
WHERE  (PopByRegion.Region = PopByCountry.Region) 
AND    (PopByRegion.Population > 1000000)
''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Eastern Asia', 'China'), ('Eastern Asia', 'DPR Korea'), 
('Eastern Asia', 'Hong Kong (China)'), ('Eastern Asia', 'Mongolia'), 
('Eastern Asia', 'Republic of Korea'), ('Eastern Asia', 'Taiwan')]

``` 

### Removing Duplicates


```python 
>>> cur.execute('''
SELECT PopByRegion.Region
FROM PopByRegion INNER JOIN PopByCountry
WHERE (PopByRegion.Region = PopByCountry.Region)
AND ((PopByCountry.Population * 1.0) / PopByRegion.Population > 0.10)''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Eastern Asia',), ('North America',), ('North America',)]
``` 


```python 
>>> cur.execute('''
SELECT DISTINCT PopByRegion.Region
FROM PopByRegion INNER JOIN PopByCountry
WHERE (PopByRegion.Region = PopByCountry.Region)
AND ((PopByCountry.Population * 1.0) / PopByRegion.Population > 0.10)''')
>>> cur.fetchall()
[('Eastern Asia',), ('North America',)]

``` 



## Keys and Constraints


```python 
>>> cur.execute('''CREATE TABLE PopByRegion (
                   Region TEXT NOT NULL, 
                   Population INTEGER NOT NULL, 
                   PRIMARY KEY (Region))''')
``` 


```python 
>>> cur.execute('''
    CREATE TABLE PopByCountry(
    Region TEXT NOT NULL,
    Country TEXT NOT NULL,
    Population INTEGER NOT NULL,
    CONSTRAINT CountryKey PRIMARY KEY (Region, Country))''')


``` 


## Advanced Features

### Aggregation



```python 
>>> cur.execute('SELECT SUM (Population) FROM PopByRegion')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchone()
(8965762,)

``` 


### Grouping



```python 
>>> cur.execute('''SELECT Region, SUM (Population) FROM PopByCountry
                   GROUP BY Region''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Eastern Asia', 1364389), ('North America', 661200)]

``` 



```python 
>>> cur.execute('''SELECT SUM (Population) FROM PopByCountry 
                   WHERE Region = "North America"''')
<sqlite3.Cursor object at 0x102a3bb20>
>>> cur.fetchall()
[(661200,)]
>>> cur.execute('''SELECT SUM (Population) FROM PopByCountry
                   WHERE Region = "Eastern Asia"''')
<sqlite3.Cursor object at 0x102a3bb20>
>>> cur.fetchall()
[(1364389,)]
``` 


### Self-Joins




```python 
>>> cur.execute('''SELECT Country FROM PopByCountry 
                   WHERE (ABS(Population - Population) < 1000)''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('China',), ('DPR Korea',), ('Hong Kong (China)',), ('Mongolia',), 
('Republic of Korea',), ('Taiwan',), ('Bahamas',), ('Canada',), 
('Greenland',), ('Mexico',), ('United States',)]

``` 

```python 
>>> cur.execute('''
SELECT A.Country, B.Country 
FROM   PopByCountry A INNER JOIN PopByCountry B 
WHERE  (ABS(A.Population - B.Population) <= 1000)
AND    (A.Country != B.Country)''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Republic of Korea', 'Canada'), ('Bahamas', 'Greenland'), ('Canada',
'Republic of Korea'), ('Greenland', 'Bahamas')]

``` 

### Nested Queries


```python 
>>> cur.execute('''SELECT DISTINCT Region 
                   FROM PopByCountry 
                   WHERE (PopByCountry.Population != 8764)''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Eastern Asia',), ('North America',)]

``` 

```python 
>>> cur.execute('''
SELECT DISTINCT Region 
FROM PopByCountry 
WHERE (PopByCountry.Population = 8764)
''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Eastern Asia',)

``` 

```python 
>>> cur.execute('''
SELECT DISTINCT Region 
FROM PopByCountry 
WHERE Region NOT IN 
    (SELECT DISTINCT Region 
     FROM PopByCountry 
     WHERE (PopByCountry.Population = 8764))
''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('North America',)]

``` 

### Transactions

```python 
cur.execute('SELECT SignedOut FROM Books WHERE ISBN = ?', isbn)
signedOut = cur.fetchone()[0]
cur.execute('''UPDATE Books SET SignedOut = ? 
               WHERE ISBN = ?''', signedOut + 1, isbn)
cur.commit()

``` 

```python 
cur.execute('SELECT SignedOut FROM Books WHERE ISBN = ?', isbn)
signedOut = cur.fetchone()[0]
cur.execute('''UPDATE Books SET SignedOut = ? 
               WHERE ISBN = ?''', signedOut - 1, isbn)
cur.commit()

``` 



```python 
Computer A: cur.execute('SELECT SignedOut FROM Books WHERE ISBN = ?', isbn)
Computer A: signedOut = cur.fetchone()[0]
Computer B: cur.execute('SELECT SignedOut FROM Books WHERE ISBN = ?', isbn)
Computer B: signedOut = cur.fetchone()[0]
Computer A: cur.execute('''UPDATE Books SET SignedOut = ? 
                           WHERE ISBN = ?''', signedOut + 1, isbn)
Computer A: cur.commit()
Computer B: cur.execute('''UPDATE Books SET SignedOut = ? 
                           WHERE ISBN = ?''', signedOut - 1, isbn)
Computer B: cur.commit()

``` 




