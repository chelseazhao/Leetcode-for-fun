# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getDepth(self, root):
        if root == None:
            return 0
        leftDepth = self.getDepth(root.left)
        if leftDepth == -1:
            return -1
        rightDepth = self.getDepth(root.right)
        if rightDepth == -1:
            return -1
        diffDepth = abs(leftDepth - rightDepth)
        if diffDepth > 1:
            return -1
        else:
            return max(leftDepth, rightDepth) + 1
            
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.getDepth(root) == -1:
            return False
        else:
            return True
