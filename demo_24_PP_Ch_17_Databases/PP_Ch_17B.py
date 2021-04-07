#!/usr/bin/python
"""
##################################################
# 
# ECP 3004: Python for Business Analytics
# 
# Using Databases with SQLite3
# 
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business Administration
# University of Central Florida
# 
# April 3, 2021
# 
# Chapter 17: Databases
# Part B: Advanced Features
# 
# This program provides examples of SQL commands
# including creating tables, selecting data, 
# joining data and aggregating data.
# 
##################################################
"""


##################################################
# Import Modules.
##################################################


import os # To set working directory

import sqlite3


##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
git_path = 'C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\'
os.chdir(git_path + 'demo_24_PP_Ch_17_Databases')
# Check that the change was successful.
os.getcwd()


##################################################
# Connect to the database from the last lecture
##################################################


# Create a database, if it does not already exist.
con = sqlite3.connect('population.db')

# Create a cursor object from which to execute
# SQL commands.
cur = con.cursor()



# Now, where were we? 

##################################################
# Aggregation
##################################################

# Calculate the sum of the population, tabulated by Region.
cur.execute('''SELECT Region, SUM (Population) FROM PopByCountry
                   GROUP BY Region''')

cur.fetchall()


# Now restrict the calculation to North America.
cur.execute('''SELECT SUM (Population) FROM PopByCountry
                   WHERE Region = "North America"''')

cur.fetchall()

# Similarly for Eastern Asia.
cur.execute('''SELECT SUM (Population) FROM PopByCountry
                   WHERE Region = "Eastern Asia"''')

cur.fetchall()



##################################################
### Self-Joins
##################################################

# Now, let's consider the problem of comparing some values from a table
# to other values drawn from the same table. 
# This can be achieved using a *self-join*. 
# You treat two instances of tables drawn from the same root table
# as separate tables that can be joined together, 
# as you could with any other pair of tables. 

# Suppose we want to find pairs of countries whose populations 
# are close to each other--say, within 1,000 of each other. 

# Our first attempt might look like this: 


cur.execute('''SELECT Country FROM PopByCountry
                   WHERE (ABS(Population - Population) < 1000)''')
# <sqlite3.Cursor object at 0x102e3e490>
cur.fetchall()
# [('China',), ('DPR Korea',), ('Hong Kong (China)',), ('Mongolia',),
# ('Republic of Korea',), ('Taiwan',), ('Bahamas',), ('Canada',),
# ('Greenland',), ('Mexico',), ('United States',)]


# This is not what was wanted, for two reasons: 
# - First, the phrase ```SELECT Country``` is going to return only one country per record, but we want pairs of countries.
# - Second, Second, the expression 
# ```(ABS(Population - Population) < 1000)``` is always going to return zero
# because it compares every population agains itself, line-by-line. 
# Since they will all be zero, the query will return all the country names in the table. 


# What we want to do is compare the population in each row with the populations 
# of countries in other rows. 
# To do this, we need to join ```PopByCountry``` with itself using an ```INNER JOIN```. 

cur.execute('''
SELECT A.Country, B.Country
FROM   PopByCountry A INNER JOIN PopByCountry B
WHERE  (ABS(A.Population - B.Population) <= 1000)
AND    (A.Country != B.Country)''')
# <sqlite3.Cursor object at 0x102e3e490>
cur.fetchall()
# [('Republic of Korea', 'Canada'), ('Bahamas', 'Greenland'), ('Canada',
# 'Republic of Korea'), ('Greenland', 'Bahamas')]


# Notice that we used the absolute value function ```ABS()```. 
# Without this, the ```WHERE``` clause would also return other pairs
# of countries where the second country is much larger than the first, 
# i.e. where the difference ```A.Population - B.Population``` would be negative. 



##################################################
# Nested Queries
##################################################


# Instead of pulling from a table, you can replace 
# the name of a table with a query that produces the required table. 

# Example: Select the list of regions that do not have 
# a country with a population of 8,764,000.



# Information:
cur.execute('''SELECT *
                   FROM PopByCountry''')

cur.fetchall()


# When you include the ```WHERE``` clause to exclude Hong Kong, 
# it also excludes Hong Kong from the list of countries in that region. 


cur.execute('''SELECT *
                   FROM PopByCountry
                   WHERE (PopByCountry.Population != 8764)''')

cur.fetchall()


# First attempt:
cur.execute('''SELECT DISTINCT Region
                   FROM PopByCountry
                   WHERE (PopByCountry.Population != 8764)''')

cur.fetchall()
# Notice the mistake: Hong Kong does have a population of 8,764,000
# but Eastern Asia is still included. 


# As an intermediate step, create a query that creates a table that 
# lists the Regions that do have a country with a population of 8,764,000.

# These are the other rows of the table. 
cur.execute('''
SELECT DISTINCT Region
FROM PopByCountry
WHERE (PopByCountry.Population = 8764)
''')
cur.fetchall()


# Now nest this within the table for the nested query. 
cur.execute('''
SELECT DISTINCT Region
FROM PopByCountry
WHERE Region NOT IN
    (SELECT DISTINCT Region
     FROM PopByCountry
     WHERE (PopByCountry.Population = 8764))
''')

cur.fetchall()

# The bracketed expression is a query that produces a table, 
# which is then passed to the nesting query, 
# much like the way you pass a calculated expression as an argument 
# to another function.

# Close the connection when finished. 
# con.close()

# If you want to save that progress, 
# make sure to commit before closing the connection.

# con.commit()
# con.close()


##################################################
# Examples from Exercises at the end of Chapter 17
##################################################

#--------------------------------------------------
### Example 1: Population, Area 
###     and Population Density of Provinces
#--------------------------------------------------

# In this example, we will create a table 
# to store the population and land area of the provinces and
# territories of Canada, according to the 2001 census with Statistics Canada. 


# a. Create a new database called census.db.

# You would import some kind of API 
# to interact with the database
# We will continue using sqlite3
import sqlite3 as dbapi
con = dbapi.connect('census.db')



# b. Make a database table called Density that will 
# hold the name of the province or territory (TEXT), 
# the population (INTEGER), 
# and the land area (REAL). 


cur = con.cursor()
cur.execute('''CREATE TABLE Density(Province TEXT,
 Population INTEGER, Area REAL)''')
con.commit()


# c. Insert the data from the table above. 

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


# d. Retrieve the contents of the table.

cur.execute('SELECT * FROM Density')
for row in cur.fetchall():
 print(row)


# e. Retrieve the populations. 

cur.execute('SELECT Population FROM Density')
for row in cur.fetchall():
 print(row)



# f. Retrieve the provinces that have populations of less than one million. 


cur.execute('''SELECT Province FROM Density
 WHERE Population < 1000000''')
for row in cur.fetchall():
 print(row)


# g. Retrieve the provinces that have populations of less than one million
# or greater than five million. 


cur.execute('''SELECT Province FROM Density
 WHERE Population < 1000000
 OR Population > 5000000''')
for row in cur.fetchall():
 print(row)


# h. Retrieve the provinces that *do not* have populations of less than one million
# or greater than five million. 


cur.execute('''SELECT Province FROM Density
 WHERE NOT(Population < 1000000
 OR Population > 5000000)''')
for row in cur.fetchall():
 print(row)


# i. Retrieve the populations of provinces that have a land area
# greater than 200,000 square kilometers. 


cur.execute('''SELECT Population FROM Density
 WHERE Area > 200000''')
for row in cur.fetchall():
 print(row)



# j. Retrieve the provinces along with their population densities
# (population divided by land area). 


cur.execute('SELECT Province, Population / Area FROM Density')
for row in cur.fetchall():
 print(row)



#--------------------------------------------------
### Example 2: Population of Capital Cities
#--------------------------------------------------

# Now add a new table called Capitals to the database. 
# Capitals has three columns: 
# province/territory (TEXT),
# capital (TEXT), and population (INTEGER). 

# We are continuing from above
# but if we started another session, 
# we would have to reopen and reconnect to the database.
# import sqlite3 as dbapi
# con = dbapi.connect('census.db')
# cur = con.cursor()


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



# a. Retrieve the contents of the table. 


cur.execute('SELECT * FROM Capitals')
for row in cur.fetchall():
 print(row)


# b. Retrieve the populations of the provinces and capitals 
# (in a list of tuples of the form 
# [province_population, capital_population]). 


cur.execute('''SELECT Density.Population, Capitals.Population
 FROM Capitals INNER JOIN Density
 WHERE Capitals.Province = Density.Province''')
for row in cur.fetchall():
 print(row)


# c. Retrieve the land area of the provinces whose capitals 
# have populations greater than 100,000. 


cur.execute('''SELECT Density.Area
 FROM Capitals INNER JOIN Density
 WHERE Capitals.Province = Density.Province
 AND Capitals.Population > 100000''')
for row in cur.fetchall():
 print(row)



# d. Retrieve the provinces with land densities
# less than two people per square kilometer
# and capital city populations more than 500,000. 



cur.execute('''SELECT Density.Province
 FROM Capitals INNER JOIN Density
 WHERE Capitals.Province = Density.Province
 AND Density.Population / Density.Area < 2
 AND Capitals.Population > 500000''')
for row in cur.fetchall():
 print(row)

# Note: This query doesn't return any results.

# e. Retrieve the total land area of Canada. 


cur.execute('SELECT SUM(Area) FROM Density')
print(cur.fetchone())


# f. Retrieve the average population of the capital cities. 


cur.execute('SELECT AVG(Population) FROM Capitals')
print(cur.fetchone())


# g. Retrieve the lowest population of the capital cities. 


cur.execute('SELECT MIN(Population) FROM Capitals')
print(cur.fetchone())


# h. Retrieve the highest population of the provinces or territories. 

cur.execute('SELECT MAX(Population) FROM Density')
print(cur.fetchone())


# i. Retrieve the provinces that have land densities within 0.5 persons per square kilometer of one another. 
# Have each pair of provinces reported only once. 


cur.execute('''SELECT A.Province, B.Province
 FROM Density A INNER JOIN Density B
 WHERE A.Province < B.Province
 AND ABS(A.Population / A.Area - B.Population / B.Area) <
0.5''')
for row in cur.fetchall():
 print(row)



# Check for yourself:
cur.execute('''SELECT A.Province, A.Population / A.Area AS PopDensity
 FROM Density A 
 ORDER BY PopDensity''')
for row in cur.fetchall():
 print(row)



##################################################
# Commit changes and close the connection
##################################################


# The commit method saves the changes. 
con.commit()


# Close the connection when finished. 
con.close()

# Then we can continue with this file when you have time
# to work on it later.



##################################################
# Extra code snippets
##################################################


# This can get the schema of the table,
# cur.execute("PRAGMA table_info('Density')").fetchall()
# cur.execute("PRAGMA table_info('Capitals')").fetchall()
# which states the names of the variables and the data types.

# In case things go wrong, you can always drop the table
# and start over:
# cur.execute('DROP TABLE Density')
# cur.execute('DROP TABLE Population')


##################################################
# End
##################################################


