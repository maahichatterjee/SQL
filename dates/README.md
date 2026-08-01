# Dates

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-dates/question)

---

## 📋 Problem Description

It's common to record the data and / or time when something happens. PostgreSQL provides a few different data types to store date and time values. Data Type

Description DATE

calendar date (year, month, day) TIME

time of day (hour, minute, second) TIMESTAMP

date and time (year, month, day, hour, minute, second) There are also variations of these data types that include timezone information which you can read more about here.

In the above example: birth_date is a DATE data type that stores the date of birth.

preferred_notification_time is a TIME data type that stores the preferred time for notifications.

last_login is a TIMESTAMP data type that stores the last login date and time. It's rare to store the TIME without a date. You will most commonly use the DATE or TIMESTAMP data type.

ChallengeCreate a table called events with the following columns: id of type INTEGER as the primary key

event_date of type DATE

event_time of type TIME

event_timestamp of type TIMESTAMP Note: With the Postgres engine we are using, the DATE column stores a default time of 00:00:00 which cannot be changed. But this is misleading since the DATE data type only stores the date, not the time.

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
