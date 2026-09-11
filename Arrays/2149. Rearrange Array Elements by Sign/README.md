# 2149. Rearrange Array Elements by Sign

## Problem Description

Given an integer array `nums` of even length containing an equal number of positive and negative integers, rearrange the elements so that:

- Every consecutive pair has opposite signs.
- The relative order of positive integers is preserved.
- The relative order of negative integers is preserved.
- The rearranged array starts with a positive integer.

## Approach
We create a new array of the same size and use two pointers:

- `p_ind` → keeps track of the next position for a positive number.
- `n_ind` → keeps track of the next position for a negative number.

While traversing the original array:
- If the number is positive, place it at `p_ind` and move `p_ind` by 2.
- If the number is negative, place it at `n_ind` and move `n_ind` by 2.

This ensures that positive and negative numbers are automatically placed at alternating positions while maintaining their original order.

## Example

Input:
nums = [3, 1, -2, -5, 2, -4]
Output:
[3, -2, 1, -5, 2, -4]

## Complexity:
Time Complexity: O(n)
Space Complexity: O(n)

## Key Idea:
The main idea is to maintain two separate positions for positive and negative numbers:
- Positive numbers are placed at even indices: `0, 2, 4, ...`
- Negative numbers are placed at odd indices: `1, 3, 5, ...`
We traverse the original array only once. Whenever we find a positive number, we place it in the next available even position. Similarly, negative numbers are placed in the next available odd position.
By increasing each pointer by `2`, we automatically maintain the required alternating pattern and preserve the relative order of numbers with the same sign.