# Composite Primary Key

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-composite-primary-key/question)

---

## 📋 Problem Description

A primary key can also be made up of multiple columns. This is known as a compound primary key or a composite primary key. It is used when a single column cannot uniquely identify each row in a table.

The combination of columns in a compound primary key must be unique for each row. The combination of values in the columns must be unique, even if the individual columns are not.

In the example above, the primary key of the employees table is a combination of the department_id and employee_id columns. This means that the combination of values in these two columns must be unique for each row.

Notice that we defined the PRIMARY KEY constraint after the column list. This is another way to add a primary key to a table, and is the required approach for composite primary keys.

ChallengeCreate a table called orders with the following columns: order_id of type INTEGER

product_id of type INTEGER

quantity of type INTEGER

A compound primary key consisting of the order_id and product_id columns.

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
