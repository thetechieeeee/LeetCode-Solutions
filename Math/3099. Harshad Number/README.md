# 3099. Harshad Number
**Topic:** Math
**Language:** Python

## Problem Description

An integer is called a Harshad number if it is divisible by the sum of its digits.

Given an integer `x`, return the sum of its digits if `x` is a Harshad number. Otherwise, return `-1`.

## Example 1

**Input:**

x = 18


**Output:**
9


**Explanation:**

The sum of the digits is `1 + 8 = 9`. Since `18` is divisible by `9`, it is a Harshad number. Therefore, return `9`.

## Example 2

**Input:**

x = 23


**Output:**

-1


**Explanation:**

The sum of the digits is `2 + 3 = 5`. Since `23` is not divisible by `5`, it is not a Harshad number. Therefore, return `-1`.

## Approach

1. Calculate the sum of the digits of the given number.
2. Check whether the number is divisible by the sum of its digits.
3. If divisible, return the digit sum.
4. Otherwise, return `-1`.

## Complexity Analysis

* **Time Complexity:** O(log x), where x is the given number.
* **Space Complexity:** O(1), using a constant amount of extra space.

## LeetCode Link

[3099. Harshad Number](https://leetcode.com/problems/harshad-number/)
