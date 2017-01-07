class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.calculate(candidates, target, result, [])
        return result

    def calculate(self, nums, target, result, path):
        if target == 0:
            result.append(path)
            return
        for i in range(0, len(nums)):
            if nums[i] > target:
                break
            self.calculate(nums[i:], target-nums[i], result, path+[nums[i]])