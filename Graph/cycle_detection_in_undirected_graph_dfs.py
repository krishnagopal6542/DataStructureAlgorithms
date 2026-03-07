# Cycle detection in Undirected Graph: Using DFS

class CycleDetector:

    def dfs(self, node, adj_list, visited, parent):
        visited[node] = True
        for neighbour in adj_list[node]:
            if not visited[neighbour]:
                res = self.dfs(neighbour, adj_list, visited, node)
                if res:
                    return True
            elif visited[neighbour] == True and neighbour != parent:
                return True
        return False

    @staticmethod
    def create_adjacency_list(v, edge_list):
        adj_list = [[] for _ in range(v)]
        for edge in edge_list:
            a, b = edge[0], edge[1]
            adj_list[a].append(b)
            adj_list[b].append(a)
        return adj_list

    def main(self, v, edge_list):
        # Convert an edge list to an adjacency list
        adjacency_list = self.create_adjacency_list(v, edge_list)
        visited = [False] * v
        for i in range(v):
            if not visited[i]:
                ans = self.dfs(i, adjacency_list, visited, -1)
                if ans:
                    return True

        return False


if __name__ == '__main__':
    CD = CycleDetector()
    V = 4
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
    print(CD.main(V, edges))
