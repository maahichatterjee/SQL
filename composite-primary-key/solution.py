CREATE TABLE orders(CREATE TABLE orders(



-- Do not modify below this line ---- Do not modify below this line --
SELECT SELECT 
    c.table_name,    c.table_name,
    c.column_name,     c.column_name, 
    c.data_type,     c.data_type, 
    CASE     CASE 
        WHEN kcu.column_name IS NOT NULL THEN         WHEN kcu.column_name IS NOT NULL THEN 
            CASE             CASE 
    order_id INTEGER,    order_id INTEGER,
););
    product_id INTEGER,    product_id INTEGER,
    quantity INTEGER,    quantity INTEGER,
    COMPOUND PRIMARY KEY (order_id,product_id)    COMPOUND PRIMARY KEY (order_id,product_id)