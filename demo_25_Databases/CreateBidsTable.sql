/*
    Create Bids table with variables: BidID, AuctionID, BidderID, 
    and Bid.
    The primary key is BidID. 

*/;


CREATE TABLE Bids(
BidID          INTEGER ,
AuctionID      INTEGER NOT NULL ,
BidderID       INTEGER NOT NULL ,
Bid            REAL ,
FOREIGN KEY    (AuctionID) REFERENCES Auctions (AuctionID) ,
FOREIGN KEY    (BidderID) REFERENCES Bidderss (BidderID) ,
PRIMARY KEY    (BidID)
);
