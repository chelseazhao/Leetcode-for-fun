class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0 or length == 1:
            return length
        head = 0
        result = 0
        cur = 0
        word_map = {}
        for i in range(length):
            if s[i] not in word_map:
                word_map[s[i]] = i
                cur += 1
            else:
                if word_map[s[i]] < head:
                    cur += 1
                    word_map[s[i]] = i
                else:
                    if cur > result:
                        result = cur
                    head = word_map[s[i]] + 1
                    word_map[s[i]] = i
                    cur = i - head + 1
        return result if result > cur else cur
