# Select Where Comparison

**🔗 [View on NeetCode](https://neetcode.io/problems/sql-select-where-comparison/question)**

---

We can also use comparison operators like `<`, `>`, `<=`, and `>=`, similar to most programming languages.

```sql
SELECT *
FROM users
WHERE age > 20; -- Users older than 20

SELECT *
FROM users
WHERE age >= 20; -- Users 20 years or older

SELECT *
FROM users
WHERE age < 20; -- Users younger than 20
```

Rather than comparing a column to a value, we could also compare two columns together. This works with any of the comparison operators we have discussed.

#### Challenge

You are given a table called `basketball_boxscore`. Use the `SELECT` statement to select all columns, and return only the rows where the points scored by the away team is greater than the points scored by the home team.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
