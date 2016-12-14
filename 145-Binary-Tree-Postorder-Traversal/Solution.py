# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = []
        result = []
        if not root:
            return result
        node.append(root)
        while node:
            tmp = node.pop()
            result.append(tmp.val)
            if tmp.left:    
                node.append(tmp.left)
            if tmp.right:
                node.append(tmp.right)
        return result[::-1]
