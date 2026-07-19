# Default Values

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-default-values/question)

---

## 📋 Problem Description

Table columns can have default values. When inserting rows into a table it's possible to omit values for some columns. The database will automatically insert NULL for those columns, unless a default value is specified. You can specify a default value for a column when creating a table.

In the above example, the name column has a default value of 'Anonymous', and the age column has a default value of 18. The email column does not have a default value, so it will be NULL if no value is provided.

You can specify a default value by using the DEFAULT keyword followed by the value you want to set. To 'drop' a column, means to remove it from the table. ChallengeCreate a table called videos with the following columns: id of type INTEGER with no default value

name of type TEXT with a default value of 'Untitled'

is_published of type BOOLEAN with a default value of false

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
