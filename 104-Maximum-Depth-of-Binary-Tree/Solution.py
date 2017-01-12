# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
        	return 0
        max_depth = 1
        cur_depth = 1
    	if root.left:
    		max_depth = max(max_depth, cur_depth + self.maxDepth(root.left))
    	if root.right:
    		max_depth = max(max_depth, cur_depth + self.maxDepth(root.right))
    	return max_depth