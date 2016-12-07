32 Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4. 

思路：一维dp。longest[i]：以s[i-1]为结尾的longest valid parentheses substring的长度。
通项公式：s[i] = '('：longest[i] = 0
s[i] = ')'：找i前一个字符的最长括号串longest[i]的前一个字符j = i-2-longest[i-1]
如果j >=0，且longest[j] = '(',longest[i] = longest[i-1] + 2 + longest[j]
如果j<0，或s[j] = ')'，longest[i] = 0