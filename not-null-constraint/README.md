# Not Null Constraint

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-not-null-constraint/question)

---

## 📋 Problem Description

We learned that columns can have default values, and if they don't, the default value is NULL. However, sometimes we want to enforce that a column must have a value. This is where the NOT NULL constraint comes in.

In the example above, the name column is set to NOT NULL. This means that every row in the table must have a value for the name column.

Columns can have both a default value and the NOT NULL constraint.

Above we have added both a default value and the NOT NULL constraint to the columns. The order we place the default value and the NOT NULL constraint for a column does not matter. A constraint in SQLis a rule that is enforced on a column. NOT NULL is only one of many constraints we will learn about. ChallengeCreate a table called products with the following columns: name of type TEXT and must not be NULL, with a default value of 'Unknown'

price of type INTEGER and must not be NULL

quantity of type INTEGER which has a default value of 0

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
