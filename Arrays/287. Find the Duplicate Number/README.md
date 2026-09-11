# 287. Find the Duplicate Number

## Problem Description

Given an integer array `nums` containing `n + 1` integers where each integer is in the range `[1, n]`, there is exactly one repeated number.

The task is to find and return the repeated number.

The array should not be modified.

## Key Idea

The main idea is to keep track of how many times each number appears.

We create a frequency array `f` of size `n + 1`:

- Initially, all values in `f` are `0`.
- For every number in `nums`, increase its corresponding frequency.
- If a number is encountered again, its frequency will already be greater than `0`.
- That number is the duplicate, so we return it immediately.

## Approach

1. Find the length of the array `n`.
2. Create a frequency array `f` of size `n + 1`.
3. Traverse through every element in `nums`.
4. Check whether the current number has already appeared:
   - If `f[nums[i]] == 0`, increase its frequency.
   - Otherwise, the number is repeated, so return `nums[i]`.
5. If no duplicate is found during the traversal, return `0`.

## Example

Input:
nums = [1, 3, 4, 2, 2]
Output:
2
Explanation:
The numbers are:
1 → first occurrence
3 → first occurrence
4 → first occurrence
2 → first occurrence
2 → already appeared
Therefore, the duplicate number is 2.

## Complexity
Time Complexity: O(n)
Space Complexity: O(n)