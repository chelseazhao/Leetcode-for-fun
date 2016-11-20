class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_int = {}
        roman_int['I'] = 1
        roman_int['V'] = 5
        roman_int['X'] = 10
        roman_int['L'] = 50
        roman_int['C'] = 100
        roman_int['D'] = 500
        roman_int['M'] = 1000
        res = 0
        for i in range(len(s) - 1):
            now = s[i]
            next = s[i + 1]
            if roman_int[now] < roman_int[next]:
                res = res - roman_int[now]
            else:
                res = res + roman_int[now]
        res = res + roman_int[s[len(s) - 1]]
        return res
