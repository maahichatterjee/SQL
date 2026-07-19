CREATE TABLE unused_table (CREATE TABLE unused_table (
  id INTEGER,  id INTEGER,
  name TEXT  name TEXT
););
-- Do not modify above this line ---- Do not modify above this line --
DROP TABLE unused_table;DROP TABLE unused_table;




-- Do not modify below this line ---- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_defaultSELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columnsFROM information_schema.columns
WHERE table_name = 'unused_table';WHERE table_name = 'unused_table';
