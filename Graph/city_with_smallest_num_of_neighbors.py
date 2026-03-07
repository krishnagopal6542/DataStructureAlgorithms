# Leet Code: 1334
from typing import List


class Solution:
    @staticmethod
    def find_the_city(n: int, edges: List[List[int]], distance_threshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for edge in edges:
            u, v, wt = edge[0], edge[1], edge[2]
            dist[u][v] = wt
            dist[v][u] = wt

        # Set diagonal to 0
        for i in range(n - 1):
            dist[i][i] = 0

        # Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] == float('inf') or dist[k][j] == float('inf'):
                        continue
                    dist_through_k = dist[i][k] + dist[k][j]
                    dist[i][j] = min(dist[i][j], dist_through_k)

        # City with the smallest number of reachable cities
        count_city = n
        city_no = -1

        for city in range(n):
            count = 0
            for adj_city in range(n):
                if dist[city][adj_city] <= distance_threshold:
                    count += 1

            if count <= count_city:
                count_city = count
                city_no = city

        return city


if __name__ == '__main__':
    no_of_cities = 4
    edgeList = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]  # [from, to, weight]
    distanceThreshold = 4
    print(Solution().find_the_city(n=no_of_cities, edges=edgeList, distance_threshold=distanceThreshold))
