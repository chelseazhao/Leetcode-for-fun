313 Super Ugly Number

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.

思路：用最小堆同Ugly Number II会出现MLE错误。相同的思路，改用数组存储，primes[i]为第i个素数，minProduct[i]存放着以i为索引的素数为因子的最小乘积，另一个因子存放在以index[i]为索引的superNumbers中 