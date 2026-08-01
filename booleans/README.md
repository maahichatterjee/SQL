# Booleans

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-booleans/question)

---

## 📋 Problem Description

There are many data types supported in SQL. For a full list, check out the PostgreSQL documentation.

We will be covering the most common data types in this course.

Booleans are a type of data that can only be true or false, similar to most programming languages.

In the above example, the is_active column can only have the values true or false. We use INSERT INTO to insert the values into the table. We will learn more about INSERT INTO later, but for now it's enough to know that each row is represented by (), and the values inside correspond to the columns in the table.

Notice that there are many different ways to represent a boolean value in SQL. For example, true can be represented as TRUE, true, t, y, or 1.

Similarly, false can be represented as FALSE, false, f, n, or 0. For consistency, it's best to stick to a single representation of a boolean value in SQL, using either TRUE or FALSE, or true or false.

ChallengeCreate a table called three_column_table with the following columns: id of type INTEGER as the primary key

is_active of type BOOLEAN

is_admin of type BOOLEAN

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
