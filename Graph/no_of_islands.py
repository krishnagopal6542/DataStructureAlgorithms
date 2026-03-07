# Leet Code: 200

class Solution:
    def __init__(self):
        self.c = None
        self.r = None
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, 1, 0, -1]

    def dfs(self, i, j, grid):
        if i < 0 or j < 0 or i >= self.r or j >= self.c or grid[i][j] != '1':
            return

        grid[i][j] = '2'

        for k in range(4):
            ii = i + self.dx[k]
            jj = j + self.dy[k]
            self.dfs(ii, jj, grid=grid)

    def no_of_island(self, grid):
        self.r = len(grid)
        self.c = len(grid[0])
        island_count = 0

        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    island_count += 1

        return island_count


if __name__ == '__main__':
    input_grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(Solution().no_of_island(grid=input_grid))
