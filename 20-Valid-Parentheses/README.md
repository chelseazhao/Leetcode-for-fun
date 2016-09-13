20 Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

思路：用栈来存储列表，如果是左半个括号，入栈；如果是右半个括号，将栈顶元素pop出栈，判断是否匹配，如果不匹配，返回False。最终如果栈为空，返回True，否则返回False。判断是否匹配使用字典存储每一对。