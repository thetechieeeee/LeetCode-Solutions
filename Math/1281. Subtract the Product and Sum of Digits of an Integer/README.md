# 1281. Subtract the Product and Sum of Digits of an Integer

**Topics:** Math, Programming
**Languages:** Python, Java

## Problem Description

Given an integer `n`, return the difference between the product of its digits and the sum of its digits.

## Example 1

**Input:**
n = 234
**Output:**
15


**Explanation:**

* Product of digits = 2 × 3 × 4 = 24
* Sum of digits = 2 + 3 + 4 = 9
* Difference = 24 - 9 = 15

## Example 2

**Input:**
n = 4421


**Output:**
21

**Explanation:**

* Product of digits = 4 × 4 × 2 × 1 = 32
* Sum of digits = 4 + 4 + 2 + 1 = 11
* Difference = 32 - 11 = 21

## Approach

1. Initialize `sum = 0` and `product = 1`.
2. Extract the last digit using `% 10`.
3. Add the digit to `sum`.
4. Multiply the digit with `product`.
5. Remove the last digit using integer division by `10`.
6. Repeat until the number becomes `0`.
7. Return `product - sum`.

## Complexity Analysis

* **Time Complexity:** O(log n) — Each iteration processes one digit.
* **Space Complexity:** O(1) — Only a constant amount of extra space is used.

## Solutions

* Python: solution.py
* Java: solution.java
## LeetCode

[Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)
