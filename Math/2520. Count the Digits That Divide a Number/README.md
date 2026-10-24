# 2520. Count the Digits That Divide a Number
**Language:** Python
**Topics:** Math, Number Manipulation

## Problem Description

Given an integer `num`, return the number of digits in `num` that divide the original number evenly.

A digit divides the number evenly if the remainder is zero when the original number is divided by that digit.

## Approach

Initially, I tried extracting the last digit and checking whether the remaining number was divisible by it. However, I needed to preserve the original number and count all the digits that satisfy the condition.

I improved the solution by using the modulo and integer division operators to process each digit individually.

### Steps Followed

1. Store the original number in a separate variable.
2. Initialize a counter to zero.
3. Use a `while` loop to process each digit.
4. Extract the last digit using `num % 10`.
5. Check whether the original number is divisible by that digit.
6. If it is divisible, increment the counter.
7. Remove the last digit using `num //= 10`.
8. Repeat until `num` becomes zero.
9. Return the final count.

## Python Solution

class Solution:
    def countDigits(self, n: int) -> int:
        original_num = n
        cnt = 0
        while n > 0:
            temp = n%10
            if original_num%temp==0:
                cnt+=1
            n//=10
        return cnt

## Example Walkthrough

### Example 1

**Input:**

num = 7


**Output:**

1


**Explanation:**

The digit 7 divides the original number 7 evenly. Therefore, the count is 1.

### Example 2

**Input:**

num = 121

**Output:**

2


**Explanation:**

* Digit 1: 121 % 1 = 0, so increment the count.
* Digit 2: 121 % 2 = 1, so the count remains unchanged.
* Digit 1: 121 % 1 = 0, so increment the count again.

The final count is 2.

## Complexity Analysis

* **Time Complexity:** O(log₁₀ n), because each iteration processes one digit.
* **Space Complexity:** O(1), because only a constant number of variables are used.

## Key Learnings

* Learned how to extract the last digit using `% 10`.
* Understood how to remove the last digit using `// 10`.
* Learned why the original number must be preserved while processing its digits.
* Practiced checking divisibility and counting values that satisfy a condition.
* Understood the importance of returning the count instead of returning an individual digit.

## LeetCode Link

[2520. Count the Digits That Divide a Number](https://leetcode.com/problems/count-the-digits-that-divide-a-number/)
