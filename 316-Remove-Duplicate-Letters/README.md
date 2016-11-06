316 Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:

Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb" 

思路：求无重复字符串的字典序最小的子串。先储存每个字母的出现次数。然后对字符串进行扫描，判断每个字母是否在栈中，若在，count-1; 若不在，和栈顶元素比较，如果比栈顶字母小且栈顶字母count不为0，则将栈顶元素出栈，该元素入栈。