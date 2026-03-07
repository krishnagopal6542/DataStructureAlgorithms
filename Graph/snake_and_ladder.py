# Leet Code: 909
import collections
from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def snakes_and_ladders(board: List[List[int]]) -> int:
        n = len(board)

        # PART-1 : Making the board easier to comprehend
        node: int = 1
        flag = True
        connections = [-1] * (n * n + 1)

        for i in range(n - 1, -1, -1):
            if flag:
                # Traverse from left to right
                for j in range(n):
                    if board[i][j] != -1:
                        destination = board[i][j]
                        connections[node] = destination
                    node += 1
            else:
                # Traverse from right to left
                for j in range(n - 1, -1, -1):
                    if board[i][j] != -1:
                        destination = board[i][j]
                        connections[node] = destination
                    node += 1
            flag = not flag

        # PART-2 : Building Graph
        graph = defaultdict(list)
        for i in range(1, n * n):
            for count in range(1, 7):
                nbr = i + count
                if nbr <= n * n:
                    if connections[nbr] != -1:
                        # Has ladder or snake
                        graph[i].append(connections[nbr])
                    else:
                        graph[i].append(nbr)

        # PART-3 :Finding the shortest path
        level: int = 0
        visited: list[int] = [0] * (n * n + 1)
        q = collections.deque()
        q.append(1)

        while q:
            q_size = len(q)
            while q_size > 0:
                pos = q.popleft()
                if pos == n * n:
                    return level

                for nbr in graph[pos]:
                    if not visited[nbr]:
                        visited[nbr] = 1
                        q.append(nbr)
                q_size -= 1
            level += 1
        return -1


if __name__ == '__main__':
    """ Given board is in Boustrophedon style """
    given_board = [[-1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1],
                   [-1, 35, -1, -1, 13, -1],
                   [-1, -1, -1, -1, -1, -1],
                   [-1, 15, -1, -1, -1, -1]]
    print(Solution().snakes_and_ladders(board=given_board))
