30 Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter). 

思路：将words存入dict，每length个字母遍历s，建立临时dict存储本次遍历，便于中间提前终止，比较本次遍历符合条件的单词数和words中单词数目是否相等。