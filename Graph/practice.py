import collections
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        for i in range(len(board)):
            if board[0][i] == 'O':
                self.dfs(board, O, i)
            if board[len(board[0]) - 1][i] == 'O':
                self.dfs(board, len(board[0]) - 1, i)

        for j in range(len(board)):
            if board[j][0] == 'O':
                self.dfs(board, j, 0)
            if board[j][len(board) - 1] == 'O':
                self.dfs(board, j, len(board) - 1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'

        for row in board:
            print(row)

    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
            return

        board[i][j] = 'B'
        self.dfs(board, i+1, j)
        self.dfs(board, i-1, j)
        self.dfs(board, i, j+1)
        self.dfs(board, i, j-1)


if __name__ == '__main__':
    # board_matrix = [["O", "X", "X", "O", "X"],
    #                 ["X", "O", "O", "X", "O"],
    #                 ["X", "O", "X", "O", "X"],
    #                 ["O", "X", "O", "O", "O"],
    #                 ["X", "X", "O", "X", "O"]]
    board_matrix = [["X", "X", "X", "X"],
                    ["X", "O", "O", "X"],
                    ["X", "X", "O", "X"],
                    ["X", "O", "X", "X"]]
    Solution().solve(board=board_matrix)
