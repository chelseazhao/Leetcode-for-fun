class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s.isalpha():
            return s
        stack = []
        stack.append(["", 1])
        num = ""
        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i]
            elif s[i] == '[':
                stack.append(["", int(num)])
            elif s[i] == ']':
                string, iternum = stack.pop()
                stack[-1][0] += string * iternum
            else:
                stack[-1][0] += s[i]
        return stack[0][0]

    
if __name__ == 'main':
    sol = Solution()
    sol.decodeString("3[a]")
