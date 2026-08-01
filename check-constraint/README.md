# Check Constraint

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-check-constraint/question)

---

## 📋 Problem Description

A check constraint is a rule that defines valid values for a column. It allows you to specify a condition that each row in a table must satisfy.

In the example above, we added a check constraint to the age column, which ensures that the value of the column is greater than or equal to 18. Check constraints are useful for ensuring data integrity and consistency in a database.

Another example of a check constraint is to ensure that a column only accepts values from a specific set.

In this example, the status column can only have the values 'active' or 'inactive'.

ChallengeCreate a table called products with the following columns: id of type INTEGER as the primary key

name of type TEXT

price of type INTEGER with a check constraint that ensures the price is greater than or equal to 0

status of type TEXT with a check constraint that ensures the status is either 'available' or 'out of stock'

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
