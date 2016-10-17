class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        length = len(nums)
        self.dp = []
        if length >= 1:
            self.dp.append(nums[0])
        if length > 1:
            for i in range(1, length):
                self.dp.append(self.dp[i-1] + self.nums[i])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j] - self.dp[i] + self.nums[i]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
