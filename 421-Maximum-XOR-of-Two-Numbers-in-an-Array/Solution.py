class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # build a trie
        root = [None, None]
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                child = int(bool(num&(1<<i)))
                if node[child] == None:
                    newNode = [None, None]
                    node[child] = newNode
                    node = newNode
                else:
                    node = node[child]
        result = 0
        for num in nums:
            node = root
            cur = 0
            for i in range(31, -1, -1):
                child = int(bool(num&(1<<i)))
                if node[1^child]:
                    cur = cur | (1 << i)
                    node = node[1 ^ child]
                else:
                    node = node[child]
            result = max(result, cur)
        return result