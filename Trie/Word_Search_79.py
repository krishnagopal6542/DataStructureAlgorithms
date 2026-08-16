"""
Leet Code: 79 Word Search
"""
from typing import List


class Solution:
    def __init__(self):
        self.direction = None
        self.l = None
        self.n = None
        self.m = None

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        self.l = len(word)

        self.direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        if self.m * self.n < self.l:
            return False

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0] and self.dfs(board, i, j, word, 0):
                    return True

        return False

    def dfs(self, board, i, j, word, idx):
        # Successfully matched all character
        if idx >= self.l:
            return True

        # Boundry Check
        if i >= self.m or j >= self.n or i < 0 or j < 0:
            return False

        if word[idx] != board[i][j] or board[i][j] == '#':
            return False

        temp = board[i][j]
        board[i][j] = '#'

        for dy, dx in self.direction:
            new_i = i + dy
            new_j = j + dx
            if self.dfs(board, new_i, new_j, word, idx + 1):
                return True

        # BACKTRACKING - restore cell
        board[i][j] = temp
        return False

if __name__ == '__main__':
    Board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    Word = "ABCCED"
    print(Solution().exist(board=Board, word=Word))
