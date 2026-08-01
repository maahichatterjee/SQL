




-- Do not modify below this line ---- Do not modify below this line --
INSERT INTO bank_accounts (id, balance, interest_rate, INSERT INTO bank_accounts (id, balance, interest_rate, 
number_of_owners) VALUESnumber_of_owners) VALUES
    (1, 123451234512345123.45, 123.45, 1);    (1, 123451234512345123.45, 123.45, 1);
    id BIGINT PRIMARY KEY,    id BIGINT PRIMARY KEY,
););
    balance NUMERIC (20,2),    balance NUMERIC (20,2),
    interest_rate NUMERIC (5,2),    interest_rate NUMERIC (5,2),
    number_of_owners SMALLINT    number_of_owners SMALLINT

SELECT SELECT 
CREATE TABLE bank_accounts(CREATE TABLE bank_accounts(