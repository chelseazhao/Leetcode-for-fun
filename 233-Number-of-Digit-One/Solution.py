class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        result = 0
        m = 1
        while m <= n:
            result += (n / m + 8) / 10 * m + (n / m % 10 == 1) * (n % m + 1)
            m *= 10
        return result
            
