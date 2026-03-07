"""
Leet Code: 79
"""
from typing import List


class Solution:
    def __init__(self):
        self.l = None
        self.m = None
        self.n = None
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        self.m = len(board)
        self.n = len(board[0])
        self.l = len(word)

        if self.m * self.n < self.l:
            return False

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0] and self.dfs(board, i, j, word, 0):
                    return True
        return False

    def dfs(self, board, i, j, word, index):

        # BASE CASE 1: Successfully matched all characters
        if index >= self.l:
            return True

        # BASE CASE 2: Boundary checks
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return False

        # BASE CASE 3: Character mismatch
        if board[i][j] != word[index] or board[i][j] == '#':
            return False

        temp = board[i][j]
        board[i][j] = '#'

        for dx, dy in self.directions:
            new_i = i + dx
            new_j = j + dy

            if self.dfs(board, new_i, new_j, word, index + 1):
                return True

        # BACKTRACING - restore cell
        board[i][j] = temp
        return False


if __name__ == '__main__':
    board_inp = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    inp_word = "ABCCED"
    print(Solution().exist(board=board_inp, word=inp_word))