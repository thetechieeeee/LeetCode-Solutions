# 1394. Find Lucky Integer in an Array

## Problem
Given an array of integers, a lucky integer is an integer whose frequency in the array is equal to its value.

Return the largest lucky integer in the array. If no lucky integer exists, return -1.

## Approach
1. Count the frequency of each number in the array.
2. Check the numbers in descending order, starting from the maximum possible value.
3. If a number's frequency equals the number itself, return it.
4. If no lucky integer is found, return -1.

## Example

**Input:** arr = [2, 2, 3, 4]

**Output:** 2

**Explanation:** The number 2 appears exactly twice, so it is a lucky integer.

## Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Languages
- Python
- Java