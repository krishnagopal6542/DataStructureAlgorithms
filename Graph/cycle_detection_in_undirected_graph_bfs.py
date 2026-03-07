import collections


class CycleDetector:
    @staticmethod
    def bfs(node, adj_list, visited, parent):
        q = collections.deque()
        q.append(node)
        visited[node] = True
        while q:
            element = q.popleft()
            for neighbour in adj_list[element]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    parent[neighbour] = element
                    q.append(neighbour)
                elif parent[element] != neighbour:
                    return True
        return False

    @staticmethod
    def create_adjacency_list(v, edge_lists):
        adj_list = [[] for _ in range(v)]
        for edge in edge_lists:
            a, b = edge[0], edge[1]
            adj_list[a].append(b)
            adj_list[b].append(a)
        return adj_list

    def main(self, v, edge_list):
        adjacent_list = self.create_adjacency_list(v, edge_list)
        visited = [False] * v
        parent = [-1] * v
        for i in range(v):
            if not visited[i]:
                ans = self.bfs(i, adjacent_list, visited, parent)
                if ans:
                    return True
        return False


if __name__ == '__main__':
    CD = CycleDetector()
    V = 4
    edges = [[0, 1], [1, 2], [2, 3], [3, 3]]
    print(CD.main(V, edges))
