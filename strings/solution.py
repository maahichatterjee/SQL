CREATE TABLE (operating_systems)(CREATE TABLE (operating_systems)(







-- Do not modify below this line ---- Do not modify below this line --
INSERT INTO operating_systems (id, name, version, market_share) INSERT INTO operating_systems (id, name, version, market_share) 
VALUESVALUES
    (1, 'Windows', '10', 75.51),    (1, 'Windows', '10', 75.51),
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
););
    name VARCHAR(255),    name VARCHAR(255),
    version CHAR(10),    version CHAR(10),
    market_share NUMERIC(5,2)    market_share NUMERIC(5,2)