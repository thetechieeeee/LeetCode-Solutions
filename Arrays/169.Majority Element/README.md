# 169. Majority Element

## Problem Description

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `n / 2` times in the array.

You may assume that the majority element always exists in the array.

## Key Idea

The main idea is to count how many times each element appears using a hash map.

We store each number as a key and its frequency as the value. After counting all elements, we check which element appears more than `n / 2` times.

## Approach

1. Find the length of the array.
2. Create an empty dictionary `mp` to store the frequency of each number.
3. Traverse through the array:
   - If the number already exists in the dictionary, increase its count.
   - Otherwise, add it with a count of `1`.
4. Traverse through the dictionary.
5. If the frequency of an element is greater than `n / 2`, return that element.

## Example
Input:
nums = [2, 2, 1, 1, 1, 2, 2]
Output:
2
Explanation:
The number 2 appears 4 times.
Since:
4 > 7 / 2
2 is the majority element.

## Complexity
Time Complexity: O(n)
Space Complexity: O(n)