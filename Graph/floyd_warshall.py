from typing import List


class Solution:
    def floyd_warshall(self, dist: List[List[int]]):
        v = len(dist)
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    if dist[i][k] == int(1e8) or dist[k][j] == int(1e8):
                        continue
                    distance_through_k = dist[i][k] + dist[k][j]
                    if dist[i][j] > distance_through_k:
                        dist[i][j] = distance_through_k

        # In case we want to detect negative cycle
        return self.has_negative_cycle(dist)

    @staticmethod
    def has_negative_cycle(dist):
        v = len(dist)

        # Check diagonal elements
        for i in range(v):
            if dist[i][i] < 0:
                return True

        # Run one more iteration to check if distances still decrease
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    if dist[i][k] == int(1e8) or dist[k][j] == int(1e8):
                        continue
                    distance_through_k = dist[i][k] + dist[k][j]
                    if dist[i][j] > distance_through_k:
                        return True  # Negative cycle detected
        return False


if __name__ == '__main__':
    distance_matrix_1 = [[0, 4, 108, 5, 108],
                         [108, 0, 1, 108, 6],
                         [2, 108, 0, 3, 108],
                         [108, 108, 1, 0, 2],
                         [1, 108, 108, 4, 0]]

    solution = Solution()
    response = solution.floyd_warshall(dist=distance_matrix_1)
    if response:
        print("Negative cycle detected!")
    else:
        print("No negative cycle detected.")
        print("\nShortest distances between every pair of vertices:")
        for row in distance_matrix_1:
            print(row)

    print("\n" + "=" * 50)
    print("Testing with a graph that has a negative cycle:")
    distance_matrix_2 = [[0, -1, 2],
                         [1, 0, 108],
                         [3, 1, 0]]

    solution = Solution()
    response = solution.floyd_warshall(dist=distance_matrix_2)
    if response:
        print("Negative cycle detected!")
    else:
        print("No negative cycle detected.")
        print("\nShortest distances between every pair of vertices:")
        for row in distance_matrix_2:
            print(row)

    # Test with a negative cycle
    print("\n" + "=" * 50)
    print("Testing with a graph that has a negative cycle:")
    distance_matrix_3 = [[0, 1, 108],
                         [108, 0, -1],
                         [-1, 108, 0]]

    response = solution.floyd_warshall(dist=distance_matrix_3)
    if response:
        print("Negative cycle detected!")
    else:
        print("No negative cycle detected.")
        print("\nShortest distances between every pair of vertices:")
        for row in distance_matrix_3:
            print(row)
