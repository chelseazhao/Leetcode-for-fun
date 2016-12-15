class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.doSum([], array, k, n)
        return self.result
    def doSum(self, curr, array, k, n):
        if len(curr) == k and n == 0:
            self.result.append(curr)
        elif n < 0 and len(curr) > k:
            return
        else:
            for i in range(len(array)):
                self.doSum(curr+[array[i]], array[i+1:], k, n - array[i])
