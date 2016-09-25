class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            result = result + 1
            n = n & (n - 1)
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.hammingWeight(11)
