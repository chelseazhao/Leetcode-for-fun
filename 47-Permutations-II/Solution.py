class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.solve(nums, 0)
        return self.result
    def solve(self, nums, i):
        n = len(nums)
        if i == n:
            self.result.append(list(nums))
            return
        exist_dict = {}
        for j in range(i, n):
            if nums[j] in exist_dict.keys():
                continue
            exist_dict[nums[j]] = 1
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            self.solve(nums, i + 1)
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
