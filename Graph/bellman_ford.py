# https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

def bellman_ford(v, edges, src):
    # Initialize distance
    dist = [float('inf')] * v
    dist[src] = 0

    # Relaxation step - iterate V-1 times
    for i in range(v - 1):
        for edge in edges:
            node = edge[0]
            nbr = edge[1]
            wt = edge[2]

            if dist[node] == float('inf'):
                continue
            new_dist_of_nbr = dist[node] + wt
            if new_dist_of_nbr < dist[nbr]:
                dist[nbr] = new_dist_of_nbr

    # Check for negative weight cycles
    for edge in edges:
        node = edge[0]
        nbr = edge[1]
        wt = edge[2]

        if dist[node] == float('inf'):
            continue

        new_dist_of_nbr = dist[node] + wt
        if new_dist_of_nbr < dist[nbr]:
            return [-1]  # Negative cycle detected

    # Replace remaining infinity values with a large number (1e8)
    for i in range(v):
        if dist[i] == float('inf'):
            dist[i] = int(1e8)

    return dist


if __name__ == '__main__':
    print("=" * 60)
    print("Test Case 1: Normal Graph (No Negative Cycle)")
    print("=" * 60)
    V = 5
    source = 0
    edge_list = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]

    print(f"Vertices: {V}")
    print(f"Source: {source}")
    print(f"Edges: {edge_list}")
    print(f"\nResult: {bellman_ford(v=V, edges=edge_list, src=source)}")


    print("\n" + "=" * 60)
    print("Test Case 2: Graph with Negative Cycle")
    print("=" * 60)
    V = 4
    source = 0
    edge_list = [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]]

    print(f"Vertices: {V}")
    print(f"Source: {source}")
    print(f"Edges: {edge_list}")
    print(f"\nResult: {bellman_ford(v=V, edges=edge_list, src=source)}")

    result2 = bellman_ford(v=V, edges=edge_list, src=source)
    if result2 == [-1]:
        print(f"Interpretation: NEGATIVE CYCLE DETECTED!")
        print(f"  The graph contains a cycle: 1 → 2 → 3 → 1")
        print(f"  Cycle weight: -6 + 5 + (-2) = -3 (negative)")
        print(f"  This means we can keep reducing distances indefinitely.")
