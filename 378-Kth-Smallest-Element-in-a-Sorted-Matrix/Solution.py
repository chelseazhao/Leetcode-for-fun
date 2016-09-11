class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        length = len(matrix)
        start = matrix[0][0]
        end = matrix[-1][-1]
        while start < end - 1:
            mid = (start + end) / 2
            num = self.findNum(mid, matrix, length)
            if num < k:
                start = mid
            else:
                end = mid
        if self.findNum(start, matrix, length) >= k:
            return start
        else:
            return end

    def findNum(self, num, matrix, length):
        x = 0
        y = length - 1
        count = 0
        while x < length and y >= 0:
            if matrix[x][y] <= num:
                count = count + y + 1
                x = x + 1
            else:
                y = y - 1
        return count
        
