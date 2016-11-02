137 Single Number II

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 

思路1：数学方法，将nums转存入set，则set中每个数字只出现一次，原数组中出现一次的数字=(sum(set) * 3 - sum(nums)) / 2
思路2：位运算，当num第一次出现时，因为ones和twos都初始化为0，所以很显然运行这两行代码后ones=num，twos=0。在此之后如果num不再出现，那么很显然这就是只出现一次的数字，ones即为最终结果，如果它第二次出现，ones将会被清零，而twos则会储存下num的值。当其第三次出现时，ones和twos都会被清零，就像从未出现过该数字一样。