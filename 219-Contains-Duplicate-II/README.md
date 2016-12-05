219 Contains Duplicate II
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

思路：用dict存每个数字最后出现的位置，如果不符合要求，更新dict。trick: not in map的速度更快 