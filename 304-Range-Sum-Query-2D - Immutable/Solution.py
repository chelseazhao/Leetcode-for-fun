class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        row = len(matrix)
        if row == 0:
            col = 0
        else:
            col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    continue
                self.matrix[i][j] = self.matrix[i][j] + (self.matrix[i-1][j] if i >= 1 else 0) + (self.matrix[i][j-1] if j >= 1 else 0) - (self.matrix[i-1][j-1] if i >= 1 and j >= 1 else 0) 
            

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.matrix[row2][col2] - (self.matrix[row1-1][col2] if row1 >= 1 else 0) - (self.matrix[row2][col1-1] if col1 >= 1 else 0) + (self.matrix[row1-1][col1-1] if row1 >= 1 and col1 >= 1 else 0)
        


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
