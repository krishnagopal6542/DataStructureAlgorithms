# Leet code : 1857
import collections
from collections import deque, defaultdict


def largest_path_value(colors: str, edges: list[list[int]]) -> int:
    n = len(colors)
    ans = 0

    # build adj list from given edge list
    graph = defaultdict(list)

    count = [[0] * 26 for _ in range(n)]

    # Get each node indegree
    indegree = [0] * n

    # Build graph and calculate indegree
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Initialize queue with nodes having indegree 0
    q = collections.deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    processed = 0

    while q:
        element = q.popleft()
        processed += 1

        # Increment count for current node's color
        count[element][ord(colors[element]) - ord('a')] += 1

        # Update answer with max count for current node's color
        ans = max(ans, count[element][ord(colors[element]) - ord('a')])

        # Now process Neighbor
        for nbr in graph[element]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0:
                q.append(nbr)

            # Pass color counts to neighbor, updating with max
            for j in range(26):
                count[nbr][j] = max(count[nbr][j], count[element][j])

    return ans if processed == n else -1


if __name__ == '__main__':
    Colors = "a"
    Edges = [[0,0]]
    print(largest_path_value(colors=Colors, edges=Edges))
