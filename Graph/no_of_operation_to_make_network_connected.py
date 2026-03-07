# Leet code : 1319
from typing import List


class Solution:
    def dfs(self, adj, visited, src):
        visited[src] = True
        for j in adj[src]:
            if not visited[j]:
                self.dfs(adj=adj, visited=visited, src=j)

    def make_connected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        adj_list = [[] for _ in range(n)]

        for edge in connections:
            u, v = edge[0], edge[1]
            adj_list[u].append(v)
            adj_list[v].append(u)

        component = 0
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                self.dfs(adj=adj_list, visited=visited, src=i)
                component += 1

        return component - 1


if __name__ == '__main__':
    computers = 4
    connection_list = [[0, 1], [0, 2], [1, 2]]
    print(Solution().make_connected(n=computers, connections=connection_list))
