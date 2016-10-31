53 Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6. 

思路：动态规划问题，假设我们已知第i步的global_max[i]和local_max[i]，那么第i+1步的表达式：
local_max[i+1]=max(nums[i], local_max[i]+nums[i])，就是局部最优是一定要包含当前元素，所以不然就是local[i]+nums[i],但是如果local_max[i]<0, 就直接用nums[i]；
global_max[i+1]=max(local_max[i+1],global_max[i])，有了当前一步的局部最优，那么全局最优就是当前的局部最优或者还是原来的全局最优（所有情况都会被涵盖进来，因为最优的解如果不包含当前元素，那么前面会被维护在全局最优里面，如果包含当前元素，那么就是这个局部最优）。