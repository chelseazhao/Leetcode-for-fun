class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.size = len(nums)
        size = len(nums)
        h = int(math.ceil(math.log(size, 2))) if size else 0
        maxSize = 2 ** (h + 1) - 1 
        self.stree = [0 for i in range(maxSize)]
        if size:
            self.initST(0, size - 1, 0)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if i < 0 or i >= self.size:
            return
        diff = val - self.nums[i]
        self.nums[i] = val
        self.updateST(0, self.size - 1, i, diff, 0)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0 or j < 0 or i >= self.size or j >= self.size:
            return 0
        return self.sumRangeST(0, self.size - 1, i, j, 0)


    def initST(self, start, end, index):
        if start == end:
            self.stree[index] = self.nums[start]
        else:
            mid = (start + end) / 2
            self.stree[index] = self.initST(start, mid, index * 2 + 1) + self.initST(mid + 1, end, index * 2 + 2)
        return self.stree[index] 


    def updateST(self, start, end, i, diff, index):
        if i < start or i > end:
            return
        self.stree[index] += diff
        if start != end:
            mid = (start + end) / 2
            self.updateST(start, mid, i, diff, index * 2 + 1)
            self.updateST(mid + 1, end, i, diff, index * 2 + 2)

    def sumRangeST(self, start, end, left, right, index):
        if left <= start and right >= end:
            return self.stree[index]
        if end < left or start > right:
            return 0
        mid = (start + end) / 2
        return self.sumRangeST(start, mid, left, right, index * 2 + 1) + self.sumRangeST(mid + 1, end, left, right, index * 2 + 2)
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
