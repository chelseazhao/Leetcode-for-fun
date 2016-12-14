152 Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6. 

思路：维护两个数组，一个是当前最大值，一个是当前最小值。转移方程：
max_copy[i] = max_local[i]
max_local[i + 1] = Max(Max(max_local[i] * nums[i], nums[i]),  min_local * nums[i])
min_local[i + 1] = Min(Min(max_copy[i] * nums[i], nums[i]),  min_local * nums[i])