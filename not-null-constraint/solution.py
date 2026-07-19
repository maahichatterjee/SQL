  name TEXT NOT NULL DEFAULT 'Unknown',  name TEXT NOT NULL DEFAULT 'Unknown',
CREATE TABLE products (CREATE TABLE products (
  price INTEGER NOT NULL,  price INTEGER NOT NULL,
  quantity INTEGER DEFAULT '0',  quantity INTEGER DEFAULT '0',
););

-- Do not modify below this line ---- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_defaultSELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columnsFROM information_schema.columns
WHERE table_name = 'products';WHERE table_name = 'products';
