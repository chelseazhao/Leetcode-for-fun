# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
        	return 0
        llevel = 1
        rlevel = 1
        left = root.left
        while left:
        	left = left.left
        	llevel += 1
        right = root.right
        while right:
        	right = right.right
        	rlevel += 1
        if llevel == rlevel:
        	return (2 << (llevel - 1)) - 1
        else:
        	return self.countNodes(root.left) + self.countNodes(root.right) + 1
