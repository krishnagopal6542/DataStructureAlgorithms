# Leet Code: 310
import collections


class Solution:
    @staticmethod
    def edge_to_adj(n, edge_list):
        in_degree = [0] * n
        adj_list = [[] for _ in range(n)]
        for u, v in edge_list:
            in_degree[u] += 1
            in_degree[v] += 1
            adj_list[u].append(v)
            adj_list[v].append(u)  # Its not Directed graph, so both u & v need to be appended
        return adj_list, in_degree

    def find_min_height(self, n, edge_list):
        adjacency_list, in_degree = self.edge_to_adj(n, edge_list)
        q = collections.deque()

        result = []
        # Add all nodes in q with indegree == 1, As they are the leaf node
        for i in range(n):
            if in_degree[i] == 1:
                q.append(i)

        while n > 2:
            size = len(q)
            n -= size

            for _ in range(size):
                element = q.popleft()
                for nbr in adjacency_list[element]:
                    in_degree[nbr] -= 1
                    if in_degree[nbr] == 1:
                        q.append(nbr)

        while q:
            result.append(q.popleft())

        return result


if __name__ == '__main__':
    nodes = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    print(Solution().find_min_height(n=nodes, edge_list=edges))
