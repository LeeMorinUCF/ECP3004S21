/*
    Create FirstTable table with variables: KeyID, Date and Name.
    The primary key is KeyID.

    Note that the slash-star symbol creates comments for a header.
    It doesn't count as a first command.
    Also, the semicolon is also used in SQL to denote end of line.
    Also, note that sqlite3 in Python can only execute one SQL command
    at a time.

*/;


CREATE TABLE FirstTable(
KeyID          INTEGER NOT NULL ,
Date           TEXT NOT NULL ,
Name           TEXT NOT NULL ,
PRIMARY KEY    (KeyID)
);
