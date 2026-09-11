# Unique 3-Digit Even Numbers

## Problem

Given an array `digits`, find the number of **distinct three-digit even numbers** that can be formed using the given digits.
Each copy of a digit can be used only once in a number, and the number cannot start with `0`.

Example:
Input:
[1, 2, 3, 4]

Output:
12

## Approach

I use three nested loops to choose the three digits of the number:
First loop chooses the hundreds digit.
Second loop chooses the tens digit.
Third loop chooses the units digit.

For every combination, I check three conditions:
The same index cannot be used more than once.
The first digit cannot be 0.
The last digit must be even.

After forming a valid three-digit number, I store it in a HashSet so that duplicate numbers are counted only once.
Choose 3 digits
      ↓
Check valid conditions
      ↓
Form the number
      ↓
Store in Set
      ↓
Return number of unique values

## Complexity
Time Complexity: O(n³) — three loops are used to choose the three digits.
Space Complexity: O(1) — the set can contain at most 900 possible three-digit numbers.

## Key Idea
Generate → Validate → Store unique numbers → Count
