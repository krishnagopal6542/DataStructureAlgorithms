import collections
from typing import List


class Solution:
    @staticmethod
    def can_finish(num_courses: int, pre_requisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(num_courses)]
        for edge in pre_requisites:
            a, b = edge[0], edge[1]
            graph[b].append(a)

        # Calculates InDegree of the Nodes
        indegree = [0] * num_courses
        for i in range(num_courses):
            if graph[i]:
                for x in graph[i]:
                    indegree[x] += 1

        # Get first 0 indegree element
        q = collections.deque()
        for j in range(num_courses):
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

        return True if len(ans) == num_courses else False


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(Solution().can_finish(num_courses=numCourses, pre_requisites=prerequisites))
