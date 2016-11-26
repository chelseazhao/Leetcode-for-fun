class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        index = len(nums) - 2
        # find out the last wrong order
        while index >= 0 and nums[index] >= nums[index + 1]:
            index -= 1
        # swap
        if index >= 0:
            i = index + 1
            while i < len(nums) and nums[i] > nums[index]:
                i += 1
            nums[i - 1], nums[index] = nums[index], nums[i - 1]
        # reverse
        left, right = index + 1, len(nums) - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
