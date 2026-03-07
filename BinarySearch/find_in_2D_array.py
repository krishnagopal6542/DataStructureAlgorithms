def search_in_matrix(matrix, target):
    i, j = 0, len(matrix[0]) - 1
    n, m = len(matrix), len(matrix[0])

    while 0 <= i < n and 0 <= j < m:
        if matrix[i][j] == target:
            return [i, j]
        elif matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
    return -1


if __name__ == '__main__':
    _matrix = [[1, 3, 5, 7],
               [10, 11, 16, 20],
               [23, 30, 34, 60]]
    element = 11
    print(search_in_matrix(_matrix, element))
