# Interview Practice Module — Data / Python / SQL Thinking

This document contains a curated set of **common interview problems** for:

- Data Analyst
- Data Scientist
- Machine Learning Engineer

Focus:

- Problem-solving patterns
- Clear thinking
- Interview readiness

---

# Section 1 — Arrays & Hashing

## Problem 1 — Contains Duplicate

**Description**
Given an integer array `nums`, return `true` if any value appears at least twice.

**Example**

```
Input: nums = [1,2,3,1]
Output: true
```

```
Input: nums = [1,2,3,4]
Output: false
```

---

## Problem 2 — Two Sum

**Description**
Return indices of the two numbers such that they add up to target.

**Example**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```

---

## Problem 3 — Top K Frequent Elements

**Description**
Return the `k` most frequent elements.

**Example**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

---

## Problem 4 — Valid Anagram

**Description**
Return true if `t` is an anagram of `s`.

**Example**

```
Input: s = "listen", t = "silent"
Output: true
```

---

## Problem 5 — First Unique Character

**Description**
Return the first non-repeating character.

**Example**

```
Input: s = "leetcode"
Output: "l"
```

---

# Section 2 — Sliding Window

## Problem 6 — Longest Substring Without Repeating Characters

```
Input: s = "abcabcbb"
Output: 3
```

---

## Problem 7 — Longest Substring with At Most K Distinct Characters

```
Input: s = "eceba", k = 2
Output: 3
```

---

## Problem 8 — Minimum Size Subarray Sum

```
Input: nums = [2,3,1,2,4,3], target = 7
Output: 2
```

---

## Problem 9 — Maximum Average Subarray (Fixed Window)

```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
```

---

# Section 3 — Prefix Sum

## Problem 10 — Subarray Sum Equals K

```
Input: nums = [1,1,1], k = 2
Output: 2
```

---

## Problem 11 — Running Sum

```
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
```

---

## Problem 12 — Pivot Index

```
Input: nums = [1,7,3,6,5,6]
Output: 3
```

---

# Section 4 — Two Pointers

## Problem 13 — Valid Palindrome

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
```

---

## Problem 14 — Two Sum II (Sorted)

```
Input: nums = [2,7,11,15], target = 9
Output: [1,2]
```

---

## Problem 15 — Container With Most Water

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

---

# Section 5 — Data Style Problems

## Problem 16 — Group Transactions by User

```
Input:
[("user1",100), ("user2",50), ("user1",200)]

Output:
{
  "user1": [100,200],
  "user2": [50]
}
```

---

## Problem 17 — Merge Users and Orders

```
Input:
users = [{id:1,name:"Ana"}]
orders = [{id:1,amount:100}]

Output:
[{id:1,name:"Ana",orders:[100]}]
```

---

## Problem 18 — Count Events per User

```
Input:
events = ["u1","u2","u1"]

Output:
{"u1":2,"u2":1}
```

---

# 🔹 Section 6 — Interval Problems

## Problem 19 — Merge Intervals

```
Input: [[1,3],[2,6],[8,10]]
Output: [[1,6],[8,10]]
```

---

## Problem 20 — Meeting Rooms

```
Input: [[0,30],[5,10],[15,20]]
Output: false
```

---

# 🔹 Section 7 — SQL Thinking (Translate mentally to Pandas)

## Problem 21 — First Purchase After Signup

```
users:
id | signup_date

orders:
id | order_date

Output:
first order after signup per user
```

---

## Problem 22 — Reactivated Users

```
Definition:
gap >= 30 days between orders

Output:
month | reactivated_users
```

---

## Problem 23 — Sessionization

```
Definition:
new session if gap > 30 min

Output:
user_id | session_id | events_count
```

---

## Problem 24 — Daily Active Users (DAU)

```
Input:
events(user_id, date)

Output:
date | unique_users
```

---

# 🔹 Section 8 — Harder Patterns

## Problem 25 — Longest Consecutive Sequence

```
Input: [100,4,200,1,3,2]
Output: 4
```

---

## Problem 26 — Product of Array Except Self

```
Input: [1,2,3,4]
Output: [24,12,8,6]
```

---

## Problem 27 — Gas Station

```
Input:
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3
```

---

# How to Use This

- Solve 3–5 problems per day
- Explain your solution out loud
- Focus on patterns, not memorization
- Time yourself (important)

---

# Goal

Become fast, clear, and confident in interviews.
