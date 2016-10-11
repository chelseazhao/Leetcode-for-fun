# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result = []
        if root is None:
            return result
        self.dfs(root, result, [])
        return result

    def dfs(self, root, result, part):
        
        if root.left is None and root.right is None:
            part.append(str(root.val))
            result.append('->'.join(part))
            part.pop()
            return
        if root.left:
            part.append(str(root.val))
            self.dfs(root.left, result, part)
            part.pop()
        if root.right:
            part.append(str(root.val))
            self.dfs(root.right, result, part)
            part.pop()
