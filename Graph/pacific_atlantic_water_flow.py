# Leet Code: 417
from typing import List


class Solution:
    def __init__(self):
        self.row = None
        self.column = None
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

    def dfs(self, row, col, boolean_matrix, height):
        if row < 0 or col < 0 or row >= self.row or col >= self.column:
            return

        if boolean_matrix[row][col]:  # already visited check
            return

        boolean_matrix[row][col] = True

        for k in range(4):
            ii = row + self.dx[k]
            jj = col + self.dy[k]
            if 0 <= ii < self.row and 0 <= jj < self.column:
                if height[ii][jj] >= height[row][col]:
                    self.dfs(ii, jj, boolean_matrix, height)

    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, column = len(heights), len(heights[0])
        self.row, self.column = row, column

        result = []

        # Step: 1 Create two 2D vector for both PACIFIC & ATLANTIC
        pacific_reachable = [[False] * column for _ in range(row)]
        atlantic_reachable = [[False] * column for _ in range(row)]

        # Step: 2 Make DFS call for either of the edges of PACIFIC and mark TRUE if it reaches ATLANTIC
        """ For Pacific """
        for j in range(column):
            self.dfs(row=0, col=j, boolean_matrix=pacific_reachable, height=heights)
        for i in range(row):
            self.dfs(row=i, col=0, boolean_matrix=pacific_reachable, height=heights)

        # Step: 3 Make DFS call for either of the edges of ATLANTIC and mark TRUE if it reaches PACIFIC
        """ For Atlantic """
        for j in range(column):
            self.dfs(row=row - 1, col=j, boolean_matrix=atlantic_reachable, height=heights)
        for i in range(row):
            self.dfs(row=i, col=column - 1, boolean_matrix=atlantic_reachable, height=heights)

        # Step: 4 Iterate to each created 2D vector and see if both [i][j] are TRUE. If both are true, save in result.
        for i in range(row):
            for j in range(column):
                if pacific_reachable[i][j] == True and atlantic_reachable[i][j] == True:
                    result.append([i, j])
        return result


if __name__ == '__main__':
    Heights = [[11,3,2,4,14,6,13,18,1,4,12,2,4,1,16],[5,11,18,0,15,14,6,17,2,17,19,15,12,3,14],[10,2,5,13,11,11,13,19,11,17,14,18,14,3,11],[14,2,10,7,5,11,6,11,15,11,6,11,12,3,11],[13,1,16,15,8,2,16,10,9,9,10,14,7,15,13],[17,12,4,17,16,5,0,4,10,15,15,15,14,5,18],[9,13,18,4,14,6,7,8,5,5,6,16,13,7,2],[19,9,16,19,16,6,1,11,7,2,12,10,9,18,19],[19,5,19,10,7,18,6,10,7,12,14,8,4,11,16],[13,3,18,9,16,12,1,0,1,14,2,6,1,16,6],[14,1,12,16,7,15,9,19,14,4,16,6,11,15,7],[6,15,19,13,3,2,13,7,19,11,13,16,0,16,16],[1,5,9,7,12,9,2,18,6,12,1,8,1,10,19],[10,11,10,11,3,5,12,0,0,8,15,7,5,13,19],[8,1,17,18,3,6,8,15,0,9,8,8,12,5,18],[8,3,6,12,18,15,10,10,12,19,16,7,17,17,1],[12,13,6,4,12,18,18,9,4,9,13,11,5,3,14],[8,4,12,11,2,2,10,3,11,17,14,2,17,4,7],[8,0,14,0,13,17,11,0,16,13,15,17,4,8,3],[18,15,8,11,18,3,10,18,3,3,15,9,11,15,15]]
    print(Solution().pacific_atlantic(Heights))