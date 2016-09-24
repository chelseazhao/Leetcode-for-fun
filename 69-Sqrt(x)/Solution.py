class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        left = 0
        right = x
        res = right / 2
        while left < right - 1:
            if res * res < x:
                left = res
                res = (left + right) / 2
            elif res * res > x:
                right = res
                res = (left + right) / 2
            else:
                return res
        return res
if __name__ == "__main__":
    sol = Solution()
    print sol.mySqrt(209)
