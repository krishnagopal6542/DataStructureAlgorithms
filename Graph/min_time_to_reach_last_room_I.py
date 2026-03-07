"""
Leet Code: 3341 Find Minimum Time to Reach Last Room I

Problem: Find minimum time to reach bottom-right cell from top-left in a grid
         where moveTime[i][j] = earliest time you can enter cell (i,j)

Approach: Dijkstra's Algorithm
================================

Key Points:
-----------
1. Graph Modeling:
   - Each cell = node
   - Edge weight = 1 (move time) + wait time (if arrive early)
   - Find the shortest path from (0,0) to (m-1, n-1)

2. Core Logic:
   - Use min-heap to always process cell with minimum time (greedy)
   - arrival_time = curr_time + max(moveTime[i][j] - curr_time, 0) + 1
   - Relaxation: Update distance if found better path

3. Algorithm:
   a) Initialize: distance[0][0] = 0, push (0,0,0) to min-heap
   b) Pop cell with min time
   c) If destination, return time
   d) For each neighbor: calculate arrival_time, relax if better
   e) Repeat until destination or heap empty

4. Optimization:
   - Early termination when destination popped (optimal found)
   - Skip cells already processed with better time

Time: O(m*n * log(m*n))
Space: O(m*n)
"""

import heapq
from typing import List


class Solution:
    @staticmethod
    def min_time_to_reach(move_time: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(move_time), len(moveTime[0])
        distance = [[float('inf')] * n for _ in range(m)]
        distance[0][0] = 0

        pq = []
        heapq.heappush(pq, (0, 0, 0))  # (time, i, j)

        while pq:
            curr_time, i, j = heapq.heappop(pq)
            if i == m - 1 and j == n - 1:
                return curr_time

            for dir_i, dir_j in directions:
                _i = dir_i + i
                _j = dir_j + j

                if 0 <= _i < m and 0 <= _j < n:
                    wait = max(move_time[_i][_j] - curr_time, 0)
                    arrival_time = curr_time + wait + 1

                    if distance[_i][_j] > arrival_time:
                        distance[_i][_j] = arrival_time
                        heapq.heappush(pq, (arrival_time, _i, _j))
        return -1


if __name__ == '__main__':
    moveTime = [[0,0,0],[0,0,0]]
    print(Solution().min_time_to_reach(move_time=moveTime))
