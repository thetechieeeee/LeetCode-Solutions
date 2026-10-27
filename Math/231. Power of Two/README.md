# 231. Power of Two

**Topics:** Math, Bit Manipulation
**Languages:** Python, Java

## Problem Description

Given an integer `n`, return `true` if it is a power of two. Otherwise, return `false`.

A number is a power of two if it can be expressed as `2^x`, where `x` is a non-negative integer.

## Example 1

**Input:** `n = 16`

**Output:** `true`

**Explanation:** `16 = 2^4`

## Example 2

**Input:** `n = 3`

**Output:** `false`

**Explanation:** 3 cannot be expressed as a power of two.

## Example 3

**Input:** `n = 1`

**Output:** `true`

**Explanation:** `1 = 2^0`

## Approach

1. If `n` is less than or equal to zero, return `false`.
2. While `n` is divisible by 2, divide it by 2.
3. After the loop, check whether `n` equals 1.
4. If `n == 1`, return `true`; otherwise, return `false`.

## Complexity Analysis

* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

## Solutions

* Python: `solution.py`
* Java: `Solution.java`

## LeetCode

[Power of Two — LeetCode 231](https://leetcode.com/problems/power-of-two/)
