CREATE TABLE orders(CREATE TABLE orders(
    order_id INTEGER,    order_id INTEGER,
    product_id INTEGER,    product_id INTEGER,
    quantity INTEGER,    quantity INTEGER,
     PRIMARY KEY (order_id,product_id)     PRIMARY KEY (order_id,product_id)
););



-- Do not modify below this line ---- Do not modify below this line --
SELECT SELECT 
    c.table_name,    c.table_name,
    c.column_name,     c.column_name, 
    c.data_type,     c.data_type, 
    CASE     CASE 