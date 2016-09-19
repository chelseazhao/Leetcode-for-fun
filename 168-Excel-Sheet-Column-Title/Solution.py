class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n > 0:
            result = result + chr(65 + (n - 1) % 26)
            n = (n - 1) / 26
        return result[::-1]
