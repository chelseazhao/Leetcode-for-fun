class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_map = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in nums_map:
                nums_map[num] = i
            else:
                if i - nums_map[num] <= k:
                    return True
                nums_map[num] = i
        return False
