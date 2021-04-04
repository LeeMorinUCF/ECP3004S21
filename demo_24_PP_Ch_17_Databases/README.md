
# Chapter 17: Databases


## Advanced Features

### Aggregation

We have already encountered an instance of aggregation:
the ```SUM``` is th emost basic form of aggregation. 


```python
>>> cur.execute('SELECT SUM (Population) FROM PopByRegion')
<sqlite3.Cursor object at 0x102e3e490>
>>> cur.fetchone()
(8965762,)

```

There exist several other commands, as in the following table.

| Aggregate Function | Description
| ------------------ | -----------------------------
| AVG                | Average of the values
| MIN                | Minimum value
| MAX                | Maximum value
| COUNT              | Number of non-NULL values
| SUM                | Sum of the values




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


## Examples



1.
 a.
 
```python
import sqlite3 as dbapi
con = dbapi.connect('census.db')
```


b.


```python
cur = con.cursor()
cur.execute('''CREATE TABLE Density(Province TEXT,
 Population INTEGER, Area REAL)''')
con.commit()
```


 c.
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


 d.
```python
cur.execute('SELECT * FROM Density')
for row in cur.fetchall():
 print(row)
```


 e.
```python
cur.execute('SELECT Population FROM Density')
for row in cur.fetchall():
 print(row)
```


f.
```python
cur.execute('''SELECT Province FROM Density
 WHERE Population < 1000000''')
for row in cur.fetchall():
 print(row)
```
g.
```python
cur.execute('''SELECT Province FROM Density
 WHERE Population < 1000000
 OR Population > 5000000''')
for row in cur.fetchall():
 print(row)
```

h.
```python
cur.execute('''SELECT Province FROM Density
 WHERE NOT(Population < 1000000
 OR Population > 5000000)''')
for row in cur.fetchall():
 print(row)
```
i.
```python
cur.execute('''SELECT Population FROM Density
 WHERE Area > 200000''')
for row in cur.fetchall():
 print(row)
```


j.
```python
cur.execute('SELECT Province, Population / Area FROM Density')
for row in cur.fetchall():
 print(row)
```


2.
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


a.
```python
cur.execute('SELECT * FROM Capitals')
for row in cur.fetchall():
 print(row)
```

b.
```python
cur.execute('''SELECT Density.Population, Capitals.Population
 FROM Capitals INNER JOIN Density
 WHERE Capitals.Province = Density.Province''')
for row in cur.fetchall():
 print(row)
```

c.
```python
cur.execute('''SELECT Density.Area
 FROM Capitals INNER JOIN Density
 WHERE Capitals.Province = Density.Province
 AND Capitals.Population > 100000''')
for row in cur.fetchall():
 print(row)
```


 d.
Note: This query doesn't return any results.
```python
cur.execute('''SELECT Density.Province
 FROM Capitals INNER JOIN Density
 WHERE Capitals.Province = Density.Province
 AND Density.Population / Density.Area < 2
 AND Capitals.Population > 500000''')
for row in cur.fetchall():
 print(row)
```

 e.
```python
cur.execute('SELECT SUM(Area) FROM Density')
print(cur.fetchone())
```

f.
```python
cur.execute('SELECT AVG(Population) FROM Capitals')
print(cur.fetchone())
```

g.
```python
cur.execute('SELECT MIN(Population) FROM Capitals')
print(cur.fetchone())
```

h.
```python
cur.execute('SELECT MAX(Population) FROM Density')
print(cur.fetchone())
```

i.
```python
cur.execute('''SELECT A.Province, B.Province
 FROM Density A INNER JOIN Density B
 WHERE A.Province < B.Province
 AND ABS(A.Population / A.Area - B.Population / B.Area) <
0.5''')
for row in cur.fetchall():
 print(row)
```





