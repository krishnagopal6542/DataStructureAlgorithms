import collections


def bfs_traversal(source, graph, n):
    q = collections.deque()
    q.append(source)
    visited = [0] * (n + 1)
    visited[source] = 1

    traversal_result = []

    while q:
        edge = q.popleft()
        traversal_result.append(edge)
        neighbour = graph[edge]
        for node in neighbour:
            if visited[node] != 1:
                visited[node] = 1
                q.append(node)

    return traversal_result


def bfs_traversal_level_wise(source, graph, n):
    q = collections.deque()
    q.append(source)
    visited = [0] * (n + 1)
    visited[source] = 1

    level_wise_result = []
    while q:
        level_size = len(q)
        current_level = []

        for _ in range(level_size):
            node = q.popleft()
            current_level.append(node)
            neighbours = graph.get(node, [])
            for neighbour in neighbours:
                if not visited[neighbour]:
                    visited[neighbour] = 1
                    q.append(neighbour)
        level_wise_result.append(current_level)

    return level_wise_result


def main(edge_list):
    n = len(edge_list)
    graph = {}

    for edges in edge_list:
        a, b = edges[0], edges[1]
        if a not in graph:
            graph[a] = []
        graph[a].append(b)

        if b not in graph:
            graph[b] = []
        graph[b].append(a)

    traversal = bfs_traversal(0, graph, 4)
    levelwise_traversal = bfs_traversal_level_wise(0, graph, 4)

    print("============== Graph using Adjacent List ==============")
    for node, neighbour in graph.items():
        print(f"Node {node}, Neighbour : {neighbour}")

    print("============== Graph BFS Traversal Output ==============")
    print("BFS_Traversal ==> ", traversal)

    print("============== Graph BFS Traversal LevelWise Output ==============")
    print("BFS_Traversal Levelwise ==> ", levelwise_traversal)


if __name__ == '__main__':
    EdgeList = [[0, 1], [1, 4], [1, 2], [2, 3]]
    main(EdgeList)
