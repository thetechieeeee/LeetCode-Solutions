# Best Time to Buy and Sell Stock

## Problem

Given an array `prices`, where `prices[i]` represents the price of a stock on the `i`th day, find the maximum profit that can be made by buying on one day and selling on a later day.
If no profit can be made, return `0`.

Example:
Input:
[7, 1, 5, 3, 6, 4]
Output:
5
The best choice is to buy at 1 and sell at 6.

##Approach:
I use a single pass through the array.

While traversing the prices:

Keep track of the minimum price seen so far.
For each price, calculate the profit by selling at the current price.
Update the maximum profit whenever a better profit is found.

Current Profit = Current Price - Minimum Price
If the current price is smaller than the minimum price, I update the minimum price.
Otherwise, I check whether selling at the current price gives a better profit.
This allows us to find the best buying and selling days without checking every possible pair.

## Complexity:
Time Complexity: O(n) — the array is traversed only once.
Space Complexity: O(1) — only a few variables are used.

## Key Idea
Track minimum price
        ↓
Calculate current profit
        ↓
Update maximum profit
        ↓
Continue through the array

One pass + minimum price tracking = maximum profit in O(n) time.