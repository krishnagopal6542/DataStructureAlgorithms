"""
Leet Code: 1091
"""
import collections
from typing import List


class Solution:
    def __init__(self):
        self.row = None
        self.col = None
        self.dx = [1, -1, -1, 1, 0, -1, 0, 1]
        self.dy = [1, 1, -1, -1, 1, 0, -1, 0]

    def bfs_traversal(self, grid):
        q = collections.deque()
        q.append((0, 0))
        ans = 0

        while q:
            ans += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                if i == self.row - 1 and j == self.col - 1:
                    return ans

                for k in range(8):
                    ii = i + self.dx[k]
                    jj = j + self.dy[k]
                    if 0 <= ii < self.row and 0 <= jj < self.col:
                        if grid[ii][jj] == 0:
                            q.append((ii, jj))
                            grid[ii][jj] = 1
        return ans

    def shortest_path_binary_matrix(self, grid: List[List[int]]) -> int:
        self.row, self.col = len(grid), len(grid[0])
        if grid[0][0] != 0:
            return -1

        res = self.bfs_traversal(grid)

        return res


if __name__ == '__main__':
    grid_matrix = [[0, 1],
                   [1, 0]]
    print(Solution().shortest_path_binary_matrix(grid=grid_matrix))
