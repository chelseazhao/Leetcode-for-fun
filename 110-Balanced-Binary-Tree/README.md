110 Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 

思路：判断是否是平衡二叉树, 对每一个结点, 递归返回左右两个子树的高度, 如果该结点左右两子树高度差大于1, 返回-1;  若小于1, 则该结点高度为左右子树最大高度加1.