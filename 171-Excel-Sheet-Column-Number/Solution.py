class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        length = len(s)
        res = 0
        for i in range(length):
            res += (ord(s[i]) - 64) * 26 ** (length - i - 1)
        return res
