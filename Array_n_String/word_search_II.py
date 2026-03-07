from typing import List


class Solution:
    def __init__(self):
        self.directions = None
        self.m = None
        self.n = None

    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        for word in words:
            print(f"\n=== Searching for '{word}' ===")
            if self.is_exist(board, word):
                print(f"✓ Found '{word}'")
                result.add(word)
            else:
                print(f"✗ NOT found '{word}'")
        print(f"Final result: {list(result)}")
        return list(result)

    def is_exist(self, board, word):
        self.m = len(board)
        self.n = len(board[0])
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        if self.m * self.n < len(word):
            return False

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    print(f"  Trying start position [{i},{j}] = '{board[i][j]}'")
                    if self.dfs(board, i, j, word, 0):
                        return True
        return False

    def dfs(self, board, i, j, word, index):
        if index == len(word):
            return True

        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return False

        if board[i][j] != word[index] or board[i][j] == '#':
            return False

        temp = board[i][j]
        board[i][j] = '#'

        for dx, dy in self.directions:
            new_i = i + dx
            new_j = j + dy
            if self.dfs(board, new_i, new_j, word, index + 1):
                board[i][j] = temp
                return True

        board[i][j] = temp
        return False


if __name__ == '__main__':
    inp_board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print(Solution().find_words(inp_board, words))
