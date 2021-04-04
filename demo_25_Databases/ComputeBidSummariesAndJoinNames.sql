/*
    This query alculates the smallest, the average, and the
    largest bids for every bidder. It also joins bidder 
    names from the Bidders table. 
*/;


.mode column
.headers on
.output ComputeBidSummariesAndJoinNames.out

SELECT 
    bidders.FirstName  AS FirstName ,
    bidders.LastName   AS LastName ,
    MIN(bids.Bid)     AS SmallestBid ,
    AVG(bids.Bid)     AS AverageBid ,
    MAX(bids.Bid)     AS LargestBid
FROM
    Bids bids
INNER JOIN 
    Bidders bidders
    ON bids.BidderID = bidders.BidderID
GROUP BY 
    bidders.FirstName ,
    bidders.LastName 
;

.output stdout