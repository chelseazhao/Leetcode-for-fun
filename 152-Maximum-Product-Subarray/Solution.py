class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        max_local = nums[0]
        min_local = nums[0]
        max_global = nums[0]
        for i in range(1, length):
            tmp = max_local
            max_local = max(max(nums[i], nums[i] * max_local), nums[i] * min_local)
            min_local = min(min(nums[i], nums[i] * tmp), nums[i] * min_local)
            max_global = max(max_global, max_local)
        return max_global
