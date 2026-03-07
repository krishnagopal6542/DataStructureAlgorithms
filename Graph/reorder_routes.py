# Leet Code: 1466
def dfs_traversal(source, forward_neighbour, backward_neighbour, ans, visited):
    visited[source] = True

    # Forward neighbors need to change a direction
    for nbr in forward_neighbour[source]:
        if not visited[nbr]:
            ans[0] += 1
            dfs_traversal(nbr, forward_neighbour, backward_neighbour, ans, visited)

    for nbr in backward_neighbour[source]:
        if not visited[nbr]:
            dfs_traversal(nbr, forward_neighbour, backward_neighbour, ans, visited)


def main(n, connections):
    forward_neighbours = [[] for _ in range(n)]
    backward_neighbours = [[] for _ in range(n)]
    visited = [False] * n

    for edge in connections:
        a, b = edge[0], edge[1]
        forward_neighbours[a].append(b)
        backward_neighbours[b].append(a)

    ans = [0]
    dfs_traversal(0, forward_neighbours, backward_neighbours, ans, visited)
    return ans[0]


if __name__ == '__main__':
    N = 6
    Connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    print(main(N, Connections))
