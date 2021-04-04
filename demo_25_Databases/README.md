# Interacting with Databases

Now that we know how to interact with a database, 
we will consider a few more examples. 
This time, we will progress toward a more generalized method of interacting
with databases: will will write SQL scripts. 
SQL is a language in its own right, so it makes sense 
to write your queries in dedicated SQL scripts. 
This way, the same operations can be used on a number of different platforms:
you could run them in the GUI of a database manager, 
you could submit them through a terminal window 
(such as when I run your my_module.py scripts), 
and you can read the text of the SQL query in Python 
and use the ```sqlite3``` module.

## Basic SQL Example

We'll start with a simple example before we get too far. 

### Operations on a single table

First specify the schema of the first table

```
CREATE TABLE FirstTable(
KeyID          INTEGER NOT NULL ,
Date           TEXT NOT NULL ,
Name           TEXT NOT NULL ,
PRIMARY KEY    (KeyID)
);
```

To verify the above, you can verify the schema by using the ```.schema``` command at the ```sqlite``` prompt. 
Aside from checking for mistakes made on input, this is epecially useful for understanding a database created by someone else. 

You can then populate ```FirstTable``` with a few entries as follows

```
INSERT INTO FirstTable(KeyID, Date, Name)
VALUES(1, "20131204", "Harry J. Paarsch");
INSERT INTO FirstTable(KeyID, Date, Name)
VALUES(2, "20131204", "Konstantin Golyaev");
INSERT INTO FirstTable(KeyID, Date, Name)
VALUES(3, "20131204", "Alberto M. Segre");
```
To see the table entered above, you can execute the simplest SQL query
```
SELECT * FROM FirstTable;
```
which will return the entire table. 

You can execute a query with a restriction by adding a ```WHERE``` clause

```
SELECT * FROM FirstTable WHERE KeyID > 1;
```

Alternatively, you can execute a query with a projection by specifying the fields
```
SELECT Name, Date FROM FirstTable;
```

If you prefer variables that are functions of the fields in the table, you can specify them with additional functions
```
SELECT 
    Name ,
    SUBSTR(Date 1, 4) as Year 
FROM FirstTable;
```


Finally, you can combine these operations in a more complex query

```
SELECT 
    Name ,
    SUBSTR(Date 1, 4) as Year 
FROM 
    FirstTable
WHERE KeyID > 1;
```

### Combining more than one table

Again, first specify the schema of this table

```
CREATE TABLE SecondTable(
KeyID          INTEGER PRIMARY KEY ,
OtherID        INTEGER PRIMARY KEY ,
Name           TEXT NOT NULL ,
FOREIGN KEY    (OtherID) REFERENCES FirstTable (KeyID)
PRIMARY KEY    (KeyID)
);
```


Next populate ```SecondTable``` with a few entries as follows

```
INSERT INTO SecondTable(KeyID, OtherID, Name)
VALUES(101, 1, "Harry J. Paarsch");
INSERT INTO SecondTable(KeyID, OtherID, Name)
VALUES(102, 2, "Konstantin Golyaev");
```

Now you can verify the contents of the database with ```.tables``` and ```.schema```

In addition, for a small example like this, you can output the tables to screen

```
SELECT * FROM FirstTable;
```
```
SELECT * FROM SecondTable;
```

With two tables, you can implement a theta join

```
SELECT 
    FirstTable.KeyID ,
    SecondTable.KeyID ,
    FirstTable.Name
FROM
    FirstTable ,
    SecondTable
WHERE 
    (FirstTable.Name = SecondTable.Name)
AND
    (FirstTable.KeyID = SecondTable.OtherID)
;
```

### Using Command Files

While you might type faster than I do, what you type at the prompt would have to be re-entered to make any modifications. In addition, there would be no record of what you entered.

If your commands are collected into ```.sql``` scripts then it would serve as a form of documentation, enabling someone else to build upon your work in the future.

See the scripts ```FirstTable.sql```, ```SecondTable.sql``` and ```ExampleThetaJoin.sql``` above.

You can create the first table by running the command 

```
sqlite> .read FirstTable.sql
```
at the ```sqlite>``` prompt and likewise for the second table. 
Verify the result by entering ```.tables``` and ```.schema```.

RUn the sample query by entering 
```
sqlite> .read ExampleThetaJoin.sql
```
at the ```sqlite>``` prompt.

To see the result, type ```more ExampleThetaJoin.csv``` in a terminal window. 




## Auctions Database

In this example, the procedure is made more scalable by reading the tables from ```.csv``` files.
The procedure is very similar, aside from the commands for reading in the data.

Open a new database in sqlite3

```
sqlite3 AuctionsDataBase.db
```
Next, read in the scripts ```CreateAuctionsTable.sql```, ```CreateBiddersTable.sql``` and ```CreateBidsTable.sql``` to create the tables, just as for the sample database.

As above, you can verify the entry by executing the ```.tables``` and ```.schema``` commands.

The next step is to populate the tables with the ```.csv``` files associated with each, using the ```.import``` command.
```
.separator ,
.import AuctionsTable.csv Auctions
.import BiddersTable.csv Bidders
.import BidsTable.csv Bids
```
You can still verify the contents of the tables with the query
```
sqlite> SELECT * FROM Auctions;
```
and so on but we will move on to the scripted queries instead.

To view the products of the queries, you may want to keep open a terminal window to view the output of ```ls``` before and after the query to see the output file created.

As above, execute the queries using the ```.read``` command at the ```sqlite>``` prompt.

```
sqlite> .read ComputeBidSummariesByBidder.sql
```
Now you can view the table ```ComputeBidSummariesByBidder.out``` as specified in the script.
The procedure is the same for the other queries.

The above query performs two main actions. 
First, it aggregates data by bidder. Second, it joins data from two different tables. 
Let's look at these two components separately. 


### Aggregation 

The aggregation step allows you to calculate functions of the data and tabulate them by different values of a particular variable. 

```
SELECT 
    AVG(bids.Bid) AS AverageBid
FROM
    Bids AS bids
GROUP BY
    bids.BidderID
;
```

You can add unique variables by the grouping variable.

```
SELECT 
    bids.BidderID,
    AVG(bids.Bis) AS AverageBid
FROM
    Bids AS bids
GROUP BY
    bids.BidderID
;
```





### Joins

An intermediate step is to join together two tables by the join key BidderID. 

```
SELECT 
    bidders.BidderID,
    bidders.FirstName,
    bidders.LastName,
    bids.Bid
FROM
    Bids AS bids
INNER JOIN Bidders AS bidders
    ON bids.BidderID = bidders.BidderID
;
```

This is but one of several kinds of joins possible. 
Since a feature of this database is that every bid corresponds to one bidder in the bidder table, this example is not rich enough to demonstrate the various kinds of joins. 
As part of these examples, the query is made more complex by introducing subqueries in the place of the joined tables.



<img src="Images/join_diagram.jpg" width="500">

Perhaps a better way of representing the join is by
picturing two simple databases in the rectangular form of the data. 
Assume that the vertical position represents entries with the same key. 
Then the two databases will be joined in the following ways.

<img src="Images/join_tables.png" width="500">

Notice the blank spaces where there is no corresponding value
from one of the tables. 

There also exists a type of join called a cross-join. 
It has the following structure. 

<img src="Images/cross_join_tables.png" width="500">

This is not used as often but is also shown for completeness. 
Examples of these joins are as follows. 


#### Left Join


```
SELECT 
    bidders.BidderID,
    bidders.FirstName,
    bidders.LastName,
    AVG(bids.Bid) AS AverageBid
FROM
    Bids AS bids
LEFT JOIN (SELECT * FROM Bidders WHERE BidderID < 6) AS bidders
    ON bids.BidderID = bidders.BidderID
GROUP BY 
    bidders.BidderID,
    bidders.FirstName,
    bidders.LastName
;
```

#### Right Join

```
SELECT 
    bidders.BidderID,
    bidders.FirstName,
    bidders.LastName,
    AVG(bids.Bid) AS AverageBid
FROM
    (SELECT * FROM Bids WHERE BidderID > 2) AS bids
RIGHT JOIN Bidders AS bidders
    ON bids.BidderID = bidders.BidderID
GROUP BY 
    bidders.BidderID,
    bidders.FirstName,
    bidders.LastName
;
```


#### Inner Join

```
SELECT 
    bidders.BidderID,
    bidders.FirstName,
    bidders.LastName,
    AVG(bids.Bid) AS AverageBid
FROM
    (SELECT * FROM Bids WHERE BidderID > 2) AS bids
INNER JOIN (SELECT * FROM Bidders WHERE BidderID < 6) AS bidders
    ON bids.BidderID = bidders.BidderID
GROUP BY 
    bidders.BidderID,
    bidders.FirstName,
    bidders.LastName
;
```



#### Outer Join

```
SELECT 
    bidders.BidderID,
    bidders.FirstName,
    bidders.LastName,
    AVG(bids.Bid) AS AverageBid
FROM
    (SELECT * FROM Bids WHERE BidderID > 2) AS bids
FULL OUTER JOIN (SELECT * FROM Bidders WHERE BidderID < 6) AS bidders
    ON bids.BidderID = bidders.BidderID
GROUP BY 
    bidders.BidderID,
    bidders.FirstName,
    bidders.LastName
;
```



### Filters


Additionally, one can select a subset of rows staisfying certain criteria. 

Run the script ```ComputeBidSummariesAndFilter.sql``` to see such an example using a ```WHERE``` clause. 
In the textbook, you will find an alternative approach using a ```HAVING``` clause. 




