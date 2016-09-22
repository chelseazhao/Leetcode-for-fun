class Solution(object):
    def reverse(self, nums, start, end):
        if start >= end:
            return
        stop = int((start + end) / 2)
        for i in range(start, stop):
            temp = nums[i]
            nums[i] = nums[start + end - 1 - i]
            nums[start + end - 1 - i] = temp
            
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n)
        self.reverse(nums, 0, k)
        self.reverse(nums, k, n)
