def dfs_traversal(source, graph, visited):
    print(source, end=" ")
    visited[source] = 1

    for neighbour in graph[source]:
        if not visited[neighbour]:
            visited[neighbour] = 1
            dfs_traversal(neighbour, graph, visited)


def main(edge_list):
    n = len(edge_list)
    graph = {}
    for edge in edge_list:
        a, b = edge[0], edge[1]
        if a not in graph:
            graph[a] = []
        graph[a].append(b)

        if b not in graph:
            graph[b] = []
        graph[b].append(a)

    print("============== Graph using Adjacent List ==============")
    for node, neighbour in graph.items():
        print(f"Node {node}, Neighbour : {neighbour}")

    print("============== Graph DFS Traversal Output ==============")
    visited = [0] * (n + 1)
    dfs_traversal(0, graph, visited)


if __name__ == '__main__':
    EdgeList = [[0, 1], [1, 4], [1, 2], [2, 3]]
    main(EdgeList)
