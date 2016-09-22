189 Rotate Array
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]

思路一 将数组元素循环向右平移k个单位
思路二 先将整个数组翻转，再分别翻转前k个和后n-k个