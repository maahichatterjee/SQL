# Select In

**🔗 [View on NeetCode](https://neetcode.io/problems/sql-select-in/question)**

---

We can use the `IN` operator to filter rows based on a list of values.

```text
SELECT *
FROM cities
WHERE name IN ('New York', 'London', 'Paris');
```

The above query will return all rows where the `name` column is either `New York`, `London`, or `Paris`. We use the parentheses to specify the list of values.

#### Challenge

You are given a table called `cities`. Return *only the names of the cities* that are in the following countries: `USA`, `Canada`, and `Mexico`.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
