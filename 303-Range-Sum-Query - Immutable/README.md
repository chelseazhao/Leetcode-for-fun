303 Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

    You may assume that the array does not change.
    There are many calls to sumRange function.

思路：动态规划，先求出[0, i](i >= 1 and i < length)的和的数组，sum[i, j] = dp[j] - dp[i] + nums[i]