# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generate(self, begin, end):
        result = []
        if begin > end:
            result.append(None)
            return result
        for i in range(begin, end + 1):
            left_tree = self.generate(begin, i - 1)
            right_tree = self.generate(i + 1, end)
            for j in range(len(left_tree)):
                for k in range(len(right_tree)):
                    node = TreeNode(i + 1)
                    result.append(node)
                    node.left = left_tree[j]
                    node.right = right_tree[k]
        return result
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            result = []
            return result
        return self.generate(0, n - 1)

if __name__ == '__main__':
    solution = Solution()
    print solution.generateTrees(0)
