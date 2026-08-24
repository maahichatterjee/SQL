



-- Do not modify below this line --
INSERT INTO gov_employee (name) 

CREATE TABLE gov_employee (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
);
    gov_id INTEGER DEFAULT nextval('gov_id'),

    name TEXT
  VALUES
      ('John Doe'),
      ('Jane Doe'),
      ('Jim Beam');

CREATE SEQUENCE gov_id START WITH 1000 INCREMENT BY 3;