class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        if l1 != l2 or sorted(s1) != sorted(s2):
            return False
        if l1 < 4 or s1 == s2:
            return True
        for i in range(1, l1):
            if (self.isScramble(s1[i:], s2[i:]) and self.isScramble(s1[:i], s2[:i])) or (self.isScramble(s1[i:], s2[:-i]) and self.isScramble(s1[:i], s2[-i:])):
                return True
        return False
