/*
    This query alculates the average bid for every bidder.
    It then returns only bidders with average bids exceeding
    twelve dollars. It also joins bidder
    names from the Bidders table.
*/;


.mode column
.headers on
.output ComputeBidSummariesAndFilter.out

SELECT
    all_data.FirstName      AS FirstName ,
    all_data.LastName       AS LastName ,
    all_data.SmallestBid    AS SmallestBid ,
    all_data.AverageBid     AS AverageBid ,
    all_data.LargestBid     AS LargestBid

FROM (

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
) AS all_data

WHERE all_data.AverageBid >= 12
;

.output stdout
