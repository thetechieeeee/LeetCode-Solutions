# 9. Palindrome Number

**Language:** Python
**Topics:** Math, Number Manipulation

## Problem Description

Given an integer `x`, return `True` if `x` is a palindrome; otherwise, return `False`.

A palindrome number reads the same from left to right and right to left.

### Examples

**Example 1**

Input: x = 121
Output: True
Explanation: 121 reads the same in both directions.


**Example 2**
Input: x = -121
Output: False
Explanation: Negative numbers are not palindromes.


**Example 3**

Input: x = 10
Output: False
Explanation: Reversed number is 01, which is 1.


## Approach

I solved this problem by reversing the given number and comparing it with the original number.

Initially, I tried adding each extracted digit directly to the reversed number. However, this only adds the digits instead of placing them in reverse order. I corrected this by multiplying the existing reversed number by 10 before adding the next digit.

### Steps Followed

1. Store the original number in a variable called `original`.
2. Initialize `rev = 0` to build the reversed number.
3. If the number is negative, return `False`.
4. Extract the last digit using `x % 10`.
5. Append the extracted digit using `rev = rev * 10 + temp`.
6. Remove the last digit using `x //= 10`.
7. Repeat until `x` becomes zero.
8. Compare the reversed number with the original number.
9. Return `True` if both are equal; otherwise, return `False`.

## Python Solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        rev = 0

        if x < 0:
            return False

        while x > 0:
            temp = x % 10
            rev = rev * 10 + temp
            x = x // 10

        return rev == original

## Example Walkthrough

### Input: x = 121

| Step | Current Number | Extracted Digit | Reversed Number |
| ---- | -------------: | --------------: | --------------: |
| 1    |            121 |               1 |               1 |
| 2    |             12 |               2 |              12 |
| 3    |              1 |               1 |             121 |

After processing all digits:

* Original number = 121
* Reversed number = 121

Since both numbers are equal, the output is `True`.

### Input: x = 10

| Step | Current Number | Extracted Digit | Reversed Number |
| ---- | -------------: | --------------: | --------------: |
| 1    |             10 |               0 |               0 |
| 2    |              1 |               1 |               1 |

The original number is 10, but the reversed number is 1.

Since they are not equal, the output is `False`.

## Complexity Analysis

* **Time Complexity:** O(log₁₀ x), because each iteration processes one digit.
* **Space Complexity:** O(1), because only a constant number of variables are used.

## Key Learnings

* Learned how to extract digits using the modulo operator (`%`).
* Understood how integer division (`//`) removes the last digit.
* Learned how to construct a reversed number using `rev * 10 + digit`.
* Understood why negative numbers are not palindromes.
* Practiced comparing the reversed number with the original number.

## LeetCode Link

[9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)
