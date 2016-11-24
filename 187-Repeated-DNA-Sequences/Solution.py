class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()
        sets = set()
        for i in range(len(s) - 9):
            substring = s[i:i+10]
            if substring  not in sets:
                sets.add(substring)
            else:
                res.add(substring)
        return list(res)
