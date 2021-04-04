/*
    This query returns all bids made by bidder 1.
*/;


.mode column
.headers on
.output SelectBidsForBidder.out

SELECT 
    bids.BidderID     AS BidderID ,
    bids.AuctionID    AS AuctionID ,
    bids.Bid          AS Bid
FROM
    Bids bids
WHERE 
    bids.BidderID = 1
;

.output stdout