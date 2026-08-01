CREATE TABLE products(CREATE TABLE products(



-- Do not modify below this line ---- Do not modify below this line --
SELECT SELECT 
    c.table_name,    c.table_name,
    c.column_name,     c.column_name, 
    id INTEGER PRIMARY KEY,    id INTEGER PRIMARY KEY,
))
    name TEXT,    name TEXT,
    price INTEGER CHECK (price>=0),    price INTEGER CHECK (price>=0),
    status TEXT CHECK (status IN ('available', 'out of stock'))    status TEXT CHECK (status IN ('available', 'out of stock'))
    c.data_type,     c.data_type, 
    CASE     CASE 
        WHEN pk.column_name IS NOT NULL THEN 'YES'        WHEN pk.column_name IS NOT NULL THEN 'YES'
        ELSE 'NO'        ELSE 'NO'