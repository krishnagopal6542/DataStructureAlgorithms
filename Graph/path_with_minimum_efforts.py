# Leet Code: 1631

from heapq import heappush, heappop
from typing import List


class Solution:

    @staticmethod
    def minimum_effort_path(heights: List[List[int]]) -> float:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        n = len(heights)
        m = len(heights[0])

        # Min heap priority queue: (distance, x, y)
        pq = []

        # Distance matrix initialized with infinity
        distance = [[float('inf')] * m for _ in range(n)]

        # Start from (0, 0)
        heappush(pq, (0, 0, 0))
        distance[0][0] = 0

        while pq:
            distance_of_par, x, y = heappop(pq)

            # Explore all 4 directions
            for k in range(4):
                ii = x + dx[k]
                jj = y + dy[k]

                # Check boundaries
                if ii < 0 or jj < 0 or ii >= n or jj >= m:
                    continue

                # Calculate new distance (effort)
                new_dist_of_nbr = max(distance_of_par, abs(heights[x][y] - heights[ii][jj]))

                # If we found a better path, update it
                if new_dist_of_nbr < distance[ii][jj]:
                    distance[ii][jj] = new_dist_of_nbr
                    heappush(pq, (distance[ii][jj], ii, jj))

        return distance[n - 1][m - 1]


if __name__ == '__main__':
    input_heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print(Solution().minimum_effort_path(heights=input_heights))