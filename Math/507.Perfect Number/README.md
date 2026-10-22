# LeetCode 507 — Perfect Number
Topics: Math, Number Theory
Language: Python

## Problem Description
A perfect number is a positive integer that equals the sum of its positive divisors, excluding the number itself.
Given an integer `num`, return `true` if it is a perfect number; otherwise, return `false`.

## Examples

**Example 1**

Input:
num = 28

Output:
true


Explanation:
The proper divisors of 28 are `1, 2, 4, 7, 14`.
Their sum is `1 + 2 + 4 + 7 + 14 = 28`.
Therefore, 28 is a perfect number.
**Example 2**
Input:
num = 7
Output:
false
Explanation:
The only proper divisor of 7 is 1. Since the sum is not equal to 7, it is not a perfect number.

## Approach
1. Return `False` if the number is less than or equal to 1.
2. Initialize the sum of proper divisors to 1.
3. Check possible divisors from 2 up to the square root of the number.
4. If a divisor is found, add it and its corresponding divisor to the sum.
5. Avoid counting the same divisor twice when both divisors are equal.
6. Compare the sum with the original number.

## Complexity Analysis
* **Time Complexity:** O(√n)
* **Space Complexity:** O(1)

## Key Concepts Learned
* Finding proper divisors
* Using the modulo operator (`%`)
* Optimizing loops using the square root
* Finding divisor pairs
* Time and space complexity analysis
