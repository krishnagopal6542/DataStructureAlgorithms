# Leet Code : 994
# BFS is well suited for this problem

import collections
from typing import List


class Solution:
    def __init__(self):
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]

    def oranges_rotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        q = collections.deque()
        ans = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i, j))

        while q:
            q_size = len(q)
            temp = 0

            while q_size > 0:
                p = q.popleft()
                for k in range(4):
                    ii = p[0] + self.dx[k]
                    jj = p[1] + self.dy[k]
                    if 0 <= ii < r and 0 <= jj < c and grid[ii][jj] == 1:
                        grid[ii][jj] = 2
                        temp = 1
                        q.append((ii, jj))
                q_size -= 1
            ans += temp

        # check if any fresh oranges remains
        for v in grid:
            for x in v:
                if x == 1:
                    return -1
        return ans


if __name__ == '__main__':
    oranges_grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(Solution().oranges_rotting(grid=oranges_grid))
