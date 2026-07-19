CREATE TABLE users(CREATE TABLE users(
  name TEXT  name TEXT
););


-- Do not modify below this line ---- Do not modify below this line --
SELECT table_name, column_name, data_typeSELECT table_name, column_name, data_type
FROM information_schema.columnsFROM information_schema.columns
WHERE table_name = 'users';WHERE table_name = 'users';
