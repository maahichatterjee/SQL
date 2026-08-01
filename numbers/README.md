# Numbers

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-numbers/question)

---

## 📋 Problem Description

There are several ways to represent numbers in PostgreSQL. Here are the most common ones:

Integers SMALLINT stores a 2 byte signed integer from -32768 to 32767.

INTEGER stores a 4 byte signed integer from -2147483648 to 2147483647.

BIGINT stores an 8 byte signed integer from -9223372036854775808 to 9223372036854775807. Floating-point numbers FLOAT stores a 4 byte floating-point number.

DOUBLE PRECISION stores an 8 byte floating-point number.

DECIMAL stores a fixed-point number, where the precision is specified.

NUMERIC is identical to DECIMAL. When we defined the DECIMAL and NUMERIC columns, we also specified the number of digits to the left and right of the decimal point.

For example, the DECIMAL(10, 2) column can store numbers with up to 10 digits total, and up to 2 digits to the right of the decimal point. This means it can store up to 8 digits to the left of the decimal point, like 12345678.90. 12.345 is not valid since it has 3 digits to the right of the decimal point.

123456789.0 is not valid since it has 9 digits to the left of the decimal point. The NUMERIC(10, 1) column can store numbers with up to to 10 digits total, and up to 1 digit to the right of the decimal point. Reminder: The DECIMAL and NUMERIC data types are identical in PostgreSQL. For consistency, you should only use one of them. ChallengeCreate a table called bank_accounts with the following columns: id of type BIGINT as the primary key

balance of type NUMERIC with up to 20 digits total and 2 digits to the right of the decimal point

interest_rate of type NUMERIC with up to 5 digits total and 2 digits to the right of the decimal point

number_of_owners of type SMALLINT

---

## 💡 Solution

Check the `solution.py` file in this directory for the complete implementation.

---

## 📊 Complexity Analysis

*Add your complexity analysis here after solving*

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

<sub>This problem was automatically synced from NeetCode using [NeetCode GitHub Pusher](https://github.com/)</sub>
