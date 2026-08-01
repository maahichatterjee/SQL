# Foreign Key

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-foreign-key/question)

---

## 📋 Problem Description

A foreign key is a column or a group of columns in a table that references a column in another table. It establishes a relationship between two tables.

In the above example, we use the keyword REFERENCES to create a foreign key constraint. The owner_id column in the videos table references the id column in the users table. This means that the value in the owner_id column must exist in the id column of the users table.

For example if we have the following rows in the users table: id

name 1

Alice 2

Bob We can have the following rows in the videos table: id

title

owner_id 10

Video 1

1 20

Video 2

2 30

Video 3

2 If we try to insert a row in the videos table with an owner_id of 3, it will fail because there is no user with an id of 3 in the users table. A foreign key does not have to be unique, but it must match an existing value in the referenced column. The referenced column must be a primary key or have a unique constraint. ChallengeCreate a table called departments with the following columns: id of type INTEGER as the primary key

name of type TEXT Create a table called employees with the following columns: id of type INTEGER as the primary key

name of type TEXT

department_id of type INTEGER that references the id column in the departments table

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
