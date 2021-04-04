/*
    Create Auctions table with variables: AuctionID, Volume, 
    District and Date.
    The primary key is AuctionID.

*/;


CREATE TABLE Auctions(
AuctionID      INTEGER ,
Volume         INTEGER NOT NULL ,
District       INTEGER NOT NULL ,
Date           TEXT NOT NULL ,
PRIMARY KEY    (AuctionID)
);
