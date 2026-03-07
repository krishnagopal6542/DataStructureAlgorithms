# Leet code: 210 : Course Schedule II
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjacency list
        graph = [[] for I in range(numCourses)]
        for edge in prerequisites:
            a, b = edge[0], edge[1]
            graph[b].append(a)

        # Create indegree for each Node
        indegree = [0] * numCourses
        for i in range(numCourses):
            if graph[i]:
                for x in graph[i]:
                    indegree[x] += 1

        # Initialize queue with nodes having indegree 0
        q = collections.deque()
        for j in range(numCourses):
            if indegree[j] == 0:
                q.append(j)

        ans = []
        while q:
            element = q.popleft()
            ans.append(element)
            for x in graph[element]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)
        if len(ans) != numCourses:
            return []
        return ans

if __name__ =='__main__':
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(Solution().findOrder(numCourses=numCourses, prerequisites=prerequisites))
