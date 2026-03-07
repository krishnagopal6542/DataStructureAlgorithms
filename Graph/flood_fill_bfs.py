# Leet Code : 733
import collections


class Solution:
    def __init__(self):
        self.c = None
        self.r = None
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, 1, 0, -1]

    def bfs(self, i, j, org_color, color, image):
        q = collections.deque()
        q.append((i, j))
        image[i][j] = color

        while q:
            ele = q.popleft()
            i, j = ele[0], ele[1]

            for k in range(4):
                ii = i + self.dx[k]
                jj = j + self.dy[k]
                if ii < 0 or jj < 0 or ii >= self.r or jj >= self.c or image[ii][jj] != org_color:
                    continue
                q.append((ii, jj))
                image[ii][jj] = color

    def flood_fill(self, image, sr, sc, color):
        self.r = len(image)
        self.c = len(image[0])

        original_color = image[sr][sc]
        if original_color == color:
            return image
        self.bfs(sr, sc, original_color, color, image)
        return image


if __name__ == '__main__':
    given_image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    source_row = 1
    source_column = 1
    given_color = 2
    print(Solution().flood_fill(image=given_image, sr=source_row, sc=source_column, color=given_color))
