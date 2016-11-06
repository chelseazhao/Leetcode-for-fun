class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        i = 0
        while i < 9:
            j = 0
            board_map = {}
            while j < 9:
                if board[i][j] != '.' and board[i][j] in board_map:
                    return False
                else:
                    board_map[board[i][j]] = True
                j += 1
            i += 1

        j = 0
        while j < 9:
            i = 0
            board_map = {}
            while i < 9:
                if board[i][j] != '.' and board[i][j] in board_map:
                    return False
                else:
                    board_map[board[i][j]] = True
                i += 1
            j += 1

        i = 0
        while i < 9:
            j = 0
            while j < 9:
                m = 0
                board_map = {}
                while m < 3:
                    n = 0
                    while n < 3:
                        if board[i + m][j + n] != '.' and board[i + m][j + n] in board_map:
                            return False
                        else:
                            board_map[board[i + m][j + n]] = True
                        n += 1
                    m += 1
                j += 3
            i += 3
        return True
