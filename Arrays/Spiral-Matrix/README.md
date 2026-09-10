# Spiral Matrix

## Problem
Given a matrix, return all the elements of the matrix in **clockwise spiral order**.
For example:
Input:

[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

The spiral order is:

[1, 2, 3, 6, 9, 8, 7, 4, 5]

## Understanding the Problem

The main idea is to traverse the matrix layer by layer in a clockwise direction.

For every layer, I need to follow these four directions:

1. Move from **left to right** across the top row.
2. Move from **top to bottom** along the right column.
3. Move from **right to left** across the bottom row.
4. Move from **bottom to top** along the left column.

After completing one layer, I move the boundaries inward and repeat the same process for the remaining inner matrix.

---

## Approach

I use four boundaries to traverse the matrix layer by layer:

- `t` → top
- `b` → bottom
- `l` → left
- `r` → right

The traversal is done in clockwise order:
→ Top row
↓ Right column
← Bottom row
↑ Left column

After traversing each side, I move that boundary inward.
t += 1
r -= 1
b -= 1
l += 1

I also check the boundaries before traversing the bottom row and left column to avoid adding elements twice.

Matrix Indexing
In Python:
mat[row][column]
So:
mat[t][i]  # Top: row fixed
mat[i][r]  # Right: column fixed
mat[b][i]  # Bottom: row fixed
mat[i][l]  # Left: column fixed

## Complexity
Time: O(m × n) — every element is visited once.
Space: O(m × n) — for storing the result.

Key Idea:
Top → Right → Bottom → Left → shrink boundaries → repeat.