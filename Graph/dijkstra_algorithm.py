import heapq
from typing import List


def dijkstra(adj: List[List[List[int]]], src: int) -> list[float]:
    n = len(adj)
    distances = [float('inf')] * n
    distances[src] = 0
    pq = [(0, src)]  # (distance of src, src)

    while pq:
        distance_of_node_frm_src, node = heapq.heappop(pq)

        # iterate of neighbours
        for nbr_info in adj[node]:
            nbr, weight = nbr_info[0], nbr_info[1]
            saved_dist_of_nbr_from_src = distances[nbr]
            new_dist_of_nbr_from_src = distance_of_node_frm_src + weight

            # Checking if reaching to neighbor with lesser distance via current node
            if new_dist_of_nbr_from_src < saved_dist_of_nbr_from_src:
                heapq.heappush(pq, (new_dist_of_nbr_from_src, nbr))
                distances[nbr] = new_dist_of_nbr_from_src

    for i in range(n):
        if distances[i] == float('inf'):
            distances[i] = -1  # unreachable

    return distances


def edges_to_adj(edges: List[List[int]], n: int) -> List[List[List[int]]]:
    """Convert edge list to adjacency list for undirected graph"""
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append([v, w])
        adj[v].append([u, w])  # undirected graph
    return adj


if __name__ == '__main__':
    edge_list = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
    source = 2
    edge_len = len(edge_list)  # number of nodes

    # Convert edges to adjacency list
    adj_list = edges_to_adj(edge_list, edge_len)  # Here each two elements are for 0, 1 and 2 accordingly
    dist = dijkstra(adj=adj_list, src=source)
    for i in range(len(dist)):
        print(f"Distance from source:{source} to node:{i} == {dist[i]}")
