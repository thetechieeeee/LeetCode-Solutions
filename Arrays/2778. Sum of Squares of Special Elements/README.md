# 2778. Sum of Squares of Special Elements

## Problem
Calculate the sum of squares of all special elements in an array.

An element is special if its 1-based index divides the array length.

## Approach
1. Find the length of the array.
2. Iterate through indices from 1 to n.
3. Check whether n is divisible by the current index.
4. If divisible, add the square of the corresponding element to the sum.
5. Return the final sum.

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## Language
Python