# LeetCode 1390 — Four Divisors
**Topics:** Array, Math, Number Theory
**Language:** Python

## Problem Description

Given an integer array `nums`, return the sum of divisors of the integers in the array that have exactly four positive divisors.

If no such integer exists, return 0.

## Examples

**Example 1**
Input:
nums = [21, 4, 7]

Output:
32

Explanation:
* 21 has four divisors: `1, 3, 7, 21`. Their sum is 32.
* 4 has three divisors: `1, 2, 4`.
* 7 has two divisors: `1, 7`.
Only 21 has exactly four divisors, so the answer is 32.

**Example 2**
Input:
nums = [21, 21]
Output:
64

Explanation:
Each occurrence of 21 contributes 32. Therefore, the total is 32 + 32 = 64.

## Approach
1. Initialize the final sum to 0.
2. Iterate through each number in the array.
3. Initialize a divisor count and a sum for the current number.
4. Check possible divisors up to the square root of the number.
5. When a divisor is found, count it and add it to the sum.
6. Find the corresponding divisor using integer division and count it separately if it is different.
7. Stop checking a number when its divisor count exceeds four.
8. If the number has exactly four divisors, add their sum to the final result.
9. Return the final sum.

## Complexity Analysis
Let `m` be the length of the array and `M` be its largest element.
* **Time Complexity:** O(m√M)
* **Space Complexity:** O(1), excluding the input array.

## Key Concepts Learned
* Array traversal
* Divisor counting
* Divisor pairs
* Square-root optimization
* Early termination using `break`
* Conditional summation
