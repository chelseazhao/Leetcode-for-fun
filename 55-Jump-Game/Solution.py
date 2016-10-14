class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        length = len(nums)
        max_step = nums[0]
        start = 0
        while start < length and start <= max_step:
            if max_step >= length - 1:
                return True
            next_max = 0
            for i in range(start, max_step + 1):
                if start == max_step:
                    return False
                if i + nums[i] >= next_max:
                    next_max = i + nums[i]
                    start = i
            max_step = next_max
        return False
