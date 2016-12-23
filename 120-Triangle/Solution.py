class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = [0 for i in range(len(triangle)+1)]
        for row in triangle[::-1]:
            for i in range(len(row)):
                res[i] = row[i] + min(res[i], res[i + 1])
        return res[0]
