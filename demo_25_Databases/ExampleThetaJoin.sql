/*
    This query joins the SecondTable KeyID with the Name and KeyID from FirstTable.
*/;


.separator ,
.mode csv
.output ExampleThetaJoin.csv
SELECT 
    FirstTable.KeyID ,
    SecondTable.KeyID ,
    FirstTable.Name
FROM
    FirstTable ,
    SecondTable
WHERE 
    (FirstTable.Name = SecondTable.Name)
AND
    (FirstTable.KeyID = SecondTable.OtherID)
;