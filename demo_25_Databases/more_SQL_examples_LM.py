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
# April 12, 2021
# 
# More Examples with SQL and Databases
# Using SQL Scripts
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

import csv # To import tables from csv files


##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
drive_path = 'C:\\Users\\le279259\\OneDrive - University of Central Florida\\Documents\\'
# git_path = 'Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\'
git_path = 'GitHub\\ECP3004S21\\'
os.chdir(drive_path + git_path + 'demo_25_Databases')
# Check that the change was successful.
os.getcwd()


##################################################
# Basic SQL Example with Scripts
##################################################



#--------------------------------------------------
# Connect to the database (open a new database)
#--------------------------------------------------


# Create a database, if it does not already exist.
con = sqlite3.connect('example.db')

# Create a cursor object from which to execute
# SQL commands.
cur = con.cursor()


#--------------------------------------------------
# Create a Table and Read Data
#--------------------------------------------------

# Read the data from a script. 
sql_str = open("Create_FirstTable.sql").read()
# It reads a string containing the commands in the script.

# See what's inside:
print(sql_str)
# It has a header in comments and a command to CREATE a TABLE.
# and few commands to INSERT VALUES INTO
# a TABLE called FirstTable. 

# Execute this command to create the table. 
cur.execute(sql_str)


# Now run a command to see what we have created.
# This can get the schema of the table,
# which states the names of the variables and the data types.
cur.execute("PRAGMA table_info('FirstTable')").fetchall()




# Read another script to populate the table. 
sql_str = open("Populate_FirstTable.sql").read()


# See what's inside:
print(sql_str)
# It has a few commands to INSERT VALUES INTO
# the TABLE called FirstTable. 

# Execute this command to create the table. 
cur.execute(sql_str)
# Traceback (most recent call last):
# 
#   File "<ipython-input-12-b72e08793f2d>", line 1, in <module>
#     cur.execute(sql_str)
# 
# Warning: You can only execute one statement at a time.


# Since this is a script, containing multiple commands, 
# you need to use executescript().
cur.executescript(sql_str)


# Now run a query to see the contents of the table.
cur.execute('''SELECT * FROM FirstTable''')

cur.fetchall()


# Now that we know how to read in multiple commands, 
# we could have done all of this in one step. 

# Let's DROP this TABLE to do it again. 
cur.execute('DROP TABLE FirstTable')

# Now everything to initialize the table is in a single script.
sql_str = open("FirstTable.sql").read()
print(sql_str)
cur.executescript(sql_str)


# Now run a query to see the contents of the table.
cur.execute('''SELECT * FROM FirstTable''')
cur.fetchall()
# Back where we were before. 

#--------------------------------------------------
# Create another Table and Read Data
#--------------------------------------------------


# Now, let's repeat to add another table to the database. 
sql_str = open("SecondTable.sql").read()
print(sql_str)
cur.executescript(sql_str)


# Now run a query to see the contents of the table.
cur.execute('''SELECT * FROM SecondTable''')
cur.fetchall()


#--------------------------------------------------
# Operations on a Single Table
#--------------------------------------------------

# Now you can perform operations on your tables, 
# just as we did before. 

# To see the table entered above, 
# you can execute the simplest SQL query

cur.execute("SELECT * FROM FirstTable")
cur.fetchall()

# which will return the entire table.

# You can execute a query with a restriction by adding a WHERE clause.

cur.execute("SELECT * FROM FirstTable WHERE KeyID > 1")
cur.fetchall()

# Alternatively, you can execute a query with a *projection* 
# by specifying the names of the fields.

cur.execute("SELECT Name, Date FROM FirstTable")
cur.fetchall()

# If you prefer variables that are functions of the fields
# in the table, you can specify them with additional functions. 

# Notice that the backslash \
# allows a string to continue to the next line. 

cur.execute(
    "SELECT \
        Name ,\
        SUBSTR(Date, 1, 4) AS Year \
    FROM FirstTable"
)
cur.fetchall()



# Finally, you can combine these operations in a more complex query.

cur.execute(
    "SELECT \
        Name ,\
            SUBSTR(Date, 1, 4) as Year \
    FROM \
        FirstTable \
    WHERE KeyID > 1 \
"
)
cur.fetchall()


#--------------------------------------------------
# Combining more than one table
#--------------------------------------------------

# For a small example like this, 
# you can output the tables to screen
# to remind yourself what we will be joining. 

cur.execute("SELECT * FROM FirstTable;")
cur.fetchall()


cur.execute("SELECT * FROM SecondTable;")
cur.fetchall()


# With two tables, you can implement 
# what's often called a *theta join*. 

cur.execute(
    "SELECT \
        FirstTable.KeyID , \
        SecondTable.KeyID , \
        FirstTable.Name \
    FROM \
        FirstTable , \
        SecondTable \
    WHERE \
        (FirstTable.Name = SecondTable.Name) \
    AND \
        (FirstTable.KeyID = SecondTable.OtherID) \
    ;"
    )
cur.fetchall()


# In this case, we simply list the tables
# and select out he non-matching pairs of entries 
# with a WHERE clause. 

# We will explore this further in a richer exampe below. 


#--------------------------------------------------
# Commit changes and close the connection
#--------------------------------------------------

# Before we move on, you might want to: 

# Use the commit method to save the changes. 
# con.commit()


# Close the connection when finished. 
# con.close()

# Then you can continue with this file when you have time
# to work on it later.



##################################################
# Auctions Database with Scripts
##################################################

# This example is based on the records from a series of auctions. 
# At each aution, there is a record of the bids made by each bidder.
# These data are collected into three tables: Auctions, Bids and Bidders.

# In this example, the procedure is made more scalable 
# by reading the tables from .csv files. 
# The procedure is very similar, 
# aside from the commands for reading in the data.

#--------------------------------------------------
# Connect to the database (open a new database)
#--------------------------------------------------

con = sqlite3. connect("AuctionsDataBase.db")
cur = con. cursor()


#--------------------------------------------------
# Create the Tables
#--------------------------------------------------

# Now everything to initialize the table is in a single script.

# Create the Auctions table. 

sql_str = open("CreateAuctionsTable.sql").read()
print(sql_str)
cur.executescript(sql_str)

# Create the Bidders table. 

sql_str = open("CreateBiddersTable.sql").read()
print(sql_str)
cur.executescript(sql_str)

# Create the Bids table. 

sql_str = open("CreateBidsTable.sql").read()
print(sql_str)
cur.executescript(sql_str)


#--------------------------------------------------
# Populate Tables by Reading Data from csv Files
#--------------------------------------------------

# We can open csv files and loop through the rows 
# to add each row to populate the tables.

# Start with the Auction table. 
table_file = open("AuctionsTable.csv")
rows = csv.reader(table_file)


# In this case, we use the executemany() method
# to execute a list of queries.
cur. executemany("INSERT INTO Auctions VALUES (?, ?, ?, ?)", rows)

# Verify that it worked.
cur.execute("SELECT * FROM Auctions")
cur.fetchall()


# Now read the data for the Bidders table. 
table_file = open("BiddersTable.csv")
rows = csv.reader(table_file)

cur. executemany("INSERT INTO Bidders VALUES \
                 (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", rows)

# Verify that it worked.
cur.execute("SELECT * FROM Bidders")
cur.fetchall()


# Finally, read the data for the Bids table. 
table_file = open("BidsTable.csv")
rows = csv.reader(table_file)

cur. executemany("INSERT INTO Bids VALUES \
                 (?, ?, ?, ?)", rows)

# Verify that it worked.
cur.execute("SELECT * FROM Bids")
cur.fetchall()


#--------------------------------------------------
# Running Queries to Summarize the Data
#--------------------------------------------------

# Now let's execute a query: ComputeBidSummariesByBidder.sql.
# The above query performs two main actions. 
# First, it aggregates data by bidder. 
# Second, it calculates values for each bidder. 


# In principle, you can write your queries in scripts
# and some samples are shown above, such as: 
# sql_str = open("ComputeBidSummariesByBidder.sql").read()
# print(sql_str)
# cur.executescript(sql_str)
# cur.fetchall()

# Note that they are written in another dialect of SQL, 
# which specifies the format of the outputs and 
# directs the output to specific files. 

# Instead, we will execute the queries 
# by entering them in a string. 
cur.execute(" \
            SELECT \
                b.BidderID     AS BidderID , \
                MIN(b.Bid)     AS SmallestBid , \
                AVG(b.Bid)     AS AverageBid , \
                MAX(b.Bid)     AS LargestBid \
            FROM \
                Bids AS b \
            GROUP BY \
                b.BidderID \
            ;")
cur.fetchall()

# Notice that we use the keyword "AS" for both the 
# variables and the tables:
# Since we are calculating the variables, they do not have names.
# For the table, we can abbreviate the name, 
# which is often useful in practice when the name of the table
# might be uninformative or excessively long. 


#--------------------------------------------------
# Aggregation
#--------------------------------------------------

# The aggregation step allows you to calculate functions 
# of the data and tabulate them by different values 
# of a particular variable.

cur.execute(" \
            SELECT \
                AVG(bids.Bid) AS AverageBid \
            FROM \
                Bids AS bids \
            GROUP BY \
                bids.BidderID \
            ;"
            )
cur.fetchall()


# You can add unique variables by the grouping variable.

cur.execute(" \
            SELECT \
                bids.BidderID, \
                AVG(bids.Bid) AS AverageBid \
            FROM \
                Bids AS bids \
            GROUP BY \
                bids.BidderID \
            ;"
            )
cur.fetchall()


#--------------------------------------------------
# Joins
#--------------------------------------------------


# An intermediate step is to join together two tables 
# by the join key BidderID.

cur.execute(
            "SELECT \
                bidders.BidderID, \
                bidders.FirstName, \
                bidders.LastName, \
                bids.Bid \
            FROM \
                Bids AS bids \
            INNER JOIN Bidders AS bidders \
                ON bids.BidderID = bidders.BidderID \
            ;"
)
cur.fetchall()

# The INNER JOIN but one of several kinds of joins possible. 
# Since a feature of this database is that 
# every bid corresponds to one bidder in the bidder table, 
# this example is not rich enough to demonstrate 
# the various kinds of joins. As part of these examples, 
# the query is made more complex by introducing subqueries 
# in the place of the joined tables, 
# WHERE the table on one side is missing some rows, 
# to illustrate what happens when this is the case.

# Left Join

# The ```LEFT JOIN``` collects all of the entries that appear in the *first*, 
# or ```LEFT``` table but are not necessarily in both tables.


cur.execute(
            "SELECT \
                bidders.BidderID, \
                bidders.FirstName, \
                bidders.LastName, \
                AVG(bids.Bid) AS AverageBid \
            FROM \
                Bids AS bids \
            LEFT JOIN (SELECT * FROM Bidders WHERE BidderID < 6) AS bidders \
                ON bids.BidderID = bidders.BidderID \
            GROUP BY \
                bidders.BidderID, \
                bidders.FirstName, \
                bidders.LastName \
            ;"
            )
cur.fetchall()


# Right Join

# The ```RIGHT JOIN``` collects all of the entries that appear in the *second*, 
# or ```RIGHT``` table but are not necessarily in both tables.


cur.execute(
            "SELECT \
                bidders.BidderID, \
                bidders.FirstName, \
                bidders.LastName, \
                AVG(bids.Bid) AS AverageBid \
            FROM \
                (SELECT * FROM Bids WHERE BidderID > 2) AS bids \
            RIGHT JOIN Bidders AS bidders \
                ON bids.BidderID = bidders.BidderID \
            GROUP BY \
                bidders.BidderID, \
                bidders.FirstName, \
                bidders.LastName \
            ;"
            )
cur.fetchall()

# Traceback (most recent call last):
# 
#   File "<ipython-input-89-6dbd0f81c504>", line 1, in <module>
#     cur.execute(
# 
# OperationalError: RIGHT and FULL OUTER JOINs are not currently supported



# Notice that sqlite3 will complain if you try to do a ```RIGHT JOIN```. 
# That is part of what makes it "lite". 
# It is not much of a loss, however, 
# because a ```RIGHT JOIN``` can be done with a ```LEFT JOIN```, 
# with the tables A and B switched. 



cur.execute(
            "SELECT \
                bidders.BidderID, \
                bidders.FirstName, \
                bidders.LastName, \
                AVG(bids.Bid) AS AverageBid \
            FROM \
                Bidders AS bidders \
            LEFT JOIN (SELECT * FROM Bids WHERE BidderID > 2) AS bids \
                ON bids.BidderID = bidders.BidderID \
            GROUP BY \
                bidders.BidderID, \
                bidders.FirstName, \
                bidders.LastName \
            ;"
            )
cur.fetchall()



# Inner Join

# The ```INNER JOIN``` collects all of the entries that appear in *both* tables. 


cur.execute(
            "SELECT \
                bidders.BidderID, \
                bidders.FirstName, \
                bidders.LastName, \
                AVG(bids.Bid) AS AverageBid \
            FROM \
                (SELECT * FROM Bids WHERE BidderID > 2) AS bids \
            INNER JOIN (SELECT * FROM Bidders WHERE BidderID < 6) AS bidders \
                ON bids.BidderID = bidders.BidderID \
            GROUP BY \
                bidders.BidderID, \
                bidders.FirstName, \
                bidders.LastName \
            ;"
            )
cur.fetchall()


# As with a ```RIGHT JOIN```, an ```INNER JOIN``` can be done 
# with a ```LEFT JOIN```, 
# with a ```WHERE``` clause to exclude missing values in table B. 



# Outer Join

# The ```OUTER JOIN``` collects all of the entries that appear in *any* of the tables. 

cur.execute(
            "SELECT \
                bidders.BidderID, \
                bidders.FirstName, \
                bidders.LastName, \
                AVG(bids.Bid) AS AverageBid \
            FROM \
                (SELECT * FROM Bids WHERE BidderID > 2) AS bids \
            FULL OUTER JOIN (SELECT * FROM Bidders WHERE BidderID < 6) AS bidders \
                ON bids.BidderID = bidders.BidderID \
            GROUP BY \
                bidders.BidderID, \
                bidders.FirstName, \
                bidders.LastName \
            ;"
            )
cur.fetchall()

# Traceback (most recent call last):
# 
#   File "<ipython-input-91-309ed246d196>", line 1, in <module>
#     cur.execute(
# 
# OperationalError: RIGHT and FULL OUTER JOINs are not currently supported

# As with RIGHT JOINs, sqlite3 does not have this functionality. 
# It can, however, be accomplished with 
# two queries with RIGHT and LEFT JOINs
# that are stacked with a UNION clause 
# and the DISTINCT qualifier to eliminate duplicate entries 
# that appear in both tables. 

# With this in mind, you can usually achieve anything you need to 
# with a LEFT JOIN,  so sqlite3 is not as light as it may seem. 


#--------------------------------------------------
# Filters
#--------------------------------------------------

# Additionally, one can select a subset of rows 
# satisfying certain criteria, 
# with a WHERE clause or a HAVING clause, 
# in addition to the joins made in the table.

# See the script ComputeBidSummariesAndFilter.sql 
# to see such an example using a WHERE clause. 



##################################################
# Extra code snippets
##################################################


# This can get the schema of the table,
# cur.execute("PRAGMA table_info('Table_Name')").fetchall()
# which states the names of the variables and the data types.

# In case things go wrong, you can always drop the table
# and start over:
# cur.execute('DROP TABLE Table_Name')


##################################################
# End
##################################################

