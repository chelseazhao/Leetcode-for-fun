72 Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

思路：动态规划，dis(i, j)表示word1中第i个和word2中第j个的编辑距离
    if i == 0 and j > 0，dis(i, j) = j
    if i > 0 and j == 0，dis(i, j) = i
    if 0 < i ≤ 1  且 0 < j ≤ 1 ，dis(i, j) == min{ dis(i-1, j) + 1, dis(i, j-1) + 1, dis(i-1, j-1) + f(i, j) }，当第一个字符串的第i个字符不等于第二个字符串的第j个字符时，f(i, j) = 1；否则，f(i, j) = 0。
