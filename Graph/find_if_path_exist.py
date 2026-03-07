import collections


def bfs_traversal(source, graph, n):
    q = collections.deque()
    q.append(source)
    visited = {source: True}
    while q:
        edge = q.popleft()
        neighbours = graph[edge]
        for neighbour in neighbours:
            if neighbour not in visited:
                visited[neighbour] = True
                q.append(neighbour)
    return visited


def main(n, edge_list, source, destination):
    graph = {}
    for edges in edge_list:
        a, b = edges[0], edges[1]
        if a not in graph:
            graph[a] = []
        graph[a].append(b)

        if b not in graph:
            graph[b] = []
        graph[b].append(a)

    visited = bfs_traversal(source, graph, n)
    return True if destination in visited else False


if __name__ == '__main__':
    N = 3
    Edges = [[0, 1], [1, 2], [2, 0]]
    Source = 0
    Destination = 2
    print(main(N, Edges, Source, Destination))
