55 Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false. 

思路：贪心算法，每次走起点可走范围内的最大值直到到达末尾。如果可走范围内无法超过起点最大值，则无法到达终点。