# LeetCode 2427 — Number of Common Factors
**Topics:** Math, Number Theory
**Language:** Python

## Problem Description
Given two positive integers `a` and `b`, return the number of common factors of the two integers.
An integer is a common factor if it divides both numbers exactly.

## Examples
**Example 1**
Input:
a = 12, b = 6
Output:
4

Explanation:
The common factors of 12 and 6 are `1, 2, 3, 6`.
There are four common factors.

**Example 2**
Input:
a = 25, b = 30
Output:
2

Explanation:
The common factors are `1` and `5`.
Therefore, the answer is 2.

## Approach
1. Calculate the Greatest Common Divisor (GCD) of `a` and `b`.
2. Initialize a counter to 0.
3. Iterate from 1 to the GCD, inclusive.
4. Check whether each number divides the GCD exactly.
5. Increment the counter whenever a factor is found.
6. Return the counter.
Every common factor of two positive integers is a factor of their GCD. Therefore, counting the factors of the GCD gives the number of common factors.

## Complexity Analysis
Let `g = gcd(a, b)`.
* **Time Complexity:** O(log(min(a, b)) + g), including the GCD calculation.
* **Space Complexity:** O(1), excluding the input.

## Key Concepts Learned
* Greatest Common Divisor (GCD)
* Python's `math.gcd()` function
* Finding common factors
* Modulo operator (`%`)
* Counting factors
