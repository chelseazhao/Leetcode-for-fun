class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0 or len(s) == 1:
            return 0
        longest = [0 for i in range(len(s))]
        curLongest = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    longest[i] = longest[i - 2] + 2
                elif i - longest[i - 1] - 1 >= 0 and s[i - longest[i - 1] - 1] == '(':
                    if longest[i - 1] > 0:
                        longest[i] = longest[i - 1] + 2 + longest[i - longest[i - 1] - 2]
                    else:
                        longest[i] = 0
                curLongest = max(curLongest, longest[i])
        return curLongest
