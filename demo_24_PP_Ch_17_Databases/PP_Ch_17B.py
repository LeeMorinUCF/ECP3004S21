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
os.chdir(git_path + 'demo_23_PP_Ch_17_Dictionaries')
# Check that the change was successful.
os.getcwd()




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

