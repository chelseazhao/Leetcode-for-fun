class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicts = {}
        length = len(nums)
        for num in nums:
        	if num not in dicts:
        		dicts[num] = 1
        	else:
        		dicts[num] += 1
    		if dicts[num] > length / 2:
    			return num