416 Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

思路：动态规划。求一个数组是否能分成两个相等子集可转化成是否存在一个和是sum / 2的子集。dp[j]表示是否存在和为j的子集，dp[j] = dp[j] or dp[j - nums[i]], j <= sum / 2 and j >= nums[i]，最后返回dp[sum / 2]