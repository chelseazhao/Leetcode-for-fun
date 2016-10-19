38 Count and Say

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence. 

思路：认真读题！题意是迭代生成字符串：后一个字符串是前一个字符串每个连续出现的数字的个数＋该数字拼凑而成，用count记录连续数字的个数，然后用key记录当前最新的数字，每次遇到不同的数字就把count+key拼接到结果当中，但如果最后一位和上一位相同则无法加入，所以先在字符串末尾加'#'，这样能保证计算到最后一位。