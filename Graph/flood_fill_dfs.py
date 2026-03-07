# Leet Code : 733

class Solution:
    def __init__(self):
        self.c = None
        self.r = None
        self.dx = [-1,0,1,0]
        self.dy = [0,1,0,-1]

    def dfs(self, i, j, org_color, color, image):
        if i<0 or j < 0 or i >= self.r or j >= self.c or image[i][j] != org_color:
            return

        image[i][j] = color

        for k in range(4):
            ii = i + self.dx[k]
            jj = j + self.dy[k]
            self.dfs(ii, jj, org_color, color, image)

    def flood_fill(self, image, sr, sc, color):
        # source is given
        # save the color
        # go to the connected cells of the same color
        # if it is a valid cell, change its color to the given color
        self.r = len(image)
        self.c = len(image[0])

        original_color = image[sr][sc]
        if original_color == color:
            return image
        self.dfs(sr, sc, original_color, color, image)
        return image


if __name__ == '__main__':
    given_image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    source_row = 1
    source_column = 1
    given_color = 2
    print(Solution().flood_fill(image=given_image, sr=source_row, sc=source_column, color=given_color))