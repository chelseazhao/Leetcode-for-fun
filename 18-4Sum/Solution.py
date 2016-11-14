class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = set()
        length = len(nums)
        if length < 4:
            return []
        dicts = {}
        nums.sort()
        for i in range(length):
            for j in range(i + 1, length):
                sums = nums[i] + nums[j]
                if sums not in dicts.keys():
                    dicts[sums] = [(i, j)]
                else:
                    dicts[sums].append((i, j))
        for i in range(length):
            for j in range(i + 1, length - 2):
                minus = target - nums[i] - nums[j]
                if minus in dicts:
                    for k in dicts[minus]:
                        if res1 > j:
                            result.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in result]
