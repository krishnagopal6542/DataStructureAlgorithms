# Leet Code: 787
import heapq
from heapq import heappop, heappush
from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build adjacency graph list
        graph = defaultdict(list)
        for i in range(len(flights)):
            from_node = flights[i][0]
            to = flights[i][1]
            wt = flights[i][2]
            graph[from_node].append((to, wt))

        # Priority queue: (stops_taken, node, dist)
        pq = []

        # Distance array initialization with infinity
        distance = [float('inf')] * n
        distance[src] = 0

        # Start from source with 0 stops and 0 distance
        heappush(pq, (0, src, 0))

        while pq:
            pr = heappop(pq)
            stop_taken = pr[0]
            node = pr[1]
            dist_of_par = pr[2]

            # if we have taken more than K steps, stop exploring further
            if stop_taken > k:
                break

            # Explore all neighbour
            for nbr_info in graph[node]:
                nbr = nbr_info[0]
                wt = nbr_info[1]
                new_dist_of_nbr = dist_of_par + wt

                # If we found better path, update it
                if new_dist_of_nbr < distance[nbr]:
                    distance[nbr] = new_dist_of_nbr
                    heappush(pq, (stop_taken + 1, nbr, new_dist_of_nbr))

        if distance[dst] == float('inf'):
            return -1
        else:
            return int(distance[dst])


if __name__ == '__main__':
    _n = 4
    flight_map = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    source = 0
    destination = 3
    k_stop = 1
    print(Solution().find_cheapest_price(n=_n, flights=flight_map, src=source, dst=destination, k=k_stop))
