# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        while root.left:
            pointer = root.left
            pre = None
            while root:
                if pre is not None:
                    pre.next = root.left
                root.left.next = root.right
                pre = root.right
                root = root.next
            root = pointer