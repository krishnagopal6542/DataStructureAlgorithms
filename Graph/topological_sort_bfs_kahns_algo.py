"""
Topological sort using BFS is known as Kahn's Algorithm
Any Node having 0 indegree will have 0 dependency/prerequisite
Always start processing from Node with 0 indegree

Algo:
    Calculate the InDegree for all nodes and save in array
    Push all 0 indegree Nodes in Queue
    While the loop starts for a Queue
        Pop element from the left
        Traverse its neighbor
            Reduce InDegree of each neighbor by 1
            If InDegree of a neighbor == 0
                Push indegree neighbor Nodes in Queue

Time Complexity: O(V+E)
"""
import collections


class Solution:
    @staticmethod
    def topological_sort(v, adj_list):
        q = collections.deque()
        # n = len(adj_list)
        indegree = [0] * v
        ans = []

        # Get Node's Indegree
        for i in range(v):
            for x in adj_list[i]:
                indegree[x] += 1

        # Get first indegree elements in queue
        for j in range(v):
            if indegree[j] == 0:
                q.append(j)

        # BFS
        while q:
            element = q.popleft()
            ans.append(element)
            for x in adj_list[element]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)
        return ans, indegree

    @staticmethod
    def verify_topological_sort(in_degree, vertex):
        """
        There are two-way to verify Topological sort
            i. if v == len(topological_order):
                    True
                else:
                    False
            ii. Iterate over indegree once. All its value should be 0
                If not 0 then its a cyclic graph, and return False
        """
        for i in range(vertex - 1):
            if in_degree[i] != 0:
                return False
        return True

    @staticmethod
    def edge_to_adj_list(v, edge_list):
        adj_list = [[] for _ in range(v)]
        for u_node, v_node in edge_list:
            adj_list[u_node].append(v_node)
        return adj_list

    def main(self, vertex, edge_list):
        adjacency_list = self.edge_to_adj_list(vertex, edge_list)
        topo_order, in_degree = self.topological_sort(vertex, adjacency_list)
        is_valid = self.verify_topological_sort(in_degree, vertex)
        return topo_order if is_valid else is_valid


if __name__ == '__main__':
    edges = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]]
    Vertex = 6
    print(Solution().main(Vertex, edges))
