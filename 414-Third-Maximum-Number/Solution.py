class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = c = None
        for num in nums:
            if num > a:
                a, b, c = num, a, b
            elif a > num > b:
                b, c = num, b
            elif b > num > c:
                c = num
        return c if c is not None else a
