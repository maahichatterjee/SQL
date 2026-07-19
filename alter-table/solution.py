CREATE TABLE books (CREATE TABLE books (
  id INTEGER,  id INTEGER,
  title TEXT,  title TEXT,
  author TEXT  author TEXT
););
-- Do not modify above this line ---- Do not modify above this line --

ALTER TABLE books ADD COLUMN published_year INTEGER;ALTER TABLE books ADD COLUMN published_year INTEGER;







ALTER TABLE books RENAME COLUMN id TO isbn;ALTER TABLE books RENAME COLUMN id TO isbn;
ALTER TABLE books DROP COLUMN author;ALTER TABLE books DROP COLUMN author;