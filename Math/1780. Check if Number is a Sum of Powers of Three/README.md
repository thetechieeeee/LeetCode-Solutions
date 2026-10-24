# 1780. Check if Number is a Sum of Powers of Three
**Language:** Python
**Topics:** Math, Number Theory

## Problem Description

Given an integer `n`, check whether it can be represented as the sum of distinct powers of three. Return `True` if possible; otherwise, return `False`.

### Examples

**Example 1**

Input: n = 12
Output: True
Explanation: 12 = 3¹ + 3² = 3 + 9

**Example 2**
Input: n = 21
Output: False


## Approach

Initially, I tried solving the problem using a loop and checking divisibility by 3. However, my first approach returned the result too early and did not check the entire number, which caused wrong answers.

After understanding the problem, I used the base-3 representation of a number to develop the correct approach.

### Steps Followed

1. Start with the given number `n`.
2. Find the remainder using `n % 3`.
3. If the remainder is `2`, return `False`, because the number cannot be represented as a sum of distinct powers of three.
4. Otherwise, divide the number by 3 using integer division: `n //= 3`.
5. Repeat the process until `n` becomes zero.
6. If no remainder equals `2`, return `True`.

## Python Solution
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

## Example Walkthrough

### Input: n = 12

| Step |  n | n % 3 | n // 3 |
| ---- | -: | ----: | -----: |
| 1    | 12 |     0 |      4 |
| 2    |  4 |     1 |      1 |
| 3    |  1 |     1 |      0 |

The number becomes zero without producing a remainder of `2`. Therefore, the output is `True`.

### Input: n = 21

| Step |  n | n % 3 | n // 3 |
| ---- | -: | ----: | -----: |
| 1    | 21 |     0 |      7 |
| 2    |  7 |     1 |      2 |
| 3    |  2 |     2 |      — |

The remainder is `2`, so the function immediately returns `False`.

## Complexity Analysis

* **Time Complexity:** O(log₃ n), because the number is divided by 3 in every iteration.
* **Space Complexity:** O(1), because the algorithm uses only a constant amount of extra space.

## Key Learnings

* Understood the difference between the modulo (`%`) and integer division (`//`) operators.
* Learned how repeated division by 3 reveals the base-3 representation of a number.
* Understood why a remainder of `2` makes the representation invalid.
* Learned to avoid returning a result before checking all necessary conditions.

## LeetCode Link

[Check if Number is a Sum of Powers of Three — Problem 1780](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/)
