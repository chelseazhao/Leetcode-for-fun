378. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.


思路：矩阵每一行每一列分别是有序的，则可以确定左上角、右上角分别是矩阵中所有数字的最小值和最大值。使用二分查找的思路，不断用start和end的mid来更新左右两端：如果mid的次序小于k，则更新左端；否则，更新右端，直到找到最终相邻次序的两个数字。