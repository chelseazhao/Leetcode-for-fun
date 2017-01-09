class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        operation = ['+', '-', '(']
        operation_stack = [1, 1]
        i = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                result += operation_stack.pop() * int(s[start:i])
                continue
            if ch in operation:
                operation_stack += operation_stack[-1] * (1, -1)[ch == '-'],
            elif ch == ')':
                operation_stack.pop()
            i += 1
        return result