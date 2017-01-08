# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = 0
    def getAnswer(self, root):
        if not root:
            return 0
        left = self.getAnswer(root.left)
        right = self.getAnswer(root.right)
        val = root.val
        if left > 0:
            val += left
        if right > 0:
            val += right
        if val > self.result:
            self.result = val
        return max(root.val, max(root.val+left, root.val+right))

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.result = root.val
        self.getAnswer(root)
        return self.result