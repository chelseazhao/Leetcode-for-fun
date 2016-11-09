222 Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

思路：如果直接递归会超时。则递归时先判断是不是complete binary tree，如果是，用公式算出节点数，否则再递归计算左右子树节点数。