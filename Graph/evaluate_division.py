# Leet Code: 399
from typing import List


class Solution:
    def dfs(self, adj, src, dst, visited, product, ans):
        if src in visited:
            return ans

        visited.add(src)
        if src == dst:
            return product

        for v, val in adj[src]:
            ans = self.dfs(adj, v, dst, visited, product * val, ans)
            if ans != -1.0:
                return ans

        return ans

    def calc_equation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)

        adj = {}
        for i in range(n):
            u = equations[i][0]
            v = equations[i][1]
            val = values[i]

            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []

            adj[u].append((v, val))
            adj[v].append((u, 1.0 / val))

        result = []
        for query in queries:
            src = query[0]
            dst = query[1]

            product = 1.0
            ans = -1.0
            if src in adj:
                visited = set()
                ans = self.dfs(adj, src, dst, visited, product, ans)

            result.append(ans)

        return result


if __name__ == '__main__':
    equation = [["a", "b"], ["b", "c"]]
    value = [2.0, 3.0]
    queri = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(Solution().calc_equation(equations=equation, values=value, queries=queri))
