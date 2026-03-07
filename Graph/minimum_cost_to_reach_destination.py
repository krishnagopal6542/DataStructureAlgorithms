# Leet Code: 1928
import heapq
from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def min_cost(max_time: int, edges: List[List[int]], passing_fees: List[int]) -> int:
        # Number of cities
        n = len(passingFees)

        # Make Adjacency List
        graph = defaultdict(list)

        for u, v, wt in edges:
            graph[u].append((v, wt))
            graph[v].append((u, wt))

        costs = [float("inf")] * n
        times = [maxTime + 1] * n

        # Starting at city 0 with its passing fee
        times[0] = 0
        costs[0] = passingFees[0]

        q = [(passingFees[0], 0, 0)]  # (current total cost, current time, current city)

        while q:
            curr_cost, curr_time, curr_city = heapq.heappop(q)

            if curr_city == n - 1:
                return curr_cost

            for next_city, time_travel in graph[curr_city]:
                if curr_time + time_travel > max_time:
                    continue

                new_time = curr_time + time_travel
                new_cost = curr_cost + passing_fees[next_city]
                if new_cost < costs[next_city] or new_time < times[next_city]:
                    costs[next_city] = new_cost
                    times[next_city] = new_time
                    heapq.heappush(q, (new_cost, new_time, next_city))

        # If we cannot reach the destination city within the allowed time, return -1
        return -1


if __name__ == '__main__':
    maxTime = 30
    edgeList = [[0, 1, 10],
                [1, 2, 10],
                [2, 5, 10],
                [0, 3, 1],
                [3, 4, 10],
                [4, 5, 15]]
    passingFees = [5, 1, 2, 20, 20, 3]
    print(Solution().min_cost(max_time=maxTime, edges=edgeList, passing_fees=passingFees))
