18 4Sum

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

思路：将四个数的和拆成两组两个数的和，复杂度O(n^2)。对S排序，遍历S，新建dict，key是S中两个数的和，value是两个数的位置元组。重新遍历S，判断Target - nums[i] - nums[j]是否在dict中。