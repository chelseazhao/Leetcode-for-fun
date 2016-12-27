class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums)
        if target % 2 == 1:
            return False
        dp = [True] + [False for i in range(target / 2 + 1)]
        for i in range(len(nums)):
            for j in range(target / 2, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[target / 2]
