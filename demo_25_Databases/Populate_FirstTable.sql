/*
    Polulate FirstTable table with a few entries.
    Table Firsttable must already exist with variables KeyID, Date and Name.
    The primary key is KeyID.

    Note that since this script contains multiple queries,
    it has to be executed using sqlite3.executescript()
    instead of sqlite3.execute(), which can only handle one command at a time. 

*/;

INSERT INTO FirstTable(KeyID, Date, Name)
VALUES(1, "20131204", "Harry J. Paarsch");
INSERT INTO FirstTable(KeyID, Date, Name)
VALUES(2, "20131204", "Konstantin Golyaev");
INSERT INTO FirstTable(KeyID, Date, Name)
VALUES(3, "20131204", "Alberto M. Segre");
