# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        lmin = self.minDepth(root.left)
        rmin = self.minDepth(root.right)
        if lmin == 0 and rmin == 0:
            return 1
        if lmin == 0:
            lmin = sys.maxint
        if rmin == 0:
            rmin = sys.maxint
        return min(lmin, rmin) + 1
