class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.calculate(candidates, target, result, 0, [])
        return result

    def calculate(self, nums, target, result, num, path):
        if target == 0:
            result.append(path)
            return
        for i in range(num, len(nums)):
            if nums[num] > target:
                break
            if i > num and nums[i - 1] == nums[i]:
                continue
            self.calculate(nums, target-nums[i], result, i+1, path+[nums[i]])