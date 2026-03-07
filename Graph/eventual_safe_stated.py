# Leet Code: 802

class SafeState:
    def dfs(self, node, adj_list, visited, current_path):
        visited[node] = True
        current_path[node] = True

        for neighbour in adj_list[node]:
            if not visited[neighbour]:
                is_cycle_found = self.dfs(neighbour, adj_list, visited, current_path)
                if is_cycle_found:
                    return True
            else:
                if current_path[neighbour]:
                    return True
        current_path[node] = False
        return False

    def eventual_safe_nodes(self, graph):
        v = len(graph)

        visited = [False] * v
        current_path = [False] * v

        for i in range(v):
            if not visited[i]:
                self.dfs(i, graph, visited, current_path)

        result = []
        for i in range(v):
            if not current_path[i]:
                result.append(i)

        return result


if __name__ == '__main__':
    graph_list = [[1, 2], [2, 3], [5], [0], [5], [], []]
    SS = SafeState()
    print(SS.eventual_safe_nodes(graph_list))
