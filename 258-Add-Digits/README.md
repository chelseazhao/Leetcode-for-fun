258 Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

思路：找规律1->1, 2->2, ... 9->9, 10->1, ...每9个数一循环(num - 1) % 9 + 1 