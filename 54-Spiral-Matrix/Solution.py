class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        row = len(matrix)
        if row == 0:
            return matrix
        column = len(matrix[0])
        num = row * column
        edge = min(row, column)
        if edge == 1:
            if row == 1:
                return matrix[0]
            elif column == 1:
                for i in range(row):
                    result.append(matrix[i][0])
                return result
        for loop in range(edge - 1):
            for i in range(loop, column - loop):
                result.append(matrix[loop][i])
            if len(result) == num:
                return result
            for j in range(loop + 1, row - loop):
                result.append(matrix[j][column - loop - 1])
            if len(result) == num:
                return result
            for k in range(column - loop - 2, loop - 1, -1):
                result.append(matrix[row - loop - 1][k])
            if len(result) == num:
                return result
            for l in range(row - loop - 2, loop, -1):
                result.append(matrix[l][loop])
            if len(result) == num:
                return result
if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    sol = Solution()
    print sol.spiralOrder(matrix)
