/*
    Create SecondTable table with variables: KeyID, OtherID and Name.
    The primary key is KeyID.

*/;


CREATE TABLE SecondTable(
KeyID          INTEGER NOT NULL ,
OtherID        INTEGER NOT NULL ,
Name           TEXT NOT NULL ,
FOREIGN KEY    (OtherID) REFERENCES FirstTable (KeyID)
PRIMARY KEY    (KeyID)
);


INSERT INTO SecondTable(KeyID, OtherID, Name)
VALUES(101, 1, "Harry J. Paarsch");
INSERT INTO SecondTable(KeyID, OtherID, Name)
VALUES(102, 2, "Konstantin Golyaev");
