class Solution(object):
    def bfs(self, board, x, y, row, column):
        if board[x][y] != 'O':
            return
        queue = [(x, y)]
        board[x][y] = 'A'
        while queue:
            x, y = queue.pop()
            if x - 1 >= 0 and board[x - 1][y] == 'O':
                board[x - 1][y] = 'A'
                queue.append((x-1, y))
            if x + 1 < row and board[x + 1][y] == 'O':
                board[x + 1][y] = 'A'
                queue.append((x+1, y))
            if y - 1 >= 0 and board[x][y - 1] == 'O':
                board[x][y - 1] = 'A'
                queue.append((x, y - 1))
            if y + 1 < column and board[x][y + 1] == 'O':
                board[x][y + 1] = 'A'
                queue.append((x, y + 1))
            
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if row <= 2 or not board:
            return
        column = len(board[0])
        if column <= 2:
            return
        for i in range(row):
            self.bfs(board, i, 0, row, column)
            self.bfs(board, i, column - 1, row, column)
        for i in range(column):
            self.bfs(board, 0, i, row, column)
            self.bfs(board, row - 1, i, row, column)
        for i in range(row):
            for j in range(column):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                
