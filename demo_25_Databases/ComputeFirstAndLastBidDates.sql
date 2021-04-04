/*
    This query alculates the date of first and last bids 
    for every bidder. For this, it combines all three tables 
    from the AuctionsDataBase. 
*/;


.mode column
.headers on
.output ComputeFirstAndLastBidDates.out

SELECT 
    bidders.FirstName  AS FirstName ,
    bidders.LastName   AS LastName ,
    MIN(auctions.Date) AS FirstBidDate ,
    MAX(auctions.Date) AS LastBidDate
FROM
    Bids bids
INNER JOIN 
    Bidders bidders
    ON bids.BidderID = bidders.BidderID
INNER JOIN
(
    SELECT 
        AuctionID, 
        DATE(Year || '-' || Month || '-' || Day) AS Date
    FROM
    (      
       SELECT 
           a.AuctionID ,
           SUBSTR(a.Date, 1, 4) AS Year, 
           SUBSTR(a.Date, 5, 2) AS Month, 
           SUBSTR(a.Date, 7, 2) AS Day 
       FROM
           Auctions a
    )
) auctions
GROUP BY 
    bidders.FirstName ,
    bidders.LastName 
;

.output stdout