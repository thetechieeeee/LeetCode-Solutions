# 258. Add Digits
**Topics:** Math, Simulation
**Languages:** Python, Java

## Problem Description

Given an integer `num`, repeatedly add all its digits until the result has only one digit. Return that single-digit number.

## Example 1

**Input:**
num = 38

**Output:**
2


**Explanation:**

* 3 + 8 = 11
* 1 + 1 = 2

Therefore, the answer is `2`.

## Example 2

**Input:**

num = 0


**Output:**
0


## Approach

1. Use a `while` loop to repeat until `num` becomes a single digit.
2. Initialize `sum = 0` for each round.
3. Extract the last digit using `% 10`.
4. Add the digit to `sum`.
5. Remove the last digit using integer division by `10`.
6. Store the digit sum in `num` and repeat.
7. Return `num` when it becomes a single digit.

## Complexity Analysis

* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

## Solutions

* Python: solution.py
* Java: solution.java

## LeetCode

[Add Digits — LeetCode 258](https://leetcode.com/problems/add-digits/)
