def print_graph_for_adjacency_matrix(adjacency_matrix):
    print("============== Graph using Adjacent matrix ==============")
    for i in range(1, len(adjacency_matrix)):  # Nodes 1-4
        neighbors = []
        for j in range(1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 1:
                neighbors.append(str(j))

        print(f"Node: {i}, Neighbors: {' '.join(neighbors)}")


def build_graph_using_adjacency_matrix(edge_list):
    # Initialize adjacency matrix (5x5 with all zeros)
    n = len(edge_list)
    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Build adjacency matrix from an edge list (undirected graph)
    for edges in edge_list:
        a, b = edges[0], edges[1]
        adjacency_matrix[a][b] = 1
        adjacency_matrix[b][a] = 1

    # Print Graph
    print_graph_for_adjacency_matrix(adjacency_matrix=adjacency_matrix)


def print_graph_for_adjacency_list(adjacency_list):
    print("============== Graph using Adjacent List ==============")
    for node, neighbors in adjacency_list.items():
        neighbors_str = ' '.join(map(str, neighbors))
        print(f"Node: {node}, Neighbors: {neighbors_str}")


def build_graph_using_adjacency_list(edge_list):
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

    print_graph_for_adjacency_list(graph)


if __name__ == '__main__':
    EdgeList = [[1, 2], [2, 3], [3, 4], [4, 2], [1, 3]]
    build_graph_using_adjacency_matrix(EdgeList)
    build_graph_using_adjacency_list(EdgeList)
