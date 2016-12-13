47 Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

思路：递归，对每个位置上的数字，将它和它后面的数字依次调换位置。用dict判断新的排列是否出现过。