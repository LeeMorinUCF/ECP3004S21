#!/usr/bin/python
"""
##################################################
# 
# QMB 6358: Software Tools for Business Analytics
# 
# Using Databases with SQLite3
# 
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business Administration
# University of Central Florida
# 
# November 18, 2020
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
os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\QMB6358_Fall_2020\\GitRepos\\QMB6358F20\\demo_19_sql_w_python')
# Check that the change was successful.
os.getcwd()


##################################################
# Creating and Populating Tables
##################################################



# Create a database, if it does not already exist.
con = sqlite3.connect('population.db')

# Create a cursor object from which to execute
# SQL commands.
cur = con.cursor()

# Create a table.
cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')

# Insert some values into the table. 
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


# The commit method saves the changes. 
con.commit()

# Close the connection when finished. 
con.close()




##################################################
# Retrieving Data
##################################################


# First, reopen the database (we just closed it).
# Create a database, if it does not already exist.
con = sqlite3.connect('population.db')
# Create a cursor object from which to execute SQL commands.
cur = con.cursor()
# This is what you would do for an existing database. 



# Basic form of a query:
cur.execute('SELECT Region FROM PopByRegion')

# Fetch one line at a time:
cur.fetchone()

# Fetch all the rest:
cur.fetchall()
# Note that the first line was already fetched above.

# Further fetches have nothing to fetch.
cur.fetchone()
cur.fetchall()


# Calculate functions of variables
cur.execute('SELECT SUM(Population) FROM PopByRegion')
cur.fetchall()

# Star (*) denotes a wildcard variable.
cur.execute('SELECT * FROM PopByRegion')
cur.fetchall()


# Use an ORDER BY clause to sort the output.
cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Region')
cur.fetchall()

# You can also sort in DESCending order.
cur.execute('''SELECT Region, Population FROM PopByRegion
                   ORDER BY Population DESC''')
cur.fetchall()


# You can select a subset of rows with the WHERE clause.
cur.execute('SELECT Region FROM PopByRegion WHERE Population > 1000000')
cur.fetchall()


# You can use logical operators like AND, OR, and NOT in the WHERE clause.
cur.execute('''SELECT Region FROM PopByRegion
                   WHERE Population > 1000000 AND Region < "L"''')
cur.fetchall()
# Notice how the < operator works on strings.


##################################################
# Joining Data from Tables
##################################################


# Create another table to experiment with joins.
cur.execute('''CREATE TABLE PopByCountry(Region TEXT, Country TEXT,
                   Population INTEGER)''')

# We could INSERT the VALUES one at a time, as with PopByRegion above:
# cur.execute('''INSERT INTO PopByCountry VALUES("Eastern Asia", "China",
#                    1285238)''')


# It is easier if we pull the values from a list of tuples.
countries = [("Eastern Asia", "China", 1285238), ("Eastern Asia", "DPR Korea", 24056), ("Eastern Asia", "Hong Kong (China)", 8764), ("Eastern Asia", "Mongolia", 3407), ("Eastern Asia", "Republic of Korea", 41491), ("Eastern Asia", "Taiwan", 1433), ("North America", "Bahamas", 368), ("North America", "Canada", 40876), ("North America", "Greenland", 43), ("North America", "Mexico", 126875), ("North America", "United States", 493038)]

# Now loop through those entries and INSERT the VALUES.
for c in countries:
    cur.execute('INSERT INTO PopByCountry VALUES (?, ?, ?)', (c[0], c[1],
                c[2]))

# As above, the commit method saves the changes. 
con.commit()


cur.execute('''SELECT * FROM   PopByCountry''')
cur.fetchall()


# Inner JOIN
cur.execute('''
SELECT PopByRegion.Region, PopByCountry.Country
FROM   PopByRegion INNER JOIN PopByCountry
WHERE  (PopByRegion.Region = PopByCountry.Region)
AND    (PopByRegion.Population > 1000000)
''')

cur.fetchall()



# Left JOIN
cur.execute('''
SELECT PopByRegion.Region, PopByCountry.Country
FROM   PopByRegion LEFT JOIN PopByCountry
ON  (PopByRegion.Region = PopByCountry.Region)
AND    (PopByRegion.Population > 1000000)
''')

cur.fetchall()



##################################################
# Removing Duplicates
##################################################

# Consider this example:
cur.execute('''
SELECT PopByRegion.Region
FROM PopByRegion INNER JOIN PopByCountry
WHERE (PopByRegion.Region = PopByCountry.Region)
AND ((PopByCountry.Population * 1.0) / PopByRegion.Population > 0.10)''')

cur.fetchall()

# Now repeat with the DISTINCT command.
cur.execute('''
SELECT DISTINCT PopByRegion.Region
FROM PopByRegion INNER JOIN PopByCountry
WHERE (PopByRegion.Region = PopByCountry.Region)
AND ((PopByCountry.Population * 1.0) / PopByRegion.Population > 0.10)''')

cur.fetchall()
# Only unique values remain. 


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
# Nested Queries
##################################################


# Instead of pulling from a table, you can replace 
# the name of a table with a query that produces the required table. 

# Example: Select the list of regions that do not have 
# a country with a population of 8,764,000.



# Information:
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


# As an inermediate step, create a query that creates a table that 
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



# Close the connection when finished. 
con.close()



##################################################
# End
##################################################
