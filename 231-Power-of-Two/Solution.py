class Solution(object):

    # iterate
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        while n % 2 == 0:
            n /= 2
        return n== 1

    # recursive
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n == 1|| (n % 2 == 0 && self.isPowerOfTwo(n / 2)))

    # bit operation
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and ((n & (n - 1)) == 0)

    # math derivation
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (1073741824 % n == 0)
