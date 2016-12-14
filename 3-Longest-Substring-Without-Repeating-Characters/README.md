3 Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

思路：两个指针，一个指针head指示当前子串起始位置，用dict存储字母在当前子串中出现的位置，如果出现重复字符，如果重复字符以前存储的位置在head前，更新为当前位置，否则将head移到当前位置后再更新dict存储。每次更新当前子串长度。