
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

```python
'CREATE TABLE Name_of_Tale(Column_name type, ...)'
```

The types for each column of data are shown in the following table.


| Type    | Python Equivalent | Usage
| ------- | ----------------- | -----------------------------
| NULL    | NoneType          | Means "no information"
| INTEGER | int               | Integers
| REAL    | float             | 8-byte floating-point numbers
| TEXT    | str               | Strings of Characters
| BLOB    | bytes             | Binary data

Most of these data types should be familiar to you. 
The new term is ```BLOB```, which stands for 
*Binary Large Object*, which could represent any object that can be stored in binary form. 
Your playlist might be stored in this format, 
as the ```BLOB``` data type is rich enough to store ```mp3``` files, for example. 

Now we will use these data types to create a two-column table
named ```PopByRegion``` to store 
regions named as strings in the ```Region``` column
and projected populations as integers in the ```Population``` column. 


```python 
>>> cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')
<sqlite3.Cursor object at 0x102e3e490>

``` 
Note that this command only returns the cursor and its location. 
So far, the table is empty but we can ```INSERT``` some ```VALUES```
to change that. 

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
Much like the way a dictionary works, 
it looks as though we pass it a tuple
in the order of the fields in the database. 
Again, this command is passed to the database with the ```execute``` method. 

For a large number of entries, you will not want to
type these commands manually. 
Another way that you could execute the ```INSERT VALUES``` command
is to use question marks as placeholders and pass tuples 
of field values to fill in the ```?``` places in the string ```'(?, ?)'```. 

```python 
>>> cur.execute('INSERT INTO PopByRegion VALUES (?, ?)', ("Japan", 100562))

``` 



### Saving Changes

However you enter your data, you will need to save the state of your database,
much like you would for any other program. 
The commit method saves the changes. 

```python 
>>> con.commit()

``` 
Use the commit command like you would the ````Ctrl-S``` command. 
(You are doing this, aren't you? 
You know what they say: "Save early. Save often.")

If the program crashes, for any reason, the work you have done 
is only stored up to the last commit. 



### Closing the Connection

Finally, when all the work is done, we need to
```close``` the connection.. 


```python 
>>> con.close()

``` 
This is just like closing a file. 
make sure, though, that you have "saved" all of your changes
with a call to ```commit```, 
otherwise those changes will not be saved. 
The main purpose of closing the connection is to free up resources, 
such as the memory required to store a database. 


## Retrieving Data

Now that we have a database that contains some data, 
how do we access the data?
First, reopen the database (since we just closed it).
Again, this will also create a database, if it does not already exist.

```python
con = sqlite3.connect('population.db')

```

As above, create a cursor object from which to execute SQL commands.

```python
cur = con.cursor()
```

This is the procedure you would follow to interact with an existing database.


The primary command issued in SQL is a query. 
The most common is the ```SELECT``` statement. 
The basic form of a query is as follows. 

```python 
cur.execute('SELECT Column_1, Column_2 FROM Name_of_Table')
```

You pass the names of the columns you want to ```SELECT```
and say which table you want them to be ```SELECT```ed from. 
Notice that the command reads like the instructions you would
give a person in English. 

```python 
>>> cur.execute('SELECT Region, Population FROM PopByRegion')
<sqlite3.Cursor at 0x1e57ba16e30>
``` 

But it does not print anything interesting. 
It only stores the result of the query in memory. 
We can access the contents of the ```SELECT```ed table
by reading parts of it from the cursor. 

With the ```fetchone``` method, we can
fetch one line at a time. 

```python 
>>> cur.fetchone()
('Central Africa', 330993)
``` 

If thst is not enough for you, you can use the ```fetchone``` method, 
to fetch all the rest.


```python 
>>> cur.fetchall()
[('Southeastern Africa', 743112), ('Northern Africa', 1037463), ('Southern
Asia', 2051941), ('Asia Pacific', 785468), ('Middle East', 687630), 
('Eastern Asia', 1362955), ('South America', 593121), ('Eastern Europe',
223427), ('North America', 661157), ('Western Europe', 387933), ('Japan',
100562)]
``` 
Notice that the first line was already fetched above. 
The subsequent fetches start from the location of the cursor. 
Since we have fetched all that the query has returned, 
further fetches have nothing more to fetch.

```python 
>>> cur.fetchone()
>>> cur.fetchall()
[]
``` 
In this case, ```cur.fetchone()``` returns ```None``` and
```cur.fetchall()``` returns an empty list. 


Databases are not very interesting if you can only
pull out what you put in. 
You can also calculate functions of the variables in your database. 

```python 
>>> cur.execute('SELECT SUM(Population) FROM PopByRegion')
>>> cur.fetchall()
[(8965762,)]
```

One of the most common shortcuts is to use the 
star, or asterisk, (```*```), which denotes a wildcard for the column names.
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
You might, however, use this on a small table that you have created with your query. 

For now, we will focus on extracting the data. 
If your data has to be in order, 
use an ```ORDER BY``` clause to sort the output.

```python 
>>> cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Region')
>>> cur.fetchall()
[('Asia Pacific', 785468), ('Central Africa', 330993), ('Eastern Asia',
1362955), ('Eastern Europe', 223427), ('Japan', 100562), ('Middle East',
687630), ('North America', 661157), ('Northern Africa', 1037463), ('South
America', 593121), ('Southeastern Africa', 743112), ('Southern Asia', 
2051941), ('Western Europe', 387933)]
``` 


You can also sort in ````DESC````ending order...


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
...or in ```ASC```ending order, if that is what you need. 

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
Since we have all studied sorting algorithms, 
we might be tempted to sort the returned list in Python. 
Instead, sorting it within your SQL query takes advantage of the fact that
entries in the databased are stored in a particular order that makes it easier to sort. 
Also, in practice, the database is usually housed on much more powerful computing system, 
which is especially useful if you have large tables 
that need to be sorted within intermediate calculations. 
It is better to transfer the smallest file in its final form. 


### Query Conditions

Note that we referred to the use of the ```ORDER``` qualifier as a *clause*. 
This is consistent with the notion that the statements are much like 
instructions in the English language:
extra qualifications are appended as clauses
(although sometimes the query is more like a run-on sentence).

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
in the ```WHERE``` clause.
These are used the same way one would use them in Python. 


```python 
>>> cur.execute('''SELECT Region FROM PopByRegion
                   WHERE Population > 1000000 AND Region < "L"''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchall()
[('Eastern Asia',)]

``` 

Notice how the ```<``` operator works on strings.
Also note that we had to use two kinds of quotes
in the above command:
the query was passed in double quotes, 
while the string ```'L'``` in the Boolean expression
was passed in single quotes within the larger string. 


## Updating and Deleting

Databases change over time. 
We laerned how to ```INSERT VALUES``` in our database
but that only operates one row at a time. 
If we want to make larger changes, 
we can use the ```UPDATE``` command to take advantage of
the use of Boolean logic passed through a ```WHERE``` caluse. 

```python 
>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchone()
('Japan', 100562)
```
This the value recorded for Japan. 
Now we can change it by updating.

```python 
>>> cur.execute('''UPDATE PopByRegion SET Population = 100600
                   WHERE Region = "Japan"''')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchone()
('Japan', 100600)

``` 
As you can see the value was changed. 
It would also work for all rows for which the columns 
satisfy the Boolean expression in the ```WHERE``` clause. 

Similarly, we can also ```DELETE``` records from the database.

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
As before, we can put them back, one row at a time. 

```python 
>>> cur.execute('INSERT INTO PopByRegion VALUES (?, ?)', ("Japan", 100562))
``` 

We can also delete all entries in the database, 
including the table itself, by ```DROP```ping the ```TABLE```. 

```python 
>>> cur.execute('DROP TABLE PopByRegion')

``` 

Be careful with this one! There is no "Undo" button. 

<img src="Images/little_bobby_tables.png" width="500">


## Using ```NULL``` for Missing Data

Just like the value ```None``` in Python, 
SQL provides a placeholder for missing values. 
The missing keyword is ```NULL```. 
Since we don't know the value of the population on Mars, we can enter

```python 
>>> cur.execute('INSERT INTO PopByRegion VALUES ("Mars", NULL)')

``` 

Sometimes, as the architect of the database, 
you make this an impossibility. 
You have seen the red starred fields in an online application before, 
under name, address, etc. 
Lurking in the background is a ```NOT NULL``` qualifier in the *schema*
of the database. 

```python 
>>> cur.execute('CREATE TABLE Test (Region TEXT NOT NULL, '
...             'Population INTEGER)')

``` 
It is much like a type contract with automated error handling
to prevent any entries that are missing values in certain fields. 

```python 
>>> cur.execute('INSERT INTO Test VALUES (NULL, 456789)')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    cur.execute('INSERT INTO Test VALUES (NULL, 456789)')
sqlite3.IntegrityError: Test.Region may not be NULL

``` 
This is fine because SQL gives you a precise error message
but this may not be ideal because the entry is blocked. 
In some cases, you might want to insert a particular value 
such as ```0```, an empty string```''``` or ```false```, 
which could be used to represent different kinds of missing data. 
Some databases use default codes, such as negative integers or 
an unlikely value, such as ```-999990```. 
Then it is up to the programmer 
to handle the default or missing values downstream. 

The tretment of ```NULL``` variables in SQL differs from 
those in other languages, such as ```None``` in Python. 
Of course, many operations involving ```NULL``` produce ```NULL```
because if the input value is missing or unknown, 
then so is the output value. 
Logical operations are more complicated, however. 
The Boolean expression ```NULL or 1``` produces 1, rather than ```NULL```, 
for the following reasons:
- If the first argument were false or zero, then the full expression would evaluate to 1. 
- If the first argument were true or one, then the full expression would also evaluate to 1. 
The technical term for this is *three-valued logic*. 
In SQL, statements are not only true or false, they can be true, false or unknown. 
Note also that different database formats might handle this sort of logic, 
so the best practice is to test it on your infrastructure. 



## Using Joins to Combine Tables

So far, we have been limiting ourselves to a single table. 
The main value of organizing data into a *relational database* is to 
form relationships between data in other tables. 

Let's create another table to experiment with the ways in which we can ```JOIN``` data.


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


Now loop through those entries and ```INSERT``` the ```VALUES```.

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

Now we have a pair of related tables in our database. 
We can join them by adding ```JOIN``` keywords after the ```FROM``` clause. 
We can join data in several ways. 
We will use ```INNER JOIN```s, ```LEFT JOIN```s and what are called self-joins. 

In an ```INNER JOIN```, the syntax is as follows. 

```python 
>>> cur.execute('''
SELECT Table1.Column1, Table2.ColumnX 
FROM   Table1 INNER JOIN Table2 
WHERE  (Table1.Column1 = Table2.Column1) 
AND    (Table1.ColumnY > 1000000)
''')
<sqlite3.Cursor object at 0x102e3e490>

``` 
What does SQL do here?
It executes the following three steps. 
1. Construct the cross product of the tables
1. Discard rows that do not meet the selection criteria
1. Select columns from the remaining rows

Now, let's repeat our query for the list of regions
with high populations, 
except we will list the countries in each region, 
taking those from the new table, ```PopByCountry```. 

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


To appreciate the difference between the two forms of joins, 
let's reconsider the steps that SQL executes under these two types of joins. 
An ```INNER JOIN``` comprises the following three steps. 
1. Construct the cross product of the tables
1. Discard rows that *do not have matching keys from both tables*
1. Select columns satisfying the ```WHERE``` clause* from the remaining rows

In contrast, a ```LEFT JOIN``` comprises the following three steps. 
1. Construct the cross product of the tables
1. Discard rows that *do not have matching keys in the RIGHT table*
1. Select columns from the remaining rows


### Removing Duplicates

Sometimes you only need to know the set of entries that uniquely satisfy
certain conditions. 
To achieve this, you remove duplicates. 
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

Notice that the string ```'North America'``` appears twice. 
Now repeat the query with the ```DISTINCT``` keyword
after the ```SELECT``` command.

```python 
>>> cur.execute('''
SELECT DISTINCT PopByRegion.Region
FROM PopByRegion INNER JOIN PopByCountry
WHERE (PopByRegion.Region = PopByCountry.Region)
AND ((PopByCountry.Population * 1.0) / PopByRegion.Population > 0.10)''')
>>> cur.fetchall()
[('Eastern Asia',), ('North America',)]

``` 

Now, only the unique values remain.


## Keys and Constraints

Our query in the previous section relied on the fact that our regions and countries
were uniquely identified by their names. 
A column in a table that is used this way is called a *key*. 
Your social security number, driver's license number and variaous customer numbers
are all keys within databases. 
Ideally, the values of the keys should be unique, 
just liek the words in a dictionary. 

To tell the database to enforce this constraint, 
we can use a ```PRIMARY KEY``` clause when we create the table. 


```python 
>>> cur.execute('''CREATE TABLE PopByRegion (
                   Region TEXT NOT NULL, 
                   Population INTEGER NOT NULL, 
                   PRIMARY KEY (Region))''')
``` 
Sometimes your data are organized according to more than one value. 
For example, your customer information on file at an online retailer
will also reference invoice numbers and transaction numbers. 
These can be used as multiple keys in some tables.

Sometimes, however, the uniqueness of your records only holds
in terms of combinations of several columns. 
The ```CONSTRAINT``` keyword is used below
to specify that no two entries in the table created below
will ever have tha same values for region *and* country. 

```python 
>>> cur.execute('''
    CREATE TABLE PopByCountry(
    Region TEXT NOT NULL,
    Country TEXT NOT NULL,
    Population INTEGER NOT NULL,
    CONSTRAINT CountryKey PRIMARY KEY (Region, Country))''')


``` 

In practice, databases are often designed to use integers as keys. 
This way, they can be generated to satisfy the uniqueness constraints
and it avoids any complications from having two entries with, say, the same name. 
