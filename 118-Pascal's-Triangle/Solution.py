class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[] for i in range(numRows)]
        for row in range(numRows):
            part = [1 for i in range(row)]
            for i in range(row+1):
                if i == 0 or i == row - 1:
                    continue
                else:
                    part[i] = result[row - 1][i - 1] + result[row - 1][i]
            result[i] = part
        return result
