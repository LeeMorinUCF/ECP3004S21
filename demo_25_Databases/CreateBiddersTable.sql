/*
    Create Bidders table with variables: BidderID, FirstName, 
    LastName, Address1, Address2, Town, Province, PostalCode, 
    Telephone, Email and Preferred. 
    The primary key is BidderID.

*/;


CREATE TABLE Bidders(
BidderID       INTEGER ,
FirstName      TEXT NOT NULL ,
LastName       TEXT NOT NULL ,
Address1       TEXT NOT NULL ,
Address2       TEXT DEFAULT NULL ,
Town           TEXT NOT NULL ,
Province       TEXT NOT NULL ,
PostalCode     TEXT NOT NULL ,
Telephone      TEXT NOT NULL ,
Email          TEXT DEFAULT NULL ,
Preferred      TEXT ,
PRIMARY KEY    (BidderID)
);
