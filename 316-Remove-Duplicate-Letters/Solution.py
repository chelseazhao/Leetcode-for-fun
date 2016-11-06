class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        visit = [False] * 26
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - 97] += 1
        for i in range(len(s)):
            index = ord(s[i]) - 97
            count[index] -= 1
            if visit[index]:
                continue
            else:
                while res and res[-1] > s[i] and count[ord(res[-1]) - 97]:
                    visit[ord(res.pop()) - 97] = False
                res.append(s[i])
                visit[index] = True
        return "".join(res)


if __name__ == '__main__':
    sol = Solution()
    print sol.removeDuplicateLetters("bcabc")
