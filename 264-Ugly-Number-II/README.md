264 Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number. 

思路：求第n个质因数只有2, 3, 5的Ugly Number。Ugly Number必定由较小的Ugly Nuber与2,3,5相乘得到。用堆存储数字和质因数，用到heapq模块。第n个Ugly Number等于当前堆的最小值，弹出并压入其和小于等于自己的factor的factor的乘积