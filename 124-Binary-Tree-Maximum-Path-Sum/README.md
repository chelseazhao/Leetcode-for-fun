124 Binary Tree Maximum Path Sum

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3

Return 6. 

思路：利用“最大连续子序列和”的思路，用dfs来进行遍历。先算出左右子树的结果left和right，如果left大于0，那么对后续结果是有利的，result加上left，如果right大于0，对后续结果也是有利的，result继续加上right。