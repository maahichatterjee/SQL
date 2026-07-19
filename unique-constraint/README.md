# Unique Constraint

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-unique-constraint/question)

---

## 📋 Problem Description

We may want to ensure that a column or a group of columns have unique values in a table. This is where the UNIQUE constraint comes in. For example, we may want to ensure that no two users have the same email address.

Above, the email column has the UNIQUE constraint. This means that every row in the table must have a unique value for the email column. We also added the NOT NULL constraint to ensure that the email column must have a value.

ChallengeCreate a table called students with the following columns: id of type INTEGER which must be unique and not be NULL

name of type TEXT which must not be NULL

age of type INTEGER which must not be NULL

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
