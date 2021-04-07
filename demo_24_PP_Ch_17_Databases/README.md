
# Chapter 17: Databases


## Advanced Features

The primary use of databases is to organize and retrieve data. 
In practice, you often want to retrieve the data to perform some sort of calculation
and it is often worthwhile to perform these calculations on the computer system
that contains the database. 
Servers typically have much more computing power than your PC or laptop, 
so it is best to do any calculations you can on a server
and then transfer only a small dataset to your computer. 




### Aggregation

We have already encountered an instance of aggregation:
the ```SUM``` is the most basic form of aggregation. 

This command calculates the sum of the population, tabulated by Region.

```python
>>> cur.execute('SELECT SUM (Population) FROM PopByRegion')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchone()
(8965762,)

```

We can restrict the calculation to North America
with a ```WHERE``` clause.

```python
>>> cur.execute('''SELECT SUM (Population) FROM PopByCountry
                   WHERE Region = "North America"''')
>>> cur.fetchall()
<sqlite3.Cursor object at 0x102e3e490>
[(661200,)]
```

and similarly for Eastern Asia.

```python
>>> cur.execute('''SELECT SUM (Population) FROM PopByCountry
                   WHERE Region = "Eastern Asia"''')
>>> cur.fetchall()
<sqlite3.Cursor object at 0x102e3e490>
[(1364389,)]
```



There exist several other commands, as in the following table.

| Aggregate Function | Description
| ------------------ | -----------------------------
| AVG                | Average of the values
| MIN                | Minimum value
| MAX                | Maximum value
| COUNT              | Number of non-NULL values
| SUM                | Sum of the values

There are many others that you might find online. 
Note that the syntax may vary, depending
on the dialect of SQL. 


### Grouping


Sometimes you want to tabulate results by category. 
Aggregation commands can pass through a ```GROUP BY``` clause
to perform a series of aggregate calculations by category. 

Using the ```GROUP BY``` command, we can tabulate the sum of the population,
for every category of ```Region```. 


```python
>>> cur.execute('''SELECT Region, SUM (Population) FROM PopByCountry
                   GROUP BY Region''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Eastern Asia', 1364389), ('North America', 661200)]

```



### Self-Joins

Now, let's consider the problem of comparing some values from a table
to other values drawn from the same table. 
This can be achieved using a *self-join*. 
You treat two instances of tables drawn from the same root table
as separate tables that can be joined together, 
as you could with any other pair of tables. 

Suppose we want to find pairs of countries whose populations 
are close to each other--say, within 1,000 of each other. 

Our first attempt might look like this: 


```python
>>> cur.execute('''SELECT Country FROM PopByCountry
                   WHERE (ABS(Population - Population) < 1000)''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('China',), ('DPR Korea',), ('Hong Kong (China)',), ('Mongolia',),
('Republic of Korea',), ('Taiwan',), ('Bahamas',), ('Canada',),
('Greenland',), ('Mexico',), ('United States',)]

```

This is not what was wanted, for two reasons: 
- First, the phrase ```SELECT Country``` is going to return only one country per record, but we want pairs of countries.
- Second, Second, the expression 
```(ABS(Population - Population) < 1000)``` is always going to return zero
because it compares every population agains itself, line-by-line. 
Since they will all be zero, the query will return all the country names in the table. 


What we want to do is compare the population in each row with the populations 
of countries in other rows. 
To do this, we need to join ```PopByCountry``` with itself using an ```INNER JOIN```. 

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

Notice that we used the absolute value function ```ABS()```. 
Without this, the ```WHERE``` clause would also return other pairs
of countries where the second country is much larger than the first, 
i.e. where the difference ```A.Population - B.Population``` would be negative. 


### Nested Queries


Instead of pulling from a table, you can replace
the name of a table with a query that produces the required table.

Example: Select the list of regions that do not have
a country with a population of 8,764,000.

To make the example more clear, 
let's remind ourselves what region that might be. 

```python
>>> cur.execute('''SELECT *
                   FROM PopByCountry''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Eastern Asia', 'China', 1285238),
 ('Eastern Asia', 'DPR Korea', 24056),
 ('Eastern Asia', 'Hong Kong (China)', 8764),
 ('Eastern Asia', 'Mongolia', 3407),
 ('Eastern Asia', 'Republic of Korea', 41491),
 ('Eastern Asia', 'Taiwan', 1433),
 ('North America', 'Bahamas', 368),
 ('North America', 'Canada', 40876),
 ('North America', 'Greenland', 43),
 ('North America', 'Mexico', 126875),
 ('North America', 'United States', 493038)]

```
When you include the ```WHERE``` clause to exclude Hong Kong, 
it also excludes Hong Kong from the list of countries in that region. 

```python
>>> cur.execute('''SELECT *
                   FROM PopByCountry
                   WHERE (PopByCountry.Population != 8764)''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Eastern Asia', 'China', 1285238),
 ('Eastern Asia', 'DPR Korea', 24056),
 ('Eastern Asia', 'Mongolia', 3407),
 ('Eastern Asia', 'Republic of Korea', 41491),
 ('Eastern Asia', 'Taiwan', 1433),
 ('North America', 'Bahamas', 368),
 ('North America', 'Canada', 40876),
 ('North America', 'Greenland', 43),
 ('North America', 'Mexico', 126875),
 ('North America', 'United States', 493038)]

```

However, when you try to obtain the list of regions, 
it still includes Eastern Asia
because the other countries in Eastern Asia
do not match the exclusion condition. 


```python
>>> cur.execute('''SELECT DISTINCT Region
                   FROM PopByCountry
                   WHERE (PopByCountry.Population != 8764)''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Eastern Asia',), ('North America',)]

```


As an intermediate step, create a query that creates a table that
lists the Regions that do have a country with a population of 8,764,000.


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

Then nest this query in the place of a table 
within a nested query. 

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

The bracketed expression is a query that produces a table, 
which is then passed to the nesting query, 
much like the way you pass a calculated expression as an argument 
to another function.


### Transactions

A *transaction* is a series of database operations that are interdependent. 
No operation can be committed unless every single operation 
can be successfully be committed in sequence. 

For example, processing payroll involves pairs of transactions: 
withdrawing funds from the employer's account 
and depositing funds in the employee's account. 
By grouping the operations into a transaction, 
it is guaranteed that either both operations occur or neither one does. 
If the transaction fails, 
all operations must be *rolled back*. 

Imagine that a library has multiple copies of the same book. 
It uses a computerized system to track its books by ISBN number. 
When a patron signs out a book,
a query is executed on the ```Books``` table to find out
how many copies of the book are currently signed out
and updates the count by one more copy. 

```python
cur.execute('SELECT SignedOut FROM Books WHERE ISBN = ?', isbn)
signedOut = cur.fetchone()[0]
cur.execute('''UPDATE Books SET SignedOut = ?
               WHERE ISBN = ?''', signedOut + 1, isbn)
cur.commit()

```
When a patron returns a book, the reverse happens. 

```python
cur.execute('SELECT SignedOut FROM Books WHERE ISBN = ?', isbn)
signedOut = cur.fetchone()[0]
cur.execute('''UPDATE Books SET SignedOut = ?
               WHERE ISBN = ?''', signedOut - 1, isbn)
cur.commit()

```
What if the library had two computers that handled book sign-outs and returns?
Both computers would be connected to the same database. 
What would happen if one computer tried to process a return while the other was
trying to sign out a copy of the same book at the same time? 
Computer A might send a query to count the number of books avaiable
just before computer B, which will get the same value. 
After computer A updates the count, computer B updates the count again, 
without taking into account the transaction from Computer A, 
which was done after Computer B sent the query. 
The result is that the database only reflects 
the transaction from Computer B. 


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
Fortunately, databases can detect such a pair of transactions and 
would prevent Computer B from committing its transaction. 



## Examples

### Example 1: Population, Area and Population Density of Provinces

In this example, we will create a table 
to store the population and land area of the provinces and
territories of Canada, according to the 2001 census with Statistics Canada. 



a. Create a new database called ```census.db```.
 
```python
import sqlite3 as dbapi
con = dbapi.connect('census.db')
```


b. Make a database table called ```Density``` that will 
hold the name of the province or territory (TEXT), 
the population (INTEGER), 
and the land area (REAL). 


```python
cur = con.cursor()
cur.execute('''CREATE TABLE Density(Province TEXT,
 Population INTEGER, Area REAL)''')
con.commit()
```


c. Insert the data from the table above. 

```python
table = [
 ('Newfoundland and Labrador', 512930, 370501.69),
 ('Prince Edward Island', 135294, 5684.39),
 ('Nova Scotia', 908007, 52917.43),
 ('New Brunswick', 729498, 71355.67),
 ('Quebec', 7237479, 1357743.08),
 ('Ontario', 11410046, 907655.59),
 ('Manitoba', 1119583, 551937.87),
 ('Saskatchewan', 978933, 586561.35),
 ('Alberta', 2974807, 639987.12),
 ('British Columbia', 3907738, 926492.48),
 ('Yukon Territory', 28674, 474706.97),
 ('Northwest Territories', 37360, 1141108.37),
 ('Nunavut', 26745, 1925460.18),
]
for row in table:
 cur.execute('INSERT INTO Density VALUES (?, ?, ?)', row)
con.commit()
```


d. Retrieve the contents of the table.

```python
cur.execute('SELECT * FROM Density')
for row in cur.fetchall():
 print(row)
```

The result is the following, which should match the table.

```python
('Newfoundland and Labrador', 512930, 370501.69)
('Prince Edward Island', 135294, 5684.39)
('Nova Scotia', 908007, 52917.43)
('New Brunswick', 729498, 71355.67)
('Quebec', 7237479, 1357743.08)
('Ontario', 11410046, 907655.59)
('Manitoba', 1119583, 551937.87)
('Saskatchewan', 978933, 586561.35)
('Alberta', 2974807, 639987.12)
('British Columbia', 3907738, 926492.48)
('Yukon Territory', 28674, 474706.97)
('Northwest Territories', 37360, 1141108.37)
('Nunavut', 26745, 1925460.18)

```



e. Retrieve the populations. 

```python
cur.execute('SELECT Population FROM Density')
for row in cur.fetchall():
 print(row)
```
The result is a list of population figures.

```python
(512930,)
(135294,)
(908007,)
(729498,)
(7237479,)
(11410046,)
(1119583,)
(978933,)
(2974807,)
(3907738,)
(28674,)
(37360,)
(26745,)
```

f. Retrieve the provinces that have populations of less than one million. 

```python
cur.execute('''SELECT Province FROM Density
 WHERE Population < 1000000''')
for row in cur.fetchall():
 print(row)
```
This is the list:

```python
('Newfoundland and Labrador',)
('Prince Edward Island',)
('Nova Scotia',)
('New Brunswick',)
('Saskatchewan',)
('Yukon Territory',)
('Northwest Territories',)
('Nunavut',)
```

g. Retrieve the provinces that have populations of less than one million
or greater than five million. 

```python
cur.execute('''SELECT Province FROM Density
 WHERE Population < 1000000
 OR Population > 5000000''')
for row in cur.fetchall():
 print(row)
```
This returns the provinces in the above list
with a few additional names.

```python
('Newfoundland and Labrador',)
('Prince Edward Island',)
('Nova Scotia',)
('New Brunswick',)
('Quebec',)
('Ontario',)
('Saskatchewan',)
('Yukon Territory',)
('Northwest Territories',)
('Nunavut',)
```

h. Retrieve the provinces that *do not* have populations of less than one million
or greater than five million. 

```python
cur.execute('''SELECT Province FROM Density
 WHERE NOT(Population < 1000000
 OR Population > 5000000)''')
for row in cur.fetchall():
 print(row)
```
The remaining provinces are found here.

```python
('Manitoba',)
('Alberta',)
('British Columbia',)
```

i. Retrieve the populations of provinces that have a land area
greater than 200,000 square kilometers. 

```python
cur.execute('''SELECT Population FROM Density
 WHERE Area > 200000''')
for row in cur.fetchall():
 print(row)
```
Verify that these population figures match the criteria. 

```python
(512930,)
(7237479,)
(11410046,)
(1119583,)
(978933,)
(2974807,)
(3907738,)
(28674,)
(37360,)
(26745,)
```
In practice, you cannot make this verification for large datasets
but you could use this process to test it on a small sample. 

j. Retrieve the provinces along with their population densities
(population divided by land area). 

```python
cur.execute('SELECT Province, Population / Area FROM Density')
for row in cur.fetchall():
 print(row)
```
Simply insert the formula in the place of the variable
with the desired calculation. 

```python
('Newfoundland and Labrador', 1.384420135843375)
('Prince Edward Island', 23.8009707286094)
('Nova Scotia', 17.15893988048928)
('New Brunswick', 10.223406212848959)
('Quebec', 5.330521736115201)
('Ontario', 12.570898175154742)
('Manitoba', 2.0284583842743027)
('Saskatchewan', 1.6689353978062142)
('Alberta', 4.648229483118348)
('British Columbia', 4.217776273802028)
('Yukon Territory', 0.060403579075318826)
('Northwest Territories', 0.03274009812056676)
('Nunavut', 0.013890185981410428)

```

### Example 2: Population of Capital Cities

Now add a new table called ```Capitals``` to the database. 
```Capitals``` has three columns: 
province/territory (TEXT),
capital (TEXT), and population (INTEGER). 

The first three lines depend on the situation. 
We are continuing from above
but if we started another session,
we would have to reopen and reconnect to the database.

```python
import sqlite3 as dbapi
con = dbapi.connect('census.db')
cur = con.cursor()
cur.execute('''CREATE TABLE Capitals(Province TEXT,
 Capital TEXT, Population INTEGER)''')
con.commit()
table = [
 ('Newfoundland and Labrador', "St. John's", 172918),
 ('Prince Edward Island', 'Charlottetown', 58358),
 ('Nova Scotia', 'Halifax', 359183),
 ('New Brunswick', 'Fredericton', 81346),
 ('Quebec', 'Qeubec City', 682757),
 ('Ontario', 'Toronto', 4682897),
 ('Manitoba', 'Winnipeg', 671274),
 ('Saskatchewan', 'Regina', 192800),
 ('Alberta', 'Edmonton', 937845),
 ('British Columbia', 'Victoria', 311902),
 ('Yukon Territory', 'Whitehorse', 21405),
 ('Northwest Territories', 'Yellowknife', 16541),
 ('Nunavut', 'Iqaluit', 5236),
]
for row in table:
 cur.execute('INSERT INTO Capitals VALUES (?, ?, ?)', row)
con.commit()

```

a. Retrieve the contents of the table. 

```python
cur.execute('SELECT * FROM Capitals')
for row in cur.fetchall():
 print(row)
```
Again, the star wildcard gets all the columns. 

```python
('Newfoundland and Labrador', "St. John's", 172918)
('Prince Edward Island', 'Charlottetown', 58358)
('Nova Scotia', 'Halifax', 359183)
('New Brunswick', 'Fredericton', 81346)
('Quebec', 'Qeubec City', 682757)
('Ontario', 'Toronto', 4682897)
('Manitoba', 'Winnipeg', 671274)
('Saskatchewan', 'Regina', 192800)
('Alberta', 'Edmonton', 937845)
('British Columbia', 'Victoria', 311902)
('Yukon Territory', 'Whitehorse', 21405)
('Northwest Territories', 'Yellowknife', 16541)
('Nunavut', 'Iqaluit', 5236)
```

b. Retrieve the populations of the provinces and capitals 
(in a list of tuples of the form 
```[province_population, capital_population]```). 

```python
cur.execute('''SELECT Density.Population, Capitals.Population
 FROM Capitals INNER JOIN Density
 WHERE Capitals.Province = Density.Province''')
for row in cur.fetchall():
 print(row)
```
This pulls pairs of population figures
from provinces and capital cities.

```python
(512930, 172918)
(135294, 58358)
(908007, 359183)
(729498, 81346)
(7237479, 682757)
(11410046, 4682897)
(1119583, 671274)
(978933, 192800)
(2974807, 937845)
(3907738, 311902)
(28674, 21405)
(37360, 16541)
(26745, 5236)
```

c. Retrieve the land area of the provinces whose capitals 
have populations greater than 100,000. 

```python
cur.execute('''SELECT Density.Area
 FROM Capitals INNER JOIN Density
 WHERE Capitals.Province = Density.Province
 AND Capitals.Population > 100000''')
for row in cur.fetchall():
 print(row)
```
This returns 

```python
(370501.69,)
(52917.43,)
(1357743.08,)
(907655.59,)
(551937.87,)
(586561.35,)
(639987.12,)
(926492.48,)
```


d. Retrieve the provinces with land densities
less than two people per square kilometer
and capital city populations more than 500,000. 


```python
cur.execute('''SELECT Density.Province
 FROM Capitals INNER JOIN Density
 WHERE Capitals.Province = Density.Province
 AND Density.Population / Density.Area < 2
 AND Capitals.Population > 500000''')
for row in cur.fetchall():
 print(row)
```


```python

```
Notice that This query doesn't return any results.

e. Retrieve the total land area of Canada. 

```python
cur.execute('SELECT SUM(Area) FROM Density')
print(cur.fetchone())
```

```python
(9012112.19,)
```

We can use ```fetchone()``` because there is only one item to fetch. 

f. Retrieve the average population of the capital cities. 

```python
cur.execute('SELECT AVG(Population) FROM Capitals')
print(cur.fetchone())
```

```python
(630343.2307692308,)
```

Again, sometimes the answer is a single number. 

g. Retrieve the lowest population of the capital cities. 

```python
cur.execute('SELECT MIN(Population) FROM Capitals')
print(cur.fetchone())
```
Iqualuit, way up North in Nunavut
is the capital city with the smallest population. 

```python
(5236,)
```

h. Retrieve the highest population of the provinces or territories. 

```python
cur.execute('SELECT MAX(Population) FROM Density')
print(cur.fetchone())
```

Ontario is the province with the largest population in Canada. 

```python
(11410046,)
```

i. Retrieve the provinces that have land densities within 0.5 persons per square kilometer of one another. 
Have each pair of provinces reported only once. 

```python
cur.execute('''SELECT A.Province, B.Province
 FROM Density A INNER JOIN Density B
 WHERE A.Province < B.Province
 AND ABS(A.Population / A.Area - B.Population / B.Area) <
0.5''')
for row in cur.fetchall():
 print(row)
```

These are the pairs of provinces with densities of similar magnitudes. 

```python
('Newfoundland and Labrador', 'Saskatchewan')
('Manitoba', 'Saskatchewan')
('Alberta', 'British Columbia')
('Northwest Territories', 'Yukon Territory')
('Northwest Territories', 'Nunavut')
('Nunavut', 'Yukon Territory')
```

There are many more examples of calculations you could perform. 
This is just a taste. 
In practice, the true value of the ability to work with databases, 
at least for a Business Analyst, 
is in the ability to make datasets to study with statistical models. 


