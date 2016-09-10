235 Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).” 
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

思路：找到平衡二叉树中两个结点最近的共同祖先。如果找一棵普通的树的两个结点的共同祖先，可以分别遍历二叉树，将到达两个结点的路径存储在列表中，比较两个列表，最后一个相同的结点即为所求。本题是平衡二叉树可以简化，从根节点开始遍历，如果两个结点的值均小于当前结点的值，结果必定在当前结点的左子树；如果两个结点的值均大于当前结点的值，结果必定在当前结点的右子树；否则，结果为当前结点。