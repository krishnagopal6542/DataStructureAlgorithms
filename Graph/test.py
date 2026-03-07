# Topological sort
import collections


class Solution:
    def __init__(self):
        self.q = collections.deque()

    def topological_sort_dfs(self, node, visited, adj_list):
        visited[node] = 1
        for neighbour in adj_list[node]:
            if not visited[neighbour]:
                self.topological_sort_dfs(node=neighbour, visited=visited, adj_list=adj_list)

        self.q.appendleft(node)

    @staticmethod
    def create_adj_list(v, edge_list):
        adj_list = [[] for _ in range(v)]

        for u_node, v_node in edge_list:
            adj_list[u_node].append(v_node)

        return adj_list

    def main(self, vertex, edge_list):
        self.q.clear()  # Clear the deque for reuse
        adj_list = self.create_adj_list(vertex, edge_list)
        visited = [0] * vertex
        for i in range(vertex):
            if not visited[i]:
                self.topological_sort_dfs(i, visited, adj_list)

        ans = []
        for element in self.q:
            ans.append(element)
        return ans


if __name__ == '__main__':
    edges = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]]
    Vertex = 6
    print(Solution().main(Vertex, edges))
