# Select Distinct

**🔗 [View on NeetCode](https://neetcode.io/problems/sql-select-distinct/question)**

---

It's common to have rows with duplicate values in a database. We can use the `DISTINCT` keyword to remove duplicate rows within one or more columns.

```sql
SELECT DISTINCT author
FROM comments;
```

If we have a table that looks like this:

id
author
body

1
NeetCode
My first comment

2
Lee
Another comment

3
NeetCode
My second comment

4
John
This is another comment

The above query will return:

author

NeetCode

Lee

John

We selected all rows from the `comments` table, but only returned the unique `author` values a single time each.

With `DISTINCT` We can also select multiple columns, which will remove duplicate rows based on the combination of values.

```sql
SELECT DISTINCT author, body
FROM comments;
```

This will return:

author
body

NeetCode
My first comment

Lee
Another comment

NeetCode
My second comment

John
This is another comment

In this case, the `DISTINCT` keyword is applied to the combination of the `author` and `body` columns. This means we will only return rows where the `author` and `body` combination is unique.

#### Challenge

You are given a table called `cities`. Return all unique values from the `country` column.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
