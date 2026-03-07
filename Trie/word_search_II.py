"""
Leet Code: 212
"""


class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = [None] * 26
        self.word = ""


class Solution:
    def insert(self, root, word):
        crawl = root
        for ch in word:
            _idx = ord(ch) - ord('a')
            if crawl.children[_idx] is None:
                crawl.children[_idx] = TrieNode()
            crawl = crawl.children[_idx]

        crawl.end_of_word = True
        crawl.word = word

    def dfs(self, board, i, j, root, result):
        # Check boundary condition and visited
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '$':
            return

        ch = board[i][j]
        _idx = ord(ch) - ord('a')

        if root.children[_idx] is None:
            return

        root = root.children[_idx]

        # Found word
        if root.end_of_word:
            result.append(root.word)
            root.end_of_word = False  # To avoid duplicates

        # Mark current cell as visited
        temp = board[i][j]
        board[i][j] = '$'

        # Explore all for directions
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            new_i = i + dx
            new_j = j + dy
            self.dfs(board=board, i=new_i, j=new_j, root=root, result=result)

        # Backtracking & restore cell
        board[i][j] = temp

    def find_word(self, board, words):
        result = []
        r = len(board)
        c = len(board[0])

        # Build Trie
        root = TrieNode()
        for word in words:
            self.insert(root, word)

        # Search for word in board
        for i in range(r):
            for j in range(c):
                ch = board[i][j]
                idx = ord(ch) - ord('a')
                if root.children[idx] is not None:
                    self.dfs(board, i, j, root, result)

        return result


if __name__ == '__main__':
    _board = [["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]]
    _words = ["oa", "oaa"]
    print(Solution().find_word(board=_board, words=_words))
