442 Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

思路：这里nums的数有3种情况：出现1次，出现2次，出现0次。
我们找出现2次的，比如element 8出现2次，那么我们按照element的值来走到下一个的时候，会有2次走到nums[8]。 标记一下，这样下次来的时候就知道了。。比如把正的换成负的，下次来的时候发现是个负数，就知道我们来过一次。当然，想赢的根据element的值来走的时候，如果是负数，要换成正数。。