/*
    This query calculates the smallest, the average, and the
    largest bids for every bidder.
*/;


SELECT
    b.BidderID     AS BidderID ,
    MIN(b.Bid)     AS SmallestBid ,
    AVG(b.Bid)     AS AverageBid ,
    MAX(b.Bid)     AS LargestBid
FROM
    Bids AS b
GROUP BY
    b.BidderID
