# Search a 2D Matrix

## Problem

Given a sorted 2D matrix, determine whether a target value exists in the matrix.

## Approach

The matrix is treated as a sorted one-dimensional array and Binary Search is used to find the target efficiently.

The middle index is converted into row and column positions using:

- `row = mid // columns`
- `col = mid % columns`

## Complexity

- Time Complexity: O(log(m × n))
- Space Complexity: O(1)
