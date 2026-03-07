# Leet Code: 2360
from typing import List


class Solution:
    longest_cycle_length = -1

    def dfs_find_long_cycle(self, cycle_length, node, current_path, visited_node_list, edges):
        cycle_length += 1
        current_path[node] = cycle_length
        visited_node_list[node] = 1

        nbr = edges[node]
        if nbr != -1:
            if visited_node_list[nbr] and current_path[nbr] > 0:
                current_cycle_length = current_path[node] - current_path[nbr] + 1
                Solution.longest_cycle_length = max(Solution.longest_cycle_length, current_cycle_length)
            elif not visited_node_list[nbr]:
                self.dfs_find_long_cycle(cycle_length, nbr, current_path, visited_node_list, edges)

        current_path[node] = 0

    def longest_cycle(self, edges: List[int]) -> int:
        numOfNodes = len(edges)
        visitedNodeList = [0] * numOfNodes
        currentPath = [0] * numOfNodes
        Solution.longest_cycle_length = -1  #Reset for each test case

        for i in range(numOfNodes):
            if not visitedNodeList[i]:
                self.dfs_find_long_cycle(0, i, currentPath, visitedNodeList, edges)
        return Solution.longest_cycle_length



if __name__ == '__main__':
    edge_list = [-1,4,-1,2,0,4]
    print(Solution().longest_cycle(edge_list))
