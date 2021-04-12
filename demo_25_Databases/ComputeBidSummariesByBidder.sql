/*
    This query calculates the smallest, the average, and the
    largest bids for every bidder.
*/;


SELECT
    bids.BidderID     AS BidderID ,
    MIN(bids.Bid)     AS SmallestBid ,
    AVG(bids.Bid)     AS AverageBid ,
    MAX(bids.Bid)     AS LargestBid
FROM
    Bids AS bids
GROUP BY
    bids.BidderID
;
