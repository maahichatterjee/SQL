# Arrays

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-arrays/question)

---

## 📋 Problem Description

PostgreSQL also supports arrays, which allow us to store a collection of values of the same type.

Above, we have a table called users with a course_list column that stores an array of strings. We can insert multiple courses for each user by using the ARRAY keyword. Arrays in PostgreSQL are 1-indexed, meaning the first element is at index 1, the second at index 2, and so on. PostgreSQL also supports multi-dimensional arrays and more, which you can read more about here. In most cases, it's more common to normalize data into separate tables rather than using arrays. We will cover this later in the course.

ChallengeCreate a table called orders with the following columns: id of type INTEGER as the primary key

items of type array of TEXT

total_price of type INTEGER

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
