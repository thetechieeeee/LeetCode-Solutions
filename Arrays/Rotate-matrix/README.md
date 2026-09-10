# Rotate Matrix 90 Degrees Clockwise

## Problem
Given an `n x n` matrix, rotate the matrix by 90 degrees clockwise.
The rotation should be done **in-place**, without using another matrix.

Example:
Input:
1 2 3
4 5 6
7 8 9

Output:
7 4 1
8 5 2
9 6 3

## Approach
A 90-degree clockwise rotation can be done in two steps:
Transpose the matrix.
Reverse every row.

Step 1: Transpose
Transpose means swapping:
matrix[i][j] ↔ matrix[j][i]

For example:

1 2 3        1 4 7
4 5 6   →    2 5 8
7 8 9        3 6 9
Only the elements above the main diagonal are swapped to avoid swapping the same elements twice.

Step 2: Reverse Each Row
After transposing:
1 4 7
2 5 8
3 6 9

Reverse every row:
7 4 1
8 5 2
9 6 3

This gives the matrix rotated by 90 degrees clockwise.
## Complexity
Time Complexity: O(n²) because every element is processed.
Space Complexity: O(1) because the rotation is done in-place.

## Key Idea
90° Clockwise Rotation
        ↓
Transpose
        ↓
Reverse Every Row
The main thing to remember is:
Transpose + Reverse Rows = 90° Clockwise Rotation