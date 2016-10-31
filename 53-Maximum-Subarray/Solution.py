import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        global_max = nums[0]
        local_max = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            local_max = max(num, local_max+num)
            global_max = max(global_max, local_max)
        return global_max
