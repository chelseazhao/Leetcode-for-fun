43 Multiply Strings

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:

    The numbers can be arbitrarily large and are non-negative.
    Converting the input string to integer is NOT allowed.
    You should NOT use internal library such as BigInteger.

思路：先逐位存储两个乘数各位乘积的和，然后再转化为十进制