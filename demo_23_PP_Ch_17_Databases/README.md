
# Chapter 17: Databases

In the last lecture, we learned about dictionaries as a precursor to 
this chapter about databases. 
I went through the following examples of databases in which
your very own information is stored. 
For example, the IRS keeps a record of your tax imformation by 
recording amounts in the fields of your tax return, 
your vital statistics, and the primary key is your social security number. 
If you have a driver's license, the DMV keeps a record of your vehicles, 
any tickets you may have received, your vital statistics, 
and these are indexed by your driver's license number as the primary key. 
The same is true for any online purchases you make: 
your order details, your address and your purchase history 
are all stored in a database with some form of customer id number and order number. 

Here we will learn one way that this sort of information can be stored, 
retrieved and organized. 
Businesses rely heavily on databases to keep track of information 
for many accounting and payroll functions.
A primary reason for a business analyst or data scientist to use databases
is to generate a dataset from the information stored in databases. 

The primary tool that we will use is the Python module ```sqlite3```. 
SQL is an acronym for *Structured Query Language*, 
which is either pronounced "S-Q-L" or "sequel". 
It is a language or, more precisely, a set of dialects that are used to 
execute commands called *queries* using *relational databases*. 
There exist many dialects of SQL and in fact, many other database structures
that do not fall under the SQL paradigm. 
However, SQL is ubiquitous in business and is a stepping stone to more advanced
methods of interacting with databases.
The dialect of SQL called ```sqlite3``` is a compact and versatile 
set of infrastructure for executing SQL queries and interacting with databases. 
Most of the important SQL commands can be executed in ```sqlite3```
and, with a few exceptions, most of the syntax is identical 
to that which you would use in another dialect of SQL. 

There are other ways of executing commands to interact with databases:
- *Typing commands into a database GUI:* You might have a graphical program, 
in which you enter the SQL queries, 
much like we do by running Python commands in Spyder.
- *By writing programs in some language:* 
These programs import a library of functions that allow you to interact with
a database. Python is one of many languages in which this can be achieved. 

We will follow the second approach, 
and the first step on this journey is to load the Python module ```sqlite3```. 


```python 
>>> import sqlite3

``` 

Let's get started. 


## Creating and Populating

The example we will use in this section is a set of predicted populations
in regions of the world for the year 2300. 
The numbers are shown in Table 30 
called *Estimated World Population in 2300*
on page 345
of *Practical Programming*, 
and the data are taken from http://www.worldmapper.org.

First, we tell Python that we want to use ```sqlite3```. 

```python 
>>> import sqlite3
```

Next, we must make a connection to our database. 
Databases can be stored in a file with extension ```db```. 
Often the database sits on a sever that can hold large amounts of data. 
In that case, you will need access to that computer and will have to pass login credentials (username and password) to open the connection. 
For our purposes, we will assume that the ```db``` file is located on your computer. 
To make the connection, we call the ```sqlite3``` method ```connect```
and pass the string filename as the argument. 

```python 
>>> con = sqlite3.connect('population.db')
``` 
If there is no database called ```'population.db'```, 
```sqlite3``` will open an empty database. 

Once we have made a connection, we need to get a cursor. 
Like the cursor in an editor (the blinking vertical line), 
this keeps track of where we are in the database. 
If several users are accessing the database at the same time, 
the database can also keep track of who is doing what. 

```python 
>>> cur = con.cursor()
``` 

Now we can start working with the database. 
So far, it is empty. 
The first step is to execute a command that ```CREATE```s a ```TABLE```
in which to store data. 
We pass commands to the database to run at the cursor 
using the ```execute``` method, 
by passing the SQL command in the form of a string. 

The basic command for creating a table is 

```
CREATE TABLE Name_of_Tale(Column_name type, ...)
```

The types for each column of data are shown in the following table.


| Type    | Python Equivalent | Usage
| ------- | ----------------- | -----------------------------
| NULL    | NoneType          | Means "no information"
| INTEGER | int               | Integers
| REAL    | float             | 8-byte floating-point numbers
| TEXT    | str               | Strings of Characters
| BLOB    | bytes             | Binary data

Now we will use this to create a two-column table
named ```PopByRegion``` to store 
regions named as strings in the ```Region``` column
and projected populations as integers in the ```Population``` column. 


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

The commit method saves the changes. 

```python 
>>> con.commit()

``` 

### Closing the Connection

Close the connection when finished. 


```python 
>>> con.close()

``` 





## Retrieving Data


First, reopen the database (we just closed it).
Create a database, if it does not already exist.

```python
con = sqlite3.connect('population.db')

```

As above, create a cursor object from which to execute SQL commands.

```python
cur = con.cursor()
```

This is the procedure you would follow to interact with an existing database.



Basic form of a query:



```python 
cur.execute('SELECT Column_1, Column_2 FROM Name_of_Table')
```



```python 
>>> cur.execute('SELECT Region, Population FROM PopByRegion')
<sqlite3.Cursor at 0x1e57ba16e30>
``` 

But it does not print anything interesting. 
It only stores the result of the query in memory. 
We can access the contents of the ```SELECT```ed table
by reading parts of it from the cursor. 


Fetch one line at a time:
```python 
>>> cur.fetchone()
('Central Africa', 330993)
``` 

Fetch all the rest:


```python 
>>> cur.fetchall()
[('Southeastern Africa', 743112), ('Northern Africa', 1037463), ('Southern
Asia', 2051941), ('Asia Pacific', 785468), ('Middle East', 687630), 
('Eastern Asia', 1362955), ('South America', 593121), ('Eastern Europe',
223427), ('North America', 661157), ('Western Europe', 387933), ('Japan',
100562)]
``` 
Note that the first line was already fetched above.

Further fetches have nothing to fetch.

```python 
>>> cur.fetchone()
>>> cur.fetchall()
[]
``` 


Calculate functions of variables
```python 
>>> cur.execute('SELECT SUM(Population) FROM PopByRegion')
>>> cur.fetchall()
[(8965762,)]
```

Star (*) denotes a wildcard variable.
```python 
>>> cur.execute('SELECT * FROM PopByRegion')
>>> cur.fetchall()
[('Central Africa', 330993),
 ('Southeastern Africa', 743112),
 ('Northern Africa', 1037463),
 ('Southern Asia', 2051941),
 ('Asia Pacific', 785468),
 ('Middle East', 687630),
 ('Eastern Asia', 1362955),
 ('South America', 593121),
 ('Eastern Europe', 223427),
 ('North America', 661157),
 ('Western Europe', 387933),
 ('Japan', 100562)]
```

This is a good go-to command to verify that your tables was created as you intended.
Be careful! It can backfire for large examples, such as a query on an entire database.
You migh, however, use this on a small table that you have created with your query. 



Use an ```ORDER BY``` clause to sort the output.

```python 
>>> cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Region')
>>> cur.fetchall()
[('Asia Pacific', 785468), ('Central Africa', 330993), ('Eastern Asia',
1362955), ('Eastern Europe', 223427), ('Japan', 100562), ('Middle East',
687630), ('North America', 661157), ('Northern Africa', 1037463), ('South
America', 593121), ('Southeastern Africa', 743112), ('Southern Asia', 
2051941), ('Western Europe', 387933)]
``` 


You can also sort in ````DESC````ending order.


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

You can select a subset of rows with the ```WHERE``` clause.
This precedes a Boolean expression that uses one or more of 
the following relational operators:
```=```, ```!=```, ```>```, ```<```, ```>=```, and ```<=```. 
All but the first have the same meaning as they do in Python. 
There is no assignment operator ```=``` in SQL 
(we did that with ```CREATE TABLE```, in some sense), 
so the equals symbol is unambiguously a test of equality,  
meaning the same as ```==``` in a Boolean expression in Python. 
You might find that, in SQL, the meaning is easy to derive from the context, 
since the commands are stated the way you would instruct someone to perform tasks, 
much like you would in the English language. 

```python 
>>> cur.execute('SELECT Region FROM PopByRegion WHERE Population > 1000000')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Northern Africa',), ('Southern Asia',), ('Eastern Asia',)]

``` 
You can use logical operators such as ```AND```, ```OR```, and ```NOT``` 
in the WHERE clause.
These are used the same way one would use them in Python. 


```python 
>>> cur.execute('''SELECT Region FROM PopByRegion
                   WHERE Population > 1000000 AND Region < "L"''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Eastern Asia',)]

``` 

Notice how the ```<``` operator works on strings.


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


Create another table to experiment with joins.


```python 
>>> cur.execute('''CREATE TABLE PopByCountry(Region TEXT, Country TEXT, 
                   Population INTEGER)''')

``` 

We could ```INSERT``` the ```VALUES``` one at a time, as with ```PopByRegion``` above:

```python 
>>> cur.execute('''INSERT INTO PopByCountry VALUES("Eastern Asia", "China", 
                   1285238)''') 

``` 

It is easier if we pull the values from a list of tuples.

```python 
>>> countries = [("Eastern Asia", "DPR Korea", 24056), ("Eastern Asia", 
"Hong Kong (China)", 8764), ("Eastern Asia", "Mongolia", 3407), ("Eastern 
Asia", "Republic of Korea", 41491), ("Eastern Asia", "Taiwan", 1433), 
("North America", "Bahamas", 368), ("North America", "Canada", 40876), 
("North America", "Greenland", 43), ("North America", "Mexico", 126875), 
("North America", "United States", 493038)]
```


Now loop through those entries and INSERT the VALUES.

```python 
>>> for c in countries:
...   cur.execute('INSERT INTO PopByCountry VALUES (?, ?, ?)', (c[0], c[1], c[2]))
... 
```
As above, the commit method saves the changes.

```python 
>>> con.commit()

``` 

Often, you would not do this sort of operation in the console. 
For large datasets, you will often prefer to collect the commands into a script. 
The following script defines a database with a pair of tables. 

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


In either case, once you have created the database (if it is a small example)
you can see what you have created by running a ```SELECT``` ... ```fetchall()```
set of commands. 


```python
>>> cur.execute('''SELECT * FROM   PopByCountry''')
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



Another very popular option is a ```LEFT JOIN```, 
which returns a row for *every* element of the first table
(the *left* table) ,
regardless of whether there is a corresponding row in the
other table (the *right* table). 

```python 
>>> cur.execute('''
SELECT PopByRegion.Region, PopByCountry.Country
FROM   PopByRegion LEFT JOIN PopByCountry
ON  (PopByRegion.Region = PopByCountry.Region)
AND    (PopByRegion.Population > 1000000)
''')
<sqlite3.Cursor object at 0x102e3e490>

>>> cur.fetchall()
[('Central Africa', None),
 ('Southeastern Africa', None),
 ('Northern Africa', None),
 ('Southern Asia', None),
 ('Asia Pacific', None),
 ('Middle East', None),
 ('Eastern Asia', 'China'),
 ('Eastern Asia', 'DPR Korea'),
 ('Eastern Asia', 'Hong Kong (China)'),
 ('Eastern Asia', 'Mongolia'),
 ('Eastern Asia', 'Republic of Korea'),
 ('Eastern Asia', 'Taiwan'),
 ('South America', None),
 ('Eastern Europe', None),
 ('North America', None),
 ('Western Europe', None),
 ('Japan', None)]
```
Notice that the missing countries within other regions 
are represented by ```None```, 
since there is no value in the other table.


### Removing Duplicates


Consider this example:

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


Now repeat with the ```DISTINCT``` keyword.

```python 
>>> cur.execute('''
SELECT DISTINCT PopByRegion.Region
FROM PopByRegion INNER JOIN PopByCountry
WHERE (PopByRegion.Region = PopByCountry.Region)
AND ((PopByCountry.Population * 1.0) / PopByRegion.Population > 0.10)''')
>>> cur.fetchall()
[('Eastern Asia',), ('North America',)]

``` 

Only unique values remain.


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

