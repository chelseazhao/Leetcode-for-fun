# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
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
            temp = node.pop()
            result.append(temp.val)
            if temp.right:
                node.append(temp.right)
            if temp.left:
                node.append(temp.left)
        return result
        
