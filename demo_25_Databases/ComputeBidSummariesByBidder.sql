/*
    This query alculates the smallest, the average, and the
    largest bids for every bidder.
*/;


.mode column
.headers on
.output ComputeBidSummariesByBidder.out

SELECT 
    bids.BidderID     AS BidderID ,
    MIN(bids.Bid)     AS SmallestBid ,
    AVG(bids.Bid)     AS AverageBid ,
    MAX(bids.Bid)     AS LargestBid
FROM
    Bids bids
GROUP BY 
    bids.BidderID 
;

.output stdout